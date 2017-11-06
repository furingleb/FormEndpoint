"""empty message

Revision ID: 451467498fd0
Revises: efa58834f8e9
Create Date: 2017-11-05 21:25:04.659963

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '451467498fd0'
down_revision = 'efa58834f8e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('google_sheet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('credentials_json', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['destination.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_constraint('destination_user_id_fkey', 'destination', type_='foreignkey')
    op.drop_column('destination', 'user_id')
    op.drop_column('destination', 'credentials_json')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('destination', sa.Column('credentials_json', postgresql.JSONB(astext_type=sa.Text()), autoincrement=False, nullable=True))
    op.add_column('destination', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('destination_user_id_fkey', 'destination', 'user', ['user_id'], ['id'])
    op.drop_table('google_sheet')
    # ### end Alembic commands ###
