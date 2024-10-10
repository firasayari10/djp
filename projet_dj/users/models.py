from django.db import models
from gestion.models import gestion
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
def email_validator(value):
      if not value.endswith('@esprit.tn'):
            raise ValidationError ('email must be @esprit.tn  domain is  allowed ')

class Participant(AbstractUser):
    cin_validator=RegexValidator(
          regex=r'^\d{8}$',
          message='this field must containt exactly 8 digits'
    )
    cin=models.CharField(primary_key=True,max_length=10,validators=[cin_validator])
    email=models.EmailField(unique=True,max_length=255,validators=[email_validator])
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    username=models.CharField(unique=True,max_length=255)
    USERNAME_FIELD='username'

    CHOICES=(
        ('etudiant','etudiant'),
        ('chercher','chercheur'),
        ('docteur','doncteur'),
        ('enseignant','enseignant'),
    )
    participant_category=models.CharField(max_length=255,choices=CHOICES)
    reservations=models.ManyToManyField (gestion,through='reservation') 
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural="Participants"


class reservation(models.Model):
        conference=models.ForeignKey(gestion,on_delete=models.CASCADE)
        participant =models.ForeignKey(Participant,on_delete=models.CASCADE)
        confirmed=models.BooleanField(default=False)
        reservation_date=models.DateTimeField(auto_now_add=True)
        def clean(self):
              if self.conference.start_date  < timezone.now().date():
                    raise ValidationError('you can only reserve for upcoming conferences ! ')
              
              reservation_count=reservation.objects.filter(
                    Participant=self.participant,
                    reservation_date=self.reservation_date

              )
              if reservation_count >= 3 :
                    raise ValidationError(' you can only make 3 reservations a day ')
        class Meta :
              verbose_name_plural="Reservations"
              unique_together=('conference','participant')
            
            


    