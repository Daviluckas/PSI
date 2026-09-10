from flask import Flask, render_template
from blueprints.home.routes import home_bp
from blueprints.users.routes import users_bp
from blueprints.login.routes import login_bp
from config import SECRET_KEY


app = Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(users_bp)
app.register_blueprint(login_bp)
app.config['SECRET_KEY'] = SECRET_KEY

if __name__ == '__main__':
  app.run(debug=True)

