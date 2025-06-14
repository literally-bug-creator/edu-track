"""Initial commit

Revision ID: 85130c6b679b
Revises: 
Create Date: 2025-03-14 01:48:23.604962

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '85130c6b679b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('units',
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_units_id'), 'units', ['id'], unique=False)
    op.create_table('tracks',
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('unit_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['unit_id'], ['units.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tracks_id'), 'tracks', ['id'], unique=False)
    op.create_table('disciplines',
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('track_id', sa.Integer(), nullable=False),
    sa.Column('course_number', sa.Enum('FIRST', 'SECOND', 'THIRD', 'FOURTH', 'FIFTH', name='coursenumber'), nullable=False),
    sa.Column('semester_number', sa.Enum('FIRST', 'SECOND', name='semesternumber'), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['track_id'], ['tracks.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_disciplines_id'), 'disciplines', ['id'], unique=False)
    op.create_table('groups',
    sa.Column('number', sa.String(length=255), nullable=False),
    sa.Column('track_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['track_id'], ['tracks.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_groups_id'), 'groups', ['id'], unique=False)
    op.create_table('disciplines_groups',
    sa.Column('discipline_id', sa.Integer(), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['discipline_id'], ['disciplines.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('discipline_id', 'group_id')
    )
    op.create_table('users',
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.LargeBinary(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('middle_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('role', sa.Enum('ADMIN', 'TEACHER', 'STUDENT', name='userrole'), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_group_id'), 'users', ['group_id'], unique=False)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_role'), 'users', ['role'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    op.create_index('username_index', 'users', ['username'], unique=False, postgresql_using='hash')
    op.create_table('disciplines_teachers',
    sa.Column('discipline_id', sa.Integer(), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['discipline_id'], ['disciplines.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['teacher_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('discipline_id', 'teacher_id')
    )
    op.create_table('marks',
    sa.Column('discipline_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('work_type', sa.Enum('HOMEWORK', 'PRACTICAL_WORK', 'LABORATORY_WORK', 'VERIFICATION_WORK', 'COURSE_WORK', name='worktype'), nullable=False),
    sa.Column('type', sa.Enum('ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', name='marktype'), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['discipline_id'], ['disciplines.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['student_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_marks_id'), 'marks', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_marks_id'), table_name='marks')
    op.drop_table('marks')
    op.drop_table('disciplines_teachers')
    op.drop_index('username_index', table_name='users', postgresql_using='hash')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_role'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_group_id'), table_name='users')
    op.drop_table('users')
    op.drop_table('disciplines_groups')
    op.drop_index(op.f('ix_groups_id'), table_name='groups')
    op.drop_table('groups')
    op.drop_index(op.f('ix_disciplines_id'), table_name='disciplines')
    op.drop_table('disciplines')
    op.drop_index(op.f('ix_tracks_id'), table_name='tracks')
    op.drop_table('tracks')
    op.drop_index(op.f('ix_units_id'), table_name='units')
    op.drop_table('units')
    # ### end Alembic commands ###
