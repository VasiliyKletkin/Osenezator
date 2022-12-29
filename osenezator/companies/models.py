from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return f"{self.name}"
