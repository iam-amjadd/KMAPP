from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Shift(models.Model):
    name = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name

class Agentshift(models.Model):
    user = models.ForeignKey(
        User,
        related_name='agent',
        on_delete=models.CASCADE
    )
    date = models.DateField(
        null=True,
        blank=True
    )
    shifts = models.ForeignKey(
        Shift,
        related_name='agentShifts',
        null=True,
        on_delete=models.SET_NULL
    )
    
    class Meta:
        unique_together = ('user','date')

    def clean(self):
        if self.user.is_staff:
            raise ValidationError("Cannot add shifts to is_staff users.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        if self.shifts is not None:
            return f'{self.user.username} {self.shifts.name} {str(self.date)}'
        else:
            return f'{self.user.username} NULL {str(self.date)}'