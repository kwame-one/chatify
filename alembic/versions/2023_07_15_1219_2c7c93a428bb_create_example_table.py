"""create example table

Revision ID: 2c7c93a428bb
Revises: 
Create Date: 2023-07-15 12:19:32.318367

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import func, text

revision = '2c7c93a428bb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'examples',
        sa.Column('id', sa.String(36), primary_key=True, nullable=False),
        sa.Column('test', sa.String(191), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=func.now(), nullable=True),
        sa.Column('updated_at', sa.DateTime, server_default=func.now(), onupdate=func.now(),
                  nullable=True),
        sa.Column('deleted_at', sa.DateTime, nullable=True)
    )


def downgrade() -> None:
    op.drop_table('examples')
