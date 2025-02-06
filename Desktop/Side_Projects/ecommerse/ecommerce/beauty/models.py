from django.db import models

# Create your models here.
class ToDolist(models.Model):
     name=models.CharField(max_length=200)

     def __str___(self):
          return self.name
     
class item(models.Model):
     todolist = models.ForeignKey(ToDolist, on_delete = models.CASCADE)    
     text = models.CharField(max_length=300)
     complete = models.BooleanField() 

     def __str___(self):
          return self.text