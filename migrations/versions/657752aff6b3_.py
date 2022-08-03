"""empty message

Revision ID: 657752aff6b3
Revises: ac66fe91ba2c
Create Date: 2022-08-03 14:12:05.191384

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '657752aff6b3'
down_revision = 'ac66fe91ba2c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artists', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.add_column('artists', sa.Column('seeking_description', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artists', 'seeking_description')
    op.drop_column('artists', 'seeking_venue')
    # ### end Alembic commands ###
