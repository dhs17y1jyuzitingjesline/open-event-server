"""empty message

Revision ID: 38f11aa39bff
Revises: 781e870940ac
Create Date: 2017-06-01 10:51:38.674997

"""

# revision identifiers, used by Alembic.
revision = '38f11aa39bff'
down_revision = '781e870940ac'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sponsors', 'logo', new_column_name='logo_url')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sponsors', 'logo_url', new_column_name='logo')
    # ### end Alembic commands ###
