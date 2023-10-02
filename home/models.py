from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    year = models.DateField()
    description = models.TextField()

    
    def __str__(self):
        return self.name

