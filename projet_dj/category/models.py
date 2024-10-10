from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re

def validate_letters_only(value):
    if not  re.match('^[A-Za-z\s]+$',value):
        raise ValidationError('this field must only contain letters')
    


class Category(models.Model):

    #letters_only=RegexValidator(r'^[A-Za-z\s]+$','only letters are allowed ')
    #title=models.CharField(max_length=225,validators=[letters_only])
    title=models.CharField(max_length=225,validators=[validate_letters_only])
    created_at=models.DateTimeField(auto_now_add=True)

    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural="categories"