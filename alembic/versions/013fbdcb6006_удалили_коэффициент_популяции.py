"""удалили коэффициент популяции

Revision ID: 013fbdcb6006
Revises: 61ee9260bf2b
Create Date: 2021-04-20 16:34:08.118519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '013fbdcb6006'
down_revision = '61ee9260bf2b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recipes', 'coeff_popular')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipes', sa.Column('coeff_popular', sa.INTEGER(), server_default=sa.text('0'), nullable=True))
    # ### end Alembic commands ###
