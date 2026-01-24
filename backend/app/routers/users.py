import uuid

from fastapi import APIRouter

from app.dependencies.auth import CurrentUserDep
from app.dependencies.user import UserServiceDep
from app.schemas.user import UserRead, UserUpdate


router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_model=list[UserRead])
async def get_users(user_service: UserServiceDep, current_user: CurrentUserDep):
    return await user_service.get_users()


@router.get("/me", response_model=UserRead)
def get_me(current_user: CurrentUserDep):
    return current_user


@router.get("/{user_id}", response_model=UserRead)
async def get_user(
    user_id: uuid.UUID, user_service: UserServiceDep, current_user: CurrentUserDep
):
    return await user_service.get_user(user_id)


@router.patch("/{user_id}", response_model=UserRead)
async def update_user(
    user_id: uuid.UUID,
    user_in: UserUpdate,
    user_service: UserServiceDep,
    current_user: CurrentUserDep,
):
    return await user_service.update_user(user_id, user_in)
