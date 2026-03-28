import uuid
from sqlmodel import SQLModel, Field
from datetime import datetime, timezone
from typing import Optional
from uuid import UUID


class Auth(SQLModel, table=True):
    __tablename__ = "auth"
    __table_args__ = {"schema": "public"}

    user_id: Optional[UUID] = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        sa_column_kwargs={"server_default": "gen_random_uuid()"}
    )
    user_name: str = Field(index=True, unique=True)
    user_email: str = Field(index=True, unique=True)
    user_password: str
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc).replace(tzinfo=None)
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc).replace(tzinfo=None)
    )
