"""empty message

Revision ID: 6063a9cac394
Revises: d81a57864cd6
Create Date: 2017-06-02 02:43:32.713980

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6063a9cac394'
down_revision = 'd81a57864cd6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('infobanjir_', sa.Column('date', sa.String(length=255), nullable=True))
    op.add_column('infobanjir_', sa.Column('time', sa.String(length=255), nullable=True))
    op.drop_column('infobanjir_', 'last_update')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('infobanjir_', sa.Column('last_update', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('infobanjir_', 'time')
    op.drop_column('infobanjir_', 'date')
    # ### end Alembic commands ###