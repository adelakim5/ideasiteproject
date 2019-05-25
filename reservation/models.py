from django.db import models

# Create your models here.
class Reservation(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    pub_date = models.DateTimeField("data published")

    def __str__(self):
        return self.title

class review(models.Model):
    name = models.CharField(max_length=20)
    guest_count = models.IntegerField()
    pub_date = models.DateTimeField('date published')
    body = models.TextField(max_length=1000)
    store_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name