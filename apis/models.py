from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Produtos(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    price=models.CharField(max_length=10)
    cost=models.CharField(max_length=10, blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='produtos', blank=True,null=True)

    def __str__(self):
        return "%s" % self.title


class Disciplina(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    professor=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.title
