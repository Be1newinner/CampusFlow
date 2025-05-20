import asyncio
import os
from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.ext.asyncio import create_async_engine
from alembic import context
from dotenv import load_dotenv

from app.db.base_class import Base

# 1. Load environment variables and alembic config
load_dotenv()
config = context.config
if config.config_file_name:
    fileConfig(config.config_file_name)

# 2. Set DB URL
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL not set in environment!")

config.set_main_option("sqlalchemy.url", DATABASE_URL)

# 3. Metadata for autogenerate support
target_metadata = Base.metadata

# 4. Define synchronous migration logic to run in sync context
def do_run_migrations(connection):
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        # You can add other options here like compare_type=True if needed
    )
    with context.begin_transaction():
        context.run_migrations()

# 5. Offline migrations - generate SQL scripts without DB connection
def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# 6. Online migrations - run using async DB engine & connection
async def run_migrations_online():
    connectable = create_async_engine(DATABASE_URL, poolclass=pool.NullPool)

    async with connectable.connect() as connection:
        # Run synchronous migration logic inside async connection
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()

# 7. Entrypoint to decide offline vs online mode
if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
