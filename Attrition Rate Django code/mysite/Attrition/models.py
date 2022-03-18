from django.db import models


class Attrition_table(models.Model):
    table_id = models.AutoField(primary_key=True)
    name = models.CharField(null=True, blank=True, max_length=200)
    location = models.CharField(null=True, blank=True, max_length=50)
    emp_group = models.CharField(null=True, blank=True, max_length=20)
    function = models.CharField(null=True, blank=True, max_length=20)
    gender = models.CharField(null=True, blank=True, max_length=10)
    tenure_group = models.CharField(null=True, blank=True, max_length=10, default="< =1")
    experience = models.FloatField(null=True, blank=True, default=0.0)
    maritial = models.CharField(null=True, blank=True, max_length=30)
    age = models.FloatField(null=True, blank=True, default=25.0)
    hiring_source = models.CharField(max_length=40)
    promoted_before = models.CharField(null=True, blank=True, max_length=40)
    job_role = models.CharField(null=True, blank=True, max_length=10) # this is yes or no

    def __str__(self):
        return self.name