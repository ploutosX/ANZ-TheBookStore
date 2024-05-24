"""books

Revision ID: 2024_05_24__22_59_59
Revises: 
Create Date: 2024-05-24 22:59:59.846026

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision: str = '2024_05_24__22_59_59'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'books',
        sa.Column('id', UUID, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('author', sa.String, nullable=False),
        sa.Column('year', sa.Integer, nullable=False),
        sa.Column('category', sa.String, nullable=False),
        sa.Column('theme', sa.String, nullable=False),
        sa.Column('version', sa.String, nullable=False),
        sa.Column('genre', sa.String),
        sa.Column('price', sa.Integer),
        sa.Column('discount', sa.Float),
        sa.Column('stock', sa.Integer),
        sa.Column('description', sa.String),
        sa.Column('image', sa.String),
        sa.Column('active', sa.Boolean, nullable=False),
        sa.UniqueConstraint('name', 'author', 'year', 'category',
                            'theme', 'version', name='unique_book')
    )


def downgrade() -> None:
    pass
