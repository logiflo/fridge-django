from django.db import models
from django.contrib.auth.models import User

class Essencial(models.Model):
    """Essencials in your fridge.
    """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    UNIT_CHOICES =[
        ('Kg', 'Kilogram'),
        ('g', 'Gram'),
        ('L', 'Litre'),
        ('unit', 'Unit'),
    ]
    units = models.CharField(max_length=15, choices=UNIT_CHOICES)

    quantity = models.FloatField(default=0.0)


    def __str__(self):
        """Return a string representation of the model
        """
        return self.text


class Food(models.Model):
    """Food in the fridge.
    """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    UNIT_CHOICES =[
        ('Kg', 'Kilogram'),
        ('g', 'Gram'),
        ('L', 'Litre'),
        ('unit', 'Unit'),
    ]
    units = models.CharField(max_length=15, choices=UNIT_CHOICES)

    quantity = models.FloatField(default=0.0)

    class Meta:
        verbose_name_plural = 'Food'

    def __str__(self):
        """Return a string representation of the model
        """
        return self.text

