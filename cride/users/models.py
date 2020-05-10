"""Users app."""

# Django 
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utilities
from cride.utils.models import CRideModel


class User(CRideModel, AbstractUser):
    """Users app.

    Extends from Django's Abstract user, change the username field
    to email and add some extra fields
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_message={
            'unique': 'A user with that email already exists'
        }
    )

    phone_number = models.CharField(max_length=17, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['username', 'first_name', 'last_name']

    is_client = models.BooleandField(
        'client status',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries'
            'Client are the main type of user'
        )
    )

    is_verified = models.BooleandField(
        'verified',
        default=True,
        help_text='Set to true when the user have verified its email address'
    )