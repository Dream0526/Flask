#!/usr/bin/env python3
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db
from app.models.user_model import FontUser
from app.models.file_model import InstanceFile, VirtualFile


app = create_app('default')
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
