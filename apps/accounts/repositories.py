from ninja.files import UploadedFile
from apps.accounts.models import User
from typing import Optional


class UserRepository:
    """
    User repository class
    """

    def create_user(self, username: str, password: str, email: str, **extra_fields) -> User:
        user = User.objects.create_user(username=username, password=password, email=email, **extra_fields)
        return user

    def get_user(self, user_id: int) -> User:
        return User.objects.get(id=user_id)

    def get_user_by_username(self, username: str) -> User:
        return User.objects.get(username=username)

    def update_user(self, user_id: int, bio: Optional[str] = None, profile_picture: Optional[UploadedFile] = None):
        user = User.objects.get(id=user_id)
        if bio is not None:
            user.bio = bio
        if profile_picture is not None:
            user.profile_picture.save(profile_picture.name, profile_picture, save=True)
        user.save()
        return user
