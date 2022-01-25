"""Added email token table ,28 jan

Revision ID: 11637492978b
Revises: bd5ffe8877fb
Create Date: 2022-01-25 03:55:23.592964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11637492978b'
down_revision = 'bd5ffe8877fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('email_token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('reset_code', sa.String(length=50), nullable=True),
    sa.Column('status', sa.String(length=1), nullable=True),
    sa.Column('expired_in', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_email_token_email'), 'email_token', ['email'], unique=False)
    op.create_index(op.f('ix_email_token_id'), 'email_token', ['id'], unique=False)
    op.create_index(op.f('ix_email_token_reset_code'), 'email_token', ['reset_code'], unique=False)
    op.create_index(op.f('ix_email_token_status'), 'email_token', ['status'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_email_token_status'), table_name='email_token')
    op.drop_index(op.f('ix_email_token_reset_code'), table_name='email_token')
    op.drop_index(op.f('ix_email_token_id'), table_name='email_token')
    op.drop_index(op.f('ix_email_token_email'), table_name='email_token')
    op.drop_table('email_token')
    # ### end Alembic commands ###