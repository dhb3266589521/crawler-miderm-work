from django.db import models

# Create your models here.
class mymodel(models.Model):
    title=models.CharField(default='主题',max_length=50)
    actor=models.CharField(default='演员',max_length=50)

    def __str__(self):
        return self.title

    def short_actor(self):
        return self.actor[:70]+'...'