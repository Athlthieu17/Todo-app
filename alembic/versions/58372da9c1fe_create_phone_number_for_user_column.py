"""Create phone number for user column

Revision ID: 58372da9c1fe
Revises: 
Create Date: 2023-10-04 21:51:25.967995

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '58372da9c1fe'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(),nullable= True))


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
