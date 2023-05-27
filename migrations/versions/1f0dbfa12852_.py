"""empty message

Revision ID: 1f0dbfa12852
Revises: c4c27337e327
Create Date: 2023-01-14 19:58:25.207251

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f0dbfa12852'
down_revision = 'c4c27337e327'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'admin_member', ['id'])
    op.create_unique_constraint(None, 'admin_tag', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'admin_tag', type_='unique')
    op.drop_constraint(None, 'admin_member', type_='unique')
    # ### end Alembic commands ###
