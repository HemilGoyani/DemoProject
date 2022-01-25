"""delete super admin table ,28 jan

Revision ID: bd5ffe8877fb
Revises: 15d4072bef48
Create Date: 2022-01-25 02:08:11.212929

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd5ffe8877fb'
down_revision = '15d4072bef48'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_super_admin_address', table_name='super_admin')
    op.drop_index('ix_super_admin_email', table_name='super_admin')
    op.drop_index('ix_super_admin_id', table_name='super_admin')
    op.drop_index('ix_super_admin_name', table_name='super_admin')
    op.drop_index('ix_super_admin_password', table_name='super_admin')
    op.drop_table('super_admin')
    op.add_column('users', sa.Column('isAdmin', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'isAdmin')
    op.create_table('super_admin',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('address', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='super_admin_pkey')
    )
    op.create_index('ix_super_admin_password', 'super_admin', ['password'], unique=False)
    op.create_index('ix_super_admin_name', 'super_admin', ['name'], unique=False)
    op.create_index('ix_super_admin_id', 'super_admin', ['id'], unique=False)
    op.create_index('ix_super_admin_email', 'super_admin', ['email'], unique=False)
    op.create_index('ix_super_admin_address', 'super_admin', ['address'], unique=False)
    # ### end Alembic commands ###