from django.db import models
import uuid

# Create your models here.
class  User(models.Model):
    ROLE_ENUM = [
        
        ('employer','Employer'),
        ('jobseeker','JobSeeker'),
        ('superAdmin','SuperAdmin'),
        ('admin','Admin')
    ]

    id = models.AutoField(primary_key = True)
    firstName = models.CharField(max_length=45)
    secondName = models.CharField(max_length=45)
    email=models.CharField(max_length=45, unique=True)
    is_active = models.BooleanField(default=True) 
    password=models.CharField(max_length=255)
    isVerified=models.BooleanField(default=False)
    verificationCode = models.UUIDField(default=uuid.uuid4, editable=False)
    role=models.CharField(max_length=20,choices=ROLE_ENUM,null=True,blank=True)
    createdAt  = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"
        managed = False

        def __str__(self):
            return self.email