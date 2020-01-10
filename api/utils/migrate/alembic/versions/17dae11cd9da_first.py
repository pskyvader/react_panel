"""first

Revision ID: 17dae11cd9da
Revises: 
Create Date: 2020-01-09 18:53:13.974504

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '17dae11cd9da'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    pass


    # op.alter_column('seo_administrador','pass', new_column_name='password', nullable=True)
    # op.alter_column('seo_usuario','pass', new_column_name='password', nullable=True)