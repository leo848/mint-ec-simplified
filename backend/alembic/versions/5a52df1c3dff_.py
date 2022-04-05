"""empty message

Revision ID: 5a52df1c3dff
Revises: 8cd6aad9f019
Create Date: 2022-04-05 17:59:46.831728

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a52df1c3dff'
down_revision = '8cd6aad9f019'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('tags', 'name', new_column_name='title')


def downgrade():
    op.alter_column('tags', 'title', new_column_name='name')
