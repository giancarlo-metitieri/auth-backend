"""Second Migration

Revision ID: 511b4b1dc0cf
Revises: 5569cdcc03a0
Create Date: 2025-01-12 23:07:41.090240

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '511b4b1dc0cf'
down_revision: Union[str, None] = '5569cdcc03a0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
