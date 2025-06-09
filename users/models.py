from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
import uuid

class User(AbstractUser, PermissionsMixin):
    ROLE_ENUM = [
        ('employer', 'Employer'),
        ('jobseeker', 'JobSeeker'),
        ('superAdmin', 'SuperAdmin'),
        ('admin', 'Admin')
    ]
    
    # Remove username completely
    username = None
    
    # Personal info (matches database columns)
    firstName = models.CharField(max_length=45, db_column='firstName')
    lastName = models.CharField(max_length=150, db_column='lastName')
    
    # Required auth fields (mapped to actual DB columns)
    email = models.EmailField(max_length=45, unique=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    
    # Status fields (match exact DB column names)
    is_active = models.BooleanField(default=True, db_column='is_active')
    is_staff = models.BooleanField(default=False, db_column='isStaff')
    is_superuser = models.BooleanField(default=False, db_column='isSuperuser')
    last_login = models.DateTimeField(null=True, blank=True, db_column='lastLogin')
    
    # Your custom fields (match exact DB column names)
    is_deleted = models.BooleanField(default=False, db_column='is_deleted')
    is_suspended = models.BooleanField(default=False, db_column='is_suspended')
    is_pending = models.BooleanField(default=True, db_column='is_pending')
    isVerified = models.BooleanField(default=False, db_column='isVerified')
    verificationCode = models.CharField(max_length=45, blank=True, null=True, db_column='verificationCode')
    role = models.CharField(max_length=20, choices=ROLE_ENUM, null=True, blank=True, db_column='role')
    createdAt = models.DateTimeField(auto_now_add=True, db_column='createdAt')
    updatedAt = models.DateTimeField(auto_now=True, db_column='updatedAt')
    date_joined = models.DateTimeField(auto_now_add=True, db_column='dateJoined')
    
    # Additional fields from your DB table
    deleted_at = models.DateTimeField(null=True, blank=True, db_column='deleted_at')
    deletion_reason = models.TextField(null=True, blank=True, db_column='deletion_reason')
    
    # Relationships (keep your existing)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name="custom_user_groups",
        related_query_name="custom_user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name="custom_user_permissions",
        related_query_name="custom_user",
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstName', 'lastName']
    
    # Property aliases for Django internals
    @property
    def is_staff(self):
        return self.is_staff
    
    @is_staff.setter
    def is_staff(self, value):
        self.is_staff = value
        
    @property
    def is_superuser(self):
        return self.is_superuser
    
    @is_superuser.setter
    def is_superuser(self, value):
        self.is_superuser = value
        
    
        
    @property
    def last_login(self):
        return self.last_login
    
    @last_login.setter
    def last_login(self, value):
        self.last_login = value
        
    @property
    def date_joined(self):
        return self.date_joined
    
    @date_joined.setter
    def date_joined(self, value):
        self.date_joined = value
    
    @property
    def first_name(self):
        return self.firstName
    
    @first_name.setter
    def first_name(self, value):
        self.firstName = value
    
    @property
    def last_name(self):
        return self.lastName  
    
    @last_name.setter
    def last_name(self, value):
        self.lastName = value

    class Meta:
        db_table = "users"