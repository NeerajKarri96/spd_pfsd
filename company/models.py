from django.db import models

# Create your models here.
class Jobdetails(models.Model):
    job_title=models.TextField()
    job_des=models.TextField()
    job_req=models.TextField()
    job_sal=models.TextField()
    work_loc=models.CharField(max_length=50)
    app_email=models.EmailField()

    def __str__(self):
        return self.job_title