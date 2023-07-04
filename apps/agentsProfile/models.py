from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Agentprofile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='agentprofile',
        on_delete=models.CASCADE,
        unique=True
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True
    )
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]
    gender = models.CharField(
        max_length=6,
        choices=gender_choices,
        null=True,
        blank=True
    )
    phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    address = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    job_position = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    department = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    employment_start_date = models.DateField(
        null=True,
        blank=True
    )
    supervisor = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    skills = models.TextField(
        null=True,
        blank=True
    )
    education = models.TextField(
        null=True,
        blank=True
    )
    experience = models.TextField(
        null=True,
        blank=True
    )
    emergency_contact_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    emergency_contact_phone = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_or_update_agentprofile(sender, instance, created, **kwargs):
    if created:
        try:
            agentprofile = instance.agentprofile
            instance.agentprofile.save()
        except Agentprofile.DoesNotExist:
            Agentprofile.objects.create(user=instance)
    else:
        instance.agentprofile.save()

