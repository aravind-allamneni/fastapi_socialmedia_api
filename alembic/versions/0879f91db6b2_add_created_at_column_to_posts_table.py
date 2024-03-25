"""add created_at column to posts table

Revision ID: 0879f91db6b2
Revises: 83db733c0b7b
Create Date: 2024-03-25 19:26:55.319909

"""

from http import server
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0879f91db6b2"
down_revision: Union[str, None] = "83db733c0b7b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )


def downgrade() -> None:
    op.drop_column("posts", "created_at")
