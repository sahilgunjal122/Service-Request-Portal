from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ServiceRequest(models.Model):

    STATUS_PENDING='Pending'
    STATUS_IN_PROGRESS='In Progress'
    STATUS_COMPLETED='Completed'

    STATUS =[
        (STATUS_PENDING,'Pending'),
        (STATUS_IN_PROGRESS,'In Progress'),
        (STATUS_COMPLETED,'Completed')
    ]



    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    description=models.TextField()
    attachment=models.FileField(upload_to='attachments/', blank=True,null=True)
    submitted_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=30,choices=STATUS,default=STATUS_PENDING)

    def __str__(self):
        return f"{self.title} by {self.user.username}"
    
