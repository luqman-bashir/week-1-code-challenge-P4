"""Initial migration.

Revision ID: 34b7a3490822
Revises: 1a8c9dc95068
Create Date: 2025-01-30 21:52:19.953335

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34b7a3490822'
down_revision = '1a8c9dc95068'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('course', schema=None) as batch_op:
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('course', schema=None) as batch_op:
     batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), nullable=False, server_default='0'))

    # ### end Alembic commands ###
