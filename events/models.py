from django.db import models

# Create your models here.


class EventInfo(models.Model):
    event_name = models.CharField(max_length=255)
    description = models.CharField(max_length=1026, null=True)
    organised_by = models.CharField(max_length=255)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return self.event_name

    class Meta:
        ordering = ["start_date"]


class EventRegistration(models.Model):
    event = models.ForeignKey(EventInfo, on_delete=models.CASCADE)
    student_id = models.IntegerField(unique=True,null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    department = models.CharField(max_length=600)
    reg_date = models.DateTimeField(auto_now_add=True, null=True)
    is_confirmed = models.BooleanField(default=False)
