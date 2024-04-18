# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, User
from core_access.forms import LoginForm, RegisterForm, AccountCreationForm, ProfileForm, AccountPasswordChangeForm, ProfileLoggedForm, Password_ResetForm
from core_access.models import User
from django.conf import settings
from django.db import DatabaseError
from core_access.filters.user_filter import UserFilter
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import permission_required
from django.db.models import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.conf import settings
from django.core.mail import send_mail

from core_log.save_db.create_log import save_log


def LoginView(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None and user.login_disabled is False:
                login(request, user)
                next_url = request.GET.get('next')
                if next_url:
                    return HttpResponseRedirect(next_url)
                else:
                    return redirect("inicio")
            else:
                msg = 'Credenciais inválidas, tente novamente.'

        else:
            msg = 'Erro de validação.'

    return render(request, "users/login.html", {"form": form, "msg": msg, })


def RegisterView(request):
    form = RegisterForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form["username"].value()
            email = form["email"].value()
            password1 = form.cleaned_data.get("password1")
            password2 = form.cleaned_data.get("password2")

            try:
                test_user = User.objects.get(username=username)
            except:
                test_user = None

            try:
                observer_group = Group.objects.get(name='Observador')
            except ObjectDoesNotExist:
                observer_group = None

            if observer_group is None:
                msg = f'Desculpe. O sistema ainda não está recebendo novos usuários.'
            elif len(username) < 4:
                msg = f'Username possui tamanho muito pequeno.'
                form.cleaned_data.get("username")

            elif test_user is not None:
                msg = f'O nome de usuário já existe'

            elif password1 != password2:
                msg = f'As duas senhas digitadas divergem.'
            else:
                user = User()
                user.username = username
                user.email = email
                user.is_active = True
                user.set_password(password1)
                try:
                    user.save()
                    observer_group.user_set.add(user)
                    return redirect("login")
                except DatabaseError as e:
                    msg = e.args

    return render(request, "users/register.html", {"form": form, "msg": msg})


def ResetPasswordView(request):
    form = Password_ResetForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            email = form["email"].value()
            user = User.objects.get(email=email)

            if user:
                subject = "Recuperação de senha - Portal F1"
                html_message =  f"Para redefinir sua senha, favor clicar <a href={settings.URL_APPLICATION_FOR_RESET_PW}/reset_password/" + urlsafe_base64_encode(force_bytes(user.pk)) + "/" + default_token_generator.make_token(user)+">aqui</a>"
                send_mail(subject, "", settings.EMAIL_HOST_USER, [user.email], fail_silently=False, html_message=html_message)
                return render(request, 'users/reset_password_sent.html')
    form = Password_ResetForm()
    return render(request, 'users/reset_password.html', {'form': form})


# cadastrar novo usuário - ADM
class AccountCreationView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    template_name = 'users/user.html'
    model = User
    form_class = AccountCreationForm
    success_url = reverse_lazy('list_user')
    permission_required = 'core_access.add_user'

    def form_valid(self, form):
        user_cpf = False
        if form['cpf'].value() != '':
            user_cpf = User.objects.filter(Q(cpf=form['cpf'].value()))

        if user_cpf:
            form.add_error('cpf', 'CPF já cadastrado!')
            return self.form_invalid(form)

        url = super().form_valid(form)

        new_user = User.objects.get(pk=self.object.pk)
        try:
            group = Group.objects.get(id=int(form['group'].value()))
            group.user_set.add(new_user)
        except:
            print('Grupo não encontrado!')

        save_log(new=new_user, user=self.request.user)
        return url


# Alterar usuário logado
class ProfileUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    template_name = 'users/user_profile_update.html'
    model = User
    form_class = ProfileLoggedForm
    success_url = reverse_lazy('index')
    permission_required = 'core_access.change_user'

    def get_object(self, queryset=None):
        self.object = get_object_or_404(User, id=self.request.user.id)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Perfil de Usuário'
        context['botao'] = 'Salvar'
        return context

    def form_valid(self, form):
        previous_user = User.objects.get(pk=self.kwargs['pk'])
        user_cpf = False
        if form['cpf'].value() != '':
            user_cpf = User.objects.filter(Q(cpf=form['cpf'].value()), ~Q(id=self.object.id))

        if user_cpf:
            form.add_error('cpf', 'CPF já cadastrado!')
            return self.form_invalid(form)

        url = super().form_valid(form)
        new_user = User.objects.get(pk=self.kwargs['pk'])
        save_log(old=previous_user, new=new_user, user=self.request.user)
        return url


# Administrador altera cadastro de usuários
class ProfileAdmUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    template_name = 'users/user_update.html'
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('list_user')
    permission_required = 'core_access.change_user'

    def get_initial(self):
        user = User.objects.get(id=self.kwargs['pk'])
        if user.groups.all().exists():
            group_user = User.groups.through.objects.get(user=user)

            return {'group': Group.objects.filter(id=group_user.group_id).values('id')[0]['id']}

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Perfil de Usuário'
        context['botao'] = 'Salvar'
        context['groups'] = Group.objects.all()
        context['user'] = self.request.user
        return context

    def form_valid(self, form):
        previous_user = User.objects.get(pk=self.object.pk)
        user_cpf = False
        if form['cpf'].value() != '':
            user_cpf = User.objects.filter(Q(cpf=form['cpf'].value()), ~Q(id=self.object.id))

        if user_cpf:
            form.add_error('cpf', 'CPF já cadastrado!')
            return self.form_invalid(form)

        url = super().form_valid(form)

        new_user = User.objects.get(pk=self.object.pk)
        try:
            group = Group.objects.get(id=int(form['group'].value()))
            group.user_set.add(new_user)
        except:
            print('Grupo não encontrado!')

        save_log(old=previous_user, new=new_user, user=self.request.user)
        return url


# alterar senha do usuário logado
@login_required(login_url='/login')
@permission_required('core_access.change_user')
def AccountPasswordChangeView(request):
    if request.method == "POST":
        form_senha = AccountPasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            previous_user = User.objects.get(pk=request.user.id)
            user = form_senha.save()
            new_user = User.objects.get(pk=request.user.id)
            save_log(old=previous_user, new=new_user, user=request.user)
            update_session_auth_hash(request, user)
            return redirect('index')
    else:
        form_senha = AccountPasswordChangeForm(request.user)

    return render(request, 'users/user_password_change.html', {'form_senha': form_senha})


# listar usuários cadastrados
class UserList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = User
    template_name = 'users/user_list.html'
    paginate_by = 10
    permission_required = ['core_access.view_user']

    def dispatch(self, request, *args, **kwargs):
        return super(UserList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = UserFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return UserFilter(self.request.GET, queryset=queryset).qs
