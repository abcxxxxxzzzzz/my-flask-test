"""empty message

Revision ID: eb6282c85528
Revises: b752ce55cd13
Create Date: 2023-01-24 12:58:41.115581

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb6282c85528'
down_revision = 'b752ce55cd13'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin_title',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='用户ID'),
    sa.Column('url', sa.String(length=255), nullable=True, comment='网址'),
    sa.Column('title', sa.String(length=255), nullable=True, comment='标题'),
    sa.Column('tag', sa.String(length=255), nullable=True, comment='标签'),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='更新时间'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('url')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('admin_title')
    # ### end Alembic commands ###
