"""empty message

Revision ID: d7b864ff73f1
Revises: 
Create Date: 2019-10-18 12:22:15.124847

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7b864ff73f1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Stores', sa.Column('address', sa.String(length=50), nullable=True))
    op.add_column('Stores', sa.Column('email', sa.String(length=50), nullable=True))
    op.add_column('Stores', sa.Column('number', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Stores', 'number')
    op.drop_column('Stores', 'email')
    op.drop_column('Stores', 'address')
    # ### end Alembic commands ###
