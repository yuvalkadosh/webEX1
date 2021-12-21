import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from django.contrib.auth.hashers import (
    check_password,
)


class DictValidator(object):
    def __init__(self, dict_path=None):
        self.dict_path = dict_path

    def validate(self, password, user=None):
        isValid = True
        f = open(self.dict_path, "r")
        for line in f:
            
            if password == line.strip():
                isValid = False


        if not isValid:
            raise ValidationError(
                _("Your password is predictable and published online, try a different one!"),
                code='password_in_dict',
            )

    def get_help_text(self):
        return _(
            "Your password must not be predictable"
        )


class ComplexValidator(object):
    def __init__(self, categories_amount=3):
        self.categories_amount = categories_amount

    def validate(self, password, user=None):
        count = 0
        if re.findall('[a-z]', password):
            count += 1
        if re.findall('[A-Z]', password):
            count += 1    
        if re.findall('\d', password):
            count += 1
        if re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            count += 1

        if count < self.categories_amount:
            raise ValidationError(
                _("Your password must contains " + str(self.categories_amount) + " of the 4 character categories: Lowercase, Uppercase, Numbers, Symbols"),
                code='password_not_complex',
            )

    def get_help_text(self):
        return _(
            "Your password must contains " + str(self.categories_amount) + " of the 4 character categories: Lowercase, Uppercase, Numbers, Symbols"
        )


class HistoryValidator(object):
    def __init__(self, last_pass_amount=1):
       self.last_pass_amount = last_pass_amount

    def validate(self, password, user=None):
        isNotValid=True

        match self.last_pass_amount:
            case 0:        
                return True
            case 4:
                isNotValid = check_password(password,user.password) or check_password(password,user.password2) or check_password(password,user.password3) or check_password(password,user.password4)
            case 3:
                isNotValid = check_password(password,user.password) or check_password(password,user.password2) or check_password(password,user.password3)
            case 2:        
                isNotValid = check_password(password,user.password) or check_password(password,user.password2)
            case 1:        
                isNotValid = check_password(password,user.password)
            

        if isNotValid:
            raise ValidationError(
                _("The password must be different then last passwords!"),
                code='password_not_different_then_last',
            )

    def get_help_text(self):
        return _(
            "The password must be different then last passwords!"
        )