from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class Location(models.Model):
    KERK = 'K'
    CREMATORIUM = 'C'
    AULA = 'A'
    TYPE_CHOICES = (
        ('K', 'Kerk'),
        ('C', 'Crematorium'),
        ('A', 'Aula'),
    )
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default=KERK)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(null=True, blank=True)

    def clean(self):
        cleaned_data = super(Location, self).clean()
        if self.name == 'Calslaan':
            raise ValidationError('Deze naam mag niet gekozen worden!')
        return cleaned_data

    def get_absolute_url(self):
        return u'/locaties/%d' % self.id