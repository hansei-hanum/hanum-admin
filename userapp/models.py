from django.db import models

# Create your models here.

class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    phone = models.CharField(unique=True, max_length=11)
    name = models.CharField(max_length=5)
    profile = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        app_label = 'userapp'
        managed = False
        db_table = 'users'
    # def __str__(self):
    #     return self.id if self.id else "(None)"