"""revision

Revision ID: 91f222d37c31
Revises: 
Create Date: 2020-01-10 15:44:03.259516

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '91f222d37c31'
down_revision = None
branch_labels = None
depends_on = None




    # op.alter_column('seo_administrador','pass', new_column_name='password', nullable=True,existing_type=mysql.CHAR(length=255))
    # op.alter_column('seo_usuario','pass', new_column_name='password', nullable=True,existing_type=mysql.CHAR(length=255))

def upgrade():
    pass
def downgrade():
    pass