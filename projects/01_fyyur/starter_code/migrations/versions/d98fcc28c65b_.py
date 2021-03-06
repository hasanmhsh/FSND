"""empty message

Revision ID: d98fcc28c65b
Revises: 9a9eedb27f0d
Create Date: 2020-10-15 18:25:44.622628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd98fcc28c65b'
down_revision = '9a9eedb27f0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('website', sa.String(length=120), nullable=True))
    op.add_column('Venue', sa.Column('seeking_description', sa.String(length=120), nullable=True))
    op.add_column('Venue', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    op.add_column('shows', sa.Column('datetimestamp_frontend', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('shows', 'datetimestamp_frontend')
    op.drop_column('Venue', 'seeking_talent')
    op.drop_column('Venue', 'seeking_description')
    op.drop_column('Artist', 'website')
    # ### end Alembic commands ###
