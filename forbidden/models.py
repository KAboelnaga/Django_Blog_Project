from django.db import models

# Create your models here.

class ForbiddenWord(models.Model):
    ID=models.AutoField(primary_key=True,editable=False)
    Name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.word