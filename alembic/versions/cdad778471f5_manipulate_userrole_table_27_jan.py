"""manipulate userrole table ,27 jan

Revision ID: cdad778471f5
Revises: 7065aa1dff80
Create Date: 2022-01-24 21:03:45.249834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cdad778471f5'
down_revision = '7065aa1dff80'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_role', sa.Column('role_name', sa.String(), nullable=True))
    op.create_index(op.f('ix_user_role_role_name'), 'user_role', ['role_name'], unique=False)
    op.drop_constraint('user_role_role_id_fkey', 'user_role', type_='foreignkey')
    op.drop_column('user_role', 'role_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_role', sa.Column('role_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('user_role_role_id_fkey', 'user_role', 'roles', ['role_id'], ['id'])
    op.drop_index(op.f('ix_user_role_role_name'), table_name='user_role')
    op.drop_column('user_role', 'role_name')
    # ### end Alembic commands ###
