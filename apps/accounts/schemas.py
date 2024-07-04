from ninja import Schema
from typing import Optional


class UserSchema(Schema):
    """
    READ User schema
    """
    id: int
    username: str
    email: str
    bio: Optional[str] = None
    profile_picture: Optional[str] = None


class CreateUserSchema(Schema):
    """
    CREATE User schema
    """
    username: str
    password: str
    email: str
    bio: Optional[str] = None


class LoginSchema(Schema):
    """
    LOGIN User schema
    """
    username: str
    password: str


class UpdateUserSchema(Schema):
    """
    UPDATE User schema, specific field bio
    profile_picture is UploadedFile = File(None)
    """
    bio: Optional[str] = None

