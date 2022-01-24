"""manipulate field in role tables ,27 jan

Revision ID: ebbfd33ee937
Revises: 7460b03bf1b8
Create Date: 2022-01-24 19:08:02.152741

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ebbfd33ee937'
down_revision = '7460b03bf1b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('name', sa.String(), nullable=True))
    op.create_index(op.f('ix_roles_name'), 'roles', ['name'], unique=True)
    op.drop_column('roles', 'role')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('role', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_roles_name'), table_name='roles')
    op.drop_column('roles', 'name')
    # ### end Alembic commands ###