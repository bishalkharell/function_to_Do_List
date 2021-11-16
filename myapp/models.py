from django.db import models

# Create your models here.

class ToDoList(models.Model):
    textField = models.CharField(max_length =450)

    def __str__(self):
        return self.textField