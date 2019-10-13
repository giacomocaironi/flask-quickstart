from app import app, db
from app.auth.models import User
from app import cli


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User}


if __name__ == "__main__":
    app.run(host="0.0.0.0")
