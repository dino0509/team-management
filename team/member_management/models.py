from django.db import models
from django.forms import ModelForm

class TeamMember(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=17, null=True)
    is_admin = models.BooleanField()
    add_date = models.DateTimeField()
    def __str__(self):
        res = self.first_name + " " + self.last_name
        if self.is_admin:
            res = res + " (admin)"
        return res
