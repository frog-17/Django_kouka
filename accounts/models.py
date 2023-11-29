from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


class UserManager(BaseUserManager):

    def create_user(self, username, email, gender, birthday, password):
        user = self.model(
            username = username,
            email = email,
            gender = gender,
            birthday = birthday
        )
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, gender, birthday, password):
        user = self.model(
            username = username,
            email = email,
            gender = gender,
            birthday = birthday
        )
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    # 使いたいFieldを追加
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    gender = models.CharField(max_length=10)
    birthday = models.DateField(max_length=8)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email' # ☆2 このテーブルのレコードを一意に識別
    REQUIRED_FIELDS = ['username', 'gender', 'birthday'] # スーパーユーザ作成時に入力する

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email
