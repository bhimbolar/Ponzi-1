from django.db import models

# Create your models here.

MATRIX = (
    ('2:1', '2:1'),
    ('3:1', '3:1'),
    ('4:1', '4:1')
)


class Plans(models.Model):
    name = models.CharField(max_length=20, default="", blank=False)
    amount = models.CharField(max_length=10, default="", blank=False)
    matrix = models.CharField(choices=MATRIX, max_length=10, default="2:1", blank=False)
    assign = models.CharField(max_length=20, default="Auto Assign", blank=False)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Plans'
