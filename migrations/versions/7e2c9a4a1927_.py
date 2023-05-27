"""empty message

Revision ID: 7e2c9a4a1927
Revises: cf25d0d22ad5
Create Date: 2023-01-18 19:14:20.748671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e2c9a4a1927'
down_revision = 'cf25d0d22ad5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('name', table_name='admin_handicap')
    op.create_index(op.f('ix_admin_handicap_name'), 'admin_handicap', ['name'], unique=True)
    op.create_index(op.f('ix_admin_member_bank'), 'admin_member', ['bank'], unique=False)
    op.create_index(op.f('ix_admin_member_details'), 'admin_member', ['details'], unique=False)
    op.create_index(op.f('ix_admin_member_iphone'), 'admin_member', ['iphone'], unique=False)
    op.create_index(op.f('ix_admin_member_realname'), 'admin_member', ['realname'], unique=False)
    op.create_index(op.f('ix_admin_member_username'), 'admin_member', ['username'], unique=False)
    op.create_index(op.f('ix_admin_tag_name'), 'admin_tag', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_admin_tag_name'), table_name='admin_tag')
    op.drop_index(op.f('ix_admin_member_username'), table_name='admin_member')
    op.drop_index(op.f('ix_admin_member_realname'), table_name='admin_member')
    op.drop_index(op.f('ix_admin_member_iphone'), table_name='admin_member')
    op.drop_index(op.f('ix_admin_member_details'), table_name='admin_member')
    op.drop_index(op.f('ix_admin_member_bank'), table_name='admin_member')
    op.drop_index(op.f('ix_admin_handicap_name'), table_name='admin_handicap')
    op.create_index('name', 'admin_handicap', ['name'], unique=False)
    # ### end Alembic commands ###
