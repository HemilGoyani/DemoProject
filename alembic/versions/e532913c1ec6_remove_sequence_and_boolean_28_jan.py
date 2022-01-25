"""remove sequence and boolean ,28 jan

Revision ID: e532913c1ec6
Revises: 0466b36a9103
Create Date: 2022-01-25 04:20:26.366114

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e532913c1ec6'
down_revision = '0466b36a9103'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_email_token_status', table_name='email_token')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_email_token_status', 'email_token', ['status'], unique=False)
    # ### end Alembic commands ###
