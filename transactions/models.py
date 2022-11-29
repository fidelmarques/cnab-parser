from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Transaction(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    type = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(9),
        ]
    )
    date = models.DateField()
    value = models.DecimalField(max_digits=15, decimal_places=2)
    cpf = models.TextField()
    card = models.TextField()
    hour = models.TimeField()
    shop_owner = models.TextField()
    shop_name = models.TextField()
