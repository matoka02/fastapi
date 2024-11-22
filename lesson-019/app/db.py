import os
from typing import AsyncGenerator
from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
)
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from dotenv import load_dotenv

from .user_models import Base, User, AccessToken


current_script_path = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(current_script_path, '..', 'database.env')

load_dotenv(dotenv_path)

HOST_PG = os.getenv('POSTGRES_HOST')
PORT_PG = os.getenv('POSTGRES_PORT')
DATABASE_PG = os.getenv('POSTGRES_DB')
USER_PG = os.getenv('POSTGRES_USER')
PASSWORD_PG = os.getenv('POSTGRES_PASSWORD')

DATABASE_URL = f"postgresql+asyncpg://{USER_PG}:{PASSWORD_PG}@{HOST_PG}:{PORT_PG}/{DATABASE_PG}"

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)


async def get_access_token_db(
    session: AsyncSession = Depends(get_async_session),
):
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)