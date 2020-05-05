from flask import Flask
from flask_migrate import MigrateCommand
from flask_script import Manager

from config.extensions import init_ext
from config.settings import init_app

app = Flask(__name__)

init_app(app)
init_ext(app)


manager=Manager(app)
manager.add_command('db', MigrateCommand)

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('defaultImg/favicon.ico')

if __name__ == '__main__':
    manager.run()
