from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Password_Register_Validator:
    
    def __init__(self):
        self.min_length = 8
        self.max_upper_case = 1
        self.max_lower_case = 1
        
        
    def validate_min_length_password(self, password):
        if len(password) < self.min_length:
            raise ValidationError(f'É necessário no mínimo 8 caracteres.')

    def validate_upper_case(self, password):
        if not any(chr.isupper() for chr in password):
            raise ValidationError(f'É necessário no mínimo 1 letra maiúscula.')

    def validate_number_case(self, password):
        if not any(chr.isdigit() for chr in password):
            raise ValidationError(f'É necessário no mínimo 1 número.')
