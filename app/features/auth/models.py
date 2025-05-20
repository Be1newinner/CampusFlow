from sqlalchemy import Enum
from sqlalchemy.orm import MappedColumn, Mapped
from app.db.base_class import Base
from datetime import datetime

from app.features.auth.schemas import UserRole

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = MappedColumn(primary_key=True, index=True)
    username: Mapped[str] = MappedColumn(unique=True, index=True)
    email: Mapped[str] = MappedColumn(unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = MappedColumn(nullable=False)
    is_active: Mapped[bool] = MappedColumn(nullable=False, default=True)
    role: Mapped[UserRole] = MappedColumn(Enum(UserRole, name="user_role_enum" ), nullable=False, default=UserRole.STUDENT)
    is_verified: Mapped[bool] = MappedColumn(nullable=False, default=False)
    is_deleted: Mapped[bool] = MappedColumn(nullable=False, default=False)
    created_at: Mapped[datetime] = MappedColumn(default=datetime.now())
    updated_at: Mapped[datetime] = MappedColumn(
        default=datetime.now(), onupdate=datetime.now()
    )
    deleted_at: Mapped[datetime] = MappedColumn(nullable=True, default=None)
    last_login: Mapped[datetime] = MappedColumn(nullable=True, default=None)