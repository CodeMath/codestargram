from ninja import Router, File, Form
from ninja.files import UploadedFile
from ninja.errors import HttpError

from ninja_jwt.authentication import JWTAuth
from ninja_jwt.tokens import RefreshToken


from apps.base_schemas import Error
from apps.accounts.services import UserService
from apps.accounts.schemas import *

router = Router()

user_service = UserService()


@router.post("/signup", response={201: UserSchema, 401: Error})
def signup(request, data: CreateUserSchema):
    """
    Create a new user
    """
    user = user_service.create_user(**data.dict())
    return 201, user


@router.post("/signin")
def signin(request, data: LoginSchema):
    """
    Signin a user
    """
    user = user_service.authenticate_user(data.username, data.password)
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@router.put("/update-profile", response={200: UserSchema, 401: Error}, auth=JWTAuth())
def update_profile(request, bio: Optional[str] = Form(None), profile_picture: Optional[UploadedFile] = File(None)):
    if not request.auth:
        raise HttpError(401, "Unauthorized")
    print(f"bio: {bio}, profile_picture: {profile_picture}")
    user = user_service.update_user(request.auth.id, bio=bio, profile_picture=profile_picture)
    return user
