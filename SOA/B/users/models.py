from django.db import models
from apps.tenant.models import Tenant, Role
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    email = models.EmailField(blank=False, max_length=254, unique=True, db_index=True, verbose_name="email address")
    avatar = models.ImageField(blank=True, null=True, upload_to='users/')
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    

    tenant = models.ForeignKey(Tenant, blank=True, null=True, on_delete=models.CASCADE, related_name='users')
    roles = models.ManyToManyField(Role, related_name='users')

    USERNAME_FIELD = "username"   # e.g: "username", "email"
    EMAIL_FIELD = "email"         # e.g: "email", "primary_email"

    # 1	_state	ModelState	It is used to preserve the state of the user.
    # 2	id	Number	Unique ID for each user.
    # 3	password	string	Encrypted password for the user.
    # 4	last_login	datetime	Date and time when user logged in last time.
    # 5	is_superuser	bool	True if the user is superuser, otherwise false.
    # 6	username	string	Unique username for the user.
    # 7	first_name	string	First name of the user.
    # 8	last_name	string	Last name of the user.
    # 9	email	email	Email ID of the user.
    # 10 is_staff	bool	Set true if the user is a staff member, else false.
    # 11 is_active	bool	Is profile active.
    # 12 date_joined	datetime	Date and time when the user joined the first time. It is usually when the user signs up or creates a user account the first time.
    
    def __str__(self):
        return self.email

    
