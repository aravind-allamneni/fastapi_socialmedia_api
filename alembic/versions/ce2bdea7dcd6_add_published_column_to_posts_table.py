"""add published column to posts table

Revision ID: ce2bdea7dcd6
Revises: 697ac574d235
Create Date: 2024-03-25 08:06:14.494414

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ce2bdea7dcd6"
down_revision: Union[str, None] = "697ac574d235"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "posts",
        sa.Column(
            "published", sa.Boolean(), nullable=False, server_default=sa.text("TRUE")
        ),
    )


def downgrade() -> None:
    op.drop_column("posts", "published")
