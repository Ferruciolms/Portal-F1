# Software - F1 [Django](https://appseed.us/admin-dashboards/django) 

Utilizando a versão Free do template [Admin dashboard](https://appseed.us/admin-dashboards) gerado por AppSeed em **[Django](https://appseed.us/admin-dashboards/django)** Framework.

[Gradient Able](https://appseed.us/admin-dashboards/django-dashboard-gradient-pro) template FREE utilizando BoodsTrap 4

## Code-base structure

A estrutura do código segue

```bash
< PROJECT ROOT >
   |
   |-- app_web/                             # Raiz do projeto, onde vão estar todos os arquivos comuns
   |    |-- applications/                    # Dentro dessa pasta estão as aplicações do Django
   |    |-- core/
   |        |-- wsgi.py                     # Starta a aplicação em produção
   |        |-- urls.py                     # Define as urls permitidas
            |-- settings.py                 # Configurações do Projeto
   |    |-- core_pages                      # Aplicação que contem páginas que são comuns para o projeto
   |    |-- core_access                      # Aplicação de controle de usuarios
   |    |-- nginx                           # Para o servidor em produção (precisa ser estudado)
   |    |-- static                          # Arquivos estaticos
   |    |-- docker-compose.yml              # Arquivo para criar o container
   |    |-- Dockerfile                      # Arquivo para constuir o container
   |    |-- requirements.txt                    # Bibliotecas necessárias
   |    |-- .env                                # Inject Configuration via Environment
   |    |-- manage.py                           # Start the app - Django default start script
   |-- ************************************************************************
```
<br />

