"""empty message

Revision ID: 81e78fdad2ed
Revises: b54b31013604
Create Date: 2018-07-27 22:07:23.058630

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '81e78fdad2ed'
down_revision = 'b54b31013604'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('refund_policy', sa.String(), nullable=True))
    op.add_column('events_version', sa.Column('refund_policy', sa.String(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
    events_table = sa.sql.table('events', sa.Column('refund_policy', sa.String()))
    op.execute(events_table.update()
               .where(events_table.c.refund_policy.is_(None))
               .values({'refund_policy': 'All sales are final. No refunds shall be issued in any case.'}))


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events_version', 'refund_policy')
    op.drop_column('events', 'refund_policy')
    # ### end Alembic commands ###