from app import app
from flask_script import Manager


manager = Manager(app)


@manager.command
def runserver(port=9998):
    app.run(debug=True, port=int(port))

if __name__ == "__main__":
    manager.run()
