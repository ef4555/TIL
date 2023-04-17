from django.db import models

# Create your models here.
class PetSitter(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    
    def __str__(self):
        return f'집사 {self.first_name}'
    
class Pet(models.Model):
    name = models.CharField(max_length=50)
    pet_sitter = models.ForeignKey(PetSitter, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name}'