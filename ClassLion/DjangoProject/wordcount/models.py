from django.db import models

# Create your models here.
class Blog(models.Model):
    def summary(self):
        return self.body[:100]
