from flask import Flask, render_template
from blueprints.home.routes import home_bp
from blueprints.users.routes import users_bp

app = Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(users_bp)

if __name__ == '__main__':
  app.run(debug=True)

