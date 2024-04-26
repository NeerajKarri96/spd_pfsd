from django.db import models

# Create your models here.
class Application(models.Model):
    name=models.TextField()
    job_title=models.TextField()
    email=models.EmailField()

    def __str__(self):
        return self.job_title