from django.db import models

# Create your models here.

class ForbiddenWord(models.Model):
    id=models.AutoField(primary_key=True,editable=False)
    word = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.word