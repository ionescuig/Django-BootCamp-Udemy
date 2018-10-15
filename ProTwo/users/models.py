from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.first_name+' '+self.last_name
        
