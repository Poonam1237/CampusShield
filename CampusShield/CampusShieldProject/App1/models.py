from django.db import models
import random


def generateid():
    return 'CAMPUS'+''.join(random.choices('0123456789',k=7))

class report(models.Model):
    c=[
        ('Ragging', 'Ragging'),
        ('Harassment', 'Harassment'),
        ('Mental Health', 'Mental Health'),
        ('Discrimination', 'Discrimination'),
        ('Academic Misconduct', 'Academic Misconduct'),
        ('Other', 'Other'),
    ]
    reportid=models.CharField(max_length=20,unique=True,default=generateid,editable=False)
    category=models.CharField(max_length=50,choices=c)
    description=models.TextField()
    time=models.DateTimeField(auto_now_add=True)
    isresolved=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.category} - {self.time.strftime('%d %b %Y %H:%M')}"



class Suggestion(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    submit_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Faculty(models.Model):
    name=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    department=models.CharField(max_length=200)
    email=models.EmailField()
    mobile=models.CharField(max_length=10)
    category = models.CharField(max_length=100, choices=[
        ('Ragging', 'Ragging'),
        ('Discrimination', 'Discrimination'),
        ('Mental Health', 'Mental Health'),
        ('Harassment', 'Harassment'),
        ('Academic Misconduct', 'Academic Misconduct'),
        ('Other', 'Other'),
    ])
    image=models.ImageField(upload_to='faculty_images/',blank=True,null=True)
    