"""creating default user accountsRevision ID: 26889be04d70Revises: 33d84dc97ea1Create Date: 2014-09-10 00:08:49.335000"""# revision identifiers, used by Alembic.revision = '26889be04d70'down_revision = '51f3b3b5cd5d'from alembic import opimport sqlalchemy as safrom sqlalchemy.sql import table, columnfrom sqlalchemy import String, Integer, DateTime, Booleanimport datetimeusers = table(    'users',    column('id', Integer),    column('email', String),    column('active', Boolean),    column('confirmed_at', DateTime),)roles = table(    'roles',    column('id', Integer),    column('name', String),    column('description', String),)permissions = table(    'permissions',    column('id', Integer),    column('name', String),    column('description', String),)from adsws.accounts import create_appapp = create_app()email = app.config.get('BOOTSTRAP_USER_EMAIL', 'anon@ads')def upgrade():    op.bulk_insert(users, [        {            'email': email,            'active': True,            'confirmed_at': datetime.datetime.now()        },    ],        multiinsert=False    )def downgrade():    op.execute(        users.delete().where(users.c.email == op.inline_literal(email))    )          