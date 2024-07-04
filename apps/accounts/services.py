from apps.accounts.repositories import UserRepository
from django.contrib.auth import authenticate

from ninja.errors import HttpError
from ninja.files import UploadedFile

from typing import Optional


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, username: str, password: str, email: str, **extra_fields):
        return self.user_repository.create_user(username, password, email, **extra_fields)

    def authenticate_user(self, username: str, password: str):
        user = authenticate(username=username, password=password)
        if user is None:
            raise HttpError(401, "Invalid credentials")
        return user

    def update_user(self, user_id: int, bio: Optional[str] = None, profile_picture: Optional[UploadedFile] = None):
        return self.user_repository.update_user(user_id, bio, profile_picture)