"""Adicionar o campo cobranca_uuid na tabela parcelas

Revision ID: 53314bafe11d
Revises: 55b8f0d469bf
Create Date: 2025-04-29 15:24:58.689082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53314bafe11d'
down_revision = '55b8f0d469bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tbl_parcelas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cobranca_uuid', sa.String(length=36), nullable=True))
        batch_op.create_index(batch_op.f('ix_tbl_parcelas_cobranca_uuid'), ['cobranca_uuid'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tbl_parcelas', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_tbl_parcelas_cobranca_uuid'))
        batch_op.drop_column('cobranca_uuid')

    # ### end Alembic commands ###
