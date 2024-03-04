import uuid

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils import timezone

from _gybase.models.base import BaseActiveTimeStampModel


class GyaanUserManager(UserManager):
    """Custom User Manager."""

    def create_first_superuser(self):
        """Check if admin users are present.

        If no admin users are present
        Then create an admin user

        Returns:
            The return value. Object for success, None otherwise.
        """
        if User.objects.filter(is_superuser=True).count() == 0:
            return super(GyaanUserManager, self).create_superuser(
                email="abhishekpandey241998@gmail.com", username="admin",
                password="abhishek@1234")
        return None
class User(AbstractUser):
    """Custom User Model."""

    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    )

    id = models.AutoField(primary_key=True, editable=False)
    gender = models.CharField(max_length=10, choices=GENDER, null=True, blank=True)

    objects = GyaanUserManager()


class Profile(BaseActiveTimeStampModel):

    email_init = models.EmailField(verbose_name='Initial Email Address', null=True)
    phone = models.CharField(null=True, max_length=30
    )
    date_of_birth = models.DateField(null=True)
    address = models.TextField(null=True)
    photo_url = models.URLField(default=None, null=True, help_text="An optional image of the user")
    alternate_phone = models.CharField(
        max_length=15,
        null=True,
    )
    locality = models.TextField(
        help_text="Verbose location of the user",
        default=None,
        null=True
    )
    city = models.CharField(
        max_length=20,
        default=None,
        null=True
    )
    preferred_languages = ArrayField(
        models.CharField(max_length=5),
        default=None,
        null=True,
        help_text="Language codes of preferred languages in the order of preference"
    )
    countries = ArrayField(
        models.CharField(max_length=20),
        default=None,
        null=True
    )
    country_of_origin = models.CharField(
        default=None,
        max_length=100,
        null=True
    )
    current_timezone = models.CharField(
        default=None,
        max_length=20,
        null=True
    )
    timezones = ArrayField(
        models.CharField(max_length=20),
        default=None,
        null=True
    )
    highest_education_qualification = models.CharField(
        max_length=15,
        null=True,
        default=None
    )
    birthday = models.DateField(default=None, null=True)
    year_of_completion = models.PositiveSmallIntegerField(blank=True, null=True)
    is_working = models.BooleanField(default=True)
    parent_or_guardian_name = models.CharField(max_length=30, null=True)
    parent_or_guardian_email = models.EmailField(null=True)
    parent_or_guardian_phone = models.CharField(
        max_length=15,
        default=None,
        null=True,
    )
    facebook_id = models.CharField(unique=True, null=True, max_length=15)
    google_plus = models.CharField(unique=True, null=True, max_length=15)
    linkedIn_id = models.CharField(unique=True, null=True, max_length=15)
    twitter_id = models.CharField(unique=True, null=True, max_length=15)
    github_id = models.CharField(unique=True, null=True, max_length=15)
    exams_interested_in = ArrayField(
        models.CharField(max_length=10),
        default=None,
        null=True,
    )

    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        related_name="profile",
        db_index=True,
    )

    friends = models.ManyToManyField(
        User,
        help_text="Users a user has befriended on this platform",
        related_name="friends",
        default=None
    )
    last_modified_by = models.IntegerField(blank=True, null=True)
    last_updated_by = models.IntegerField(blank=True, null=True)
