"""empty message

Revision ID: dde25ac8c50d
Revises: 657752aff6b3
Create Date: 2022-08-03 14:31:59.914152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dde25ac8c50d'
down_revision = '657752aff6b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artists', sa.Column('website_link', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artists', 'website_link')
    # ### end Alembic commands ###
