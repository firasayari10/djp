from django.db import models
from category.models import Category
from django.core.validators import MaxValueValidator,FileExtensionValidator
# Create your models here.
from django.core.exceptions import ValidationError
from django.utils import timezone
#import datetime
class gestion(models.Model):

   title=models.CharField(max_length=255)
   description=models.TextField()
   start_date=models.DateField(default=timezone.now().date())

   end_date=models.DateField()
   location=models.CharField(max_length=255)
   price=models.FloatField()
   capacite=models.IntegerField(validators=[MaxValueValidator(limit_value=100,message="capacity must be under 100")])

   program=models.FileField(upload_to='desktop/',validators=[FileExtensionValidator(allowed_extensions=['pdf','png','jpeg','jpg'],message='only pdf ,jpeg , jpg ,png are allowed')])
   created_at=models.DateTimeField(auto_now_add=True)
   updated_at=models.DateTimeField(auto_now=True)
   category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="gestions")

   def clean(self):
       if self.end_date <= self.start_date:
           raise ValidationError('End date must be greater than start date  ! ')
   class Meta:
        constraints=[
            models.CheckConstraint(
                check=models.Q(
                    start_date__gte=timezone.now().date(),
                    ),
                    name="the start date must be greater or equal to  today "
            )
        ]
        verbose_name_plural="Conferences"


   

