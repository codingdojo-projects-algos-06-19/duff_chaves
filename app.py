from config import app, db
from server.routes import users, dashboard

if __name__ == "__main__":
    app.run(debug=True)