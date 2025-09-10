from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        
        email=self.normalize_email(email)
        user=self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # some extra work for superuser registration and operation
    def create_superuser(self, email, password=None, **extra_fields):
        #handling two extra fields other than normal user

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("SuperUser must have is_staff=True")
        if not extra_fields.get('is_superuser'):
            raise ValueError("SuperUser must have is_superuser=True")
        
        return self.create_user(email, password, **extra_fields)

