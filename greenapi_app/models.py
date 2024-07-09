from django.db import models
from django import forms


class GreenAPIInstance(models.Model):
    id_instance = models.CharField(max_length=50,verbose_name='ID инстанса')
    api_token_instance = models.CharField(max_length=100,verbose_name='API токен')

    def __str__(self):
        return self.id_instance


class GreenAPIInstanceForm(forms.ModelForm):
    class Meta:
        model = GreenAPIInstance
        fields = ['id_instance', 'api_token_instance']
