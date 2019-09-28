"""empty message

Revision ID: 9e2001cfae6f
Revises: 
Create Date: 2019-09-09 20:26:24.963797

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e2001cfae6f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tests',
    sa.Column('is_active', sa.Boolean(), server_default='1', nullable=False),
    sa.Column('is_deleted', sa.Boolean(), server_default='0', nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('example_enum', sa.Enum('Enum1', 'Enum2', 'Enum3', name='enum'), server_default='Enum1', nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contains',
    sa.Column('is_active', sa.Boolean(), server_default='1', nullable=False),
    sa.Column('is_deleted', sa.Boolean(), server_default='0', nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('testing_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['testing_id'], ['tests.id'], onupdate='CASCADE', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contains')
    op.drop_table('tests')
    # ### end Alembic commands ###
