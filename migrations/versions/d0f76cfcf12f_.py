"""empty message

Revision ID: d0f76cfcf12f
Revises: a7bd64045be6
Create Date: 2019-06-28 22:25:46.036607

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0f76cfcf12f'
down_revision = 'a7bd64045be6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users_cart_items',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'item_id')
    )
    op.drop_table('users_kart_items')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users_kart_items',
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('item_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'item_id')
    )
    op.drop_table('users_cart_items')
    # ### end Alembic commands ###