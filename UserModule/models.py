from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not full_name:
            raise ValueError('User must provide his Full Name')

        user = self.model(
            email=self.normalize_email(email),
            full_name = full_name

        )

        user.set_password(password)
        user.is_active = False
        user.save(using=self._db)
        return user

    def create_staffuser(self, email,full_name, password = None):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            full_name,
            password=password,
        )
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email,full_name, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            full_name,
            password=password,
        )
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user




class User(AbstractBaseUser):
    email = models.EmailField(unique = True, max_length= 160)
    full_name = models.CharField(max_length = 160)
    is_active = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    is_admin = models.BooleanField(default = False)


    join_date = models.DateTimeField(auto_now_add = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()


    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.full_name.split(' ')[0]


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def staff(self):
        "Is the user a member of staff?"
        return self.is_staff

    @property
    def admin(self):
        "Is the user a admin member?"
        return self.is_admin

    @property
    def active(self):
        "Is the user active?"
        return self.is_active


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, blank = True, null = True)
    passout_year = models.IntegerField(null = True, blank = True)
    home_city = models.CharField(max_length = 120, null = True, blank = True)
    current_city = models.CharField(max_length = 120, null = True, blank = True)
    description = models.CharField(max_length = 120, null = True, blank = True)
    working = models.CharField(max_length = 120, null = True, blank = True)
    work_history = models.CharField(max_length = 120, null = True, blank = True)
    profile_pic = models.ImageField(default = 'profile1.png', null = True, blank = True)


    def __str__(self):
        return str(self.user)





