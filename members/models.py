from django.db import models

# Create your models here.
class Member(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name