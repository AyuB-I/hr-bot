"""Deleted 4 one-to-many tables and added new columns to forms and created new enum types for them

Revision ID: 08a5c06cd9b6
Revises: 
Create Date: 2022-09-07 13:54:12.640448

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08a5c06cd9b6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('departments',
    sa.Column('department_id', sa.SMALLINT(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), nullable=False),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.Column('photo_id', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('department_id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('forms',
    sa.Column('form_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('full_name', sa.VARCHAR(length=255), nullable=False),
    sa.Column('birth_date', sa.DATE(), nullable=False),
    sa.Column('phonenum', sa.VARCHAR(length=20), nullable=False),
    sa.Column('address', sa.VARCHAR(length=255), nullable=False),
    sa.Column('living_conditions', sa.Enum('FLAT', 'HOUSE', name='livingconditionsenum'), nullable=False),
    sa.Column('education', sa.Enum('SECONDARY', 'SECONDARY_SPECIAL', 'BACHELOR', 'MASTER', name='educationsenum'), nullable=False),
    sa.Column('marital_status', sa.BOOLEAN(), nullable=False),
    sa.Column('business_trip', sa.BOOLEAN(), nullable=False),
    sa.Column('military_service', sa.BOOLEAN(), nullable=False),
    sa.Column('criminal_record', sa.TEXT(), nullable=False),
    sa.Column('driver_license', sa.VARCHAR(length=10), nullable=False),
    sa.Column('personal_car', sa.VARCHAR(length=64), nullable=False),
    sa.Column('origin', sa.Enum('FAMILIAR', 'TELEGRAM', 'INSTAGRAM', 'FACEBOOK', 'OTHER', name='originsenum'), nullable=False),
    sa.Column('salary_last_job', sa.VARCHAR(length=255), nullable=False),
    sa.Column('overwork_agreement', sa.BOOLEAN(), nullable=False),
    sa.Column('force_majeure_salary_agreement', sa.BOOLEAN(), nullable=False),
    sa.Column('working_style', sa.Enum('COLLECTIVE', 'INDIVIDUAL', name='workingstylesenum'), nullable=False),
    sa.Column('health', sa.VARCHAR(length=255), nullable=False),
    sa.Column('photo_id', sa.TEXT(), nullable=False),
    sa.Column('registered_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('form_id')
    )
    op.create_table('applications',
    sa.Column('application_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('form_id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=32), nullable=False),
    sa.Column('level', sa.SMALLINT(), nullable=False),
    sa.ForeignKeyConstraint(['form_id'], ['forms.form_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('application_id')
    )
    op.create_table('forms_departments',
    sa.Column('form_id', sa.INTEGER(), nullable=False),
    sa.Column('department_id', sa.SMALLINT(), nullable=False),
    sa.ForeignKeyConstraint(['department_id'], ['departments.department_id'], ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['form_id'], ['forms.form_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('form_id', 'department_id')
    )
    op.create_table('languages',
    sa.Column('language_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('form_id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=32), nullable=False),
    sa.Column('level', sa.SMALLINT(), nullable=False),
    sa.ForeignKeyConstraint(['form_id'], ['forms.form_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('language_id')
    )
    op.create_table('self_assessment',
    sa.Column('assessment_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('form_id', sa.INTEGER(), nullable=False),
    sa.Column('type', sa.VARCHAR(length=32), nullable=False),
    sa.Column('text', sa.TEXT(), nullable=False),
    sa.ForeignKeyConstraint(['form_id'], ['forms.form_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('assessment_id')
    )
    op.create_table('trips',
    sa.Column('trip_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('form_id', sa.INTEGER(), nullable=False),
    sa.Column('country', sa.VARCHAR(length=255), nullable=False),
    sa.Column('reason', sa.VARCHAR(length=255), nullable=False),
    sa.Column('traveled_at', sa.DATE(), nullable=False),
    sa.ForeignKeyConstraint(['form_id'], ['forms.form_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('trip_id')
    )
    op.create_table('universities',
    sa.Column('university_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('form_id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), nullable=False),
    sa.Column('faculty', sa.VARCHAR(length=255), nullable=False),
    sa.Column('finished_at', sa.SMALLINT(), nullable=False),
    sa.ForeignKeyConstraint(['form_id'], ['forms.form_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('university_id', 'form_id')
    )
    op.create_table('users',
    sa.Column('telegram_id', sa.BIGINT(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=255), nullable=True),
    sa.Column('telegram_name', sa.VARCHAR(length=255), nullable=False),
    sa.Column('form_id', sa.INTEGER(), nullable=True),
    sa.Column('is_employee', sa.BOOLEAN(), server_default='FALSE', nullable=True),
    sa.Column('registered_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['form_id'], ['forms.form_id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('telegram_id'),
    sa.UniqueConstraint('form_id')
    )
    op.create_table('worked_companies',
    sa.Column('company_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('form_id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), nullable=False),
    sa.Column('position', sa.VARCHAR(length=255), nullable=False),
    sa.Column('started_at', sa.DATE(), nullable=False),
    sa.Column('finished_at', sa.DATE(), nullable=True),
    sa.ForeignKeyConstraint(['form_id'], ['forms.form_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('company_id')
    )
    op.create_table('appreciations',
    sa.Column('appreciation_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.BIGINT(), nullable=False),
    sa.Column('sender_id', sa.BIGINT(), nullable=False),
    sa.Column('text', sa.TEXT(), nullable=True),
    sa.Column('sent_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['sender_id'], ['users.telegram_id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['user_id'], ['users.telegram_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('appreciation_id')
    )
    op.create_table('bonuses',
    sa.Column('bonus_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.BIGINT(), nullable=False),
    sa.Column('assigner_id', sa.BIGINT(), nullable=False),
    sa.Column('amount', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), nullable=False),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['assigner_id'], ['users.telegram_id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['user_id'], ['users.telegram_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('bonus_id')
    )
    op.create_table('complaints',
    sa.Column('complaint_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.BIGINT(), nullable=False),
    sa.Column('sender_id', sa.BIGINT(), nullable=False),
    sa.Column('text', sa.TEXT(), nullable=True),
    sa.Column('sent_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['sender_id'], ['users.telegram_id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['user_id'], ['users.telegram_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('complaint_id')
    )
    op.create_table('fines',
    sa.Column('fine_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.BIGINT(), nullable=False),
    sa.Column('assigner_id', sa.BIGINT(), nullable=False),
    sa.Column('amount', sa.INTEGER(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('given_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['assigner_id'], ['users.telegram_id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['user_id'], ['users.telegram_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('fine_id')
    )
    op.create_table('salaries',
    sa.Column('salary_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.BIGINT(), nullable=False),
    sa.Column('assigner_id', sa.BIGINT(), nullable=False),
    sa.Column('amount', sa.INTEGER(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('given_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['assigner_id'], ['users.telegram_id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['user_id'], ['users.telegram_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('salary_id')
    )
    op.create_table('tasks',
    sa.Column('task_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.BIGINT(), nullable=False),
    sa.Column('assigner_id', sa.BIGINT(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), nullable=False),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.Column('status', sa.VARCHAR(length=32), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('finished_at', sa.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['assigner_id'], ['users.telegram_id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['user_id'], ['users.telegram_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('task_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tasks')
    op.drop_table('salaries')
    op.drop_table('fines')
    op.drop_table('complaints')
    op.drop_table('bonuses')
    op.drop_table('appreciations')
    op.drop_table('worked_companies')
    op.drop_table('users')
    op.drop_table('universities')
    op.drop_table('trips')
    op.drop_table('self_assessment')
    op.drop_table('languages')
    op.drop_table('forms_departments')
    op.drop_table('applications')
    op.drop_table('forms')
    op.drop_table('departments')

    op.execute('drop type livingconditionsenum;')
    op.execute('drop type educationsenum;')
    op.execute('drop type originsenum;')
    op.execute('drop type workingstylesenum;')
    # ### end Alembic commands ###