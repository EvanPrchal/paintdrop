"""2nd

Revision ID: 3c699207ec29
Revises: 9af8725264a4
Create Date: 2025-09-15 11:51:15.296136

"""
from typing import Sequence

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '3c699207ec29'
down_revision: str | Sequence[str] | None = '9af8725264a4'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
