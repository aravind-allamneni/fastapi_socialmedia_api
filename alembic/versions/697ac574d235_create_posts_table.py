"""create posts table

Revision ID: 697ac574d235
Revises: 
Create Date: 2024-03-25 07:47:03.115188

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "697ac574d235"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("content", sa.String()),
    )


def downgrade() -> None:
    op.drop_table("posts")
