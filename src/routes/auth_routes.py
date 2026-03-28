from fastapi import APIRouter, Depends, HTTPException, Request, Body
from sqlalchemy.ext.asyncio import AsyncSession
from datalayer.database import get_db_session
from datalayer.model.dto import UserRegister, UserLogin
from services.auth_service import AuthService
from typing import List

router = APIRouter(tags=["Authentication"])

@router.post("/register")
async def register(
    user_data: UserRegister, 
    db: AsyncSession = Depends(get_db_session)
):
    try:
        service = AuthService(db)
        user = await service.register_user(user_data.model_dump())
        return {"message": "Registration successful", "user_id": user.user_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/users")
async def get_users(db: AsyncSession = Depends(get_db_session)):
    try:
        service = AuthService(db)
        users = await service.get_all_users()
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/login")
async def login(
    login_data: UserLogin, 
    db: AsyncSession = Depends(get_db_session)
):
    # Simple login placeholder logic
    return {"message": f"Login attempt for {login_data.username}"}
