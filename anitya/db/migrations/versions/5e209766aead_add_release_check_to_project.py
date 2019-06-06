"""Add release check to project

Revision ID: 5e209766aead
Revises: e34988f3e2f4
Create Date: 2019-06-06 14:53:06.236820
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5e209766aead"
down_revision = "e34988f3e2f4"


def upgrade():
    """ Add releases_only column to the projects table. """
    op.add_column(
        "projects",
        sa.Column(
            "releases_only",
            sa.Boolean(),
            default=False,
            server_default="FALSE",
            nullable=False,
        ),
    )


def downgrade():
    """ Drop releases_only column to the projects table. """
    op.drop_column("projects", "releases_only")
