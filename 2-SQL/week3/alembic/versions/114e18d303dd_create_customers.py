"""create customers

Revision ID: 114e18d303dd
Revises: 
Create Date: 2022-05-10 19:14:27.230170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '114e18d303dd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        ADD COLUMN date_of_birth TIMESTAMP;
        )
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE customers 
        DROP COLUMN date_of_birth
        """
    )
