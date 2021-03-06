"""empty message

Revision ID: 73b73d64b9e7
Revises: deb39d8a3a18
Create Date: 2020-10-18 03:05:50.787822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73b73d64b9e7'
down_revision = 'deb39d8a3a18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('shows', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shows', sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
