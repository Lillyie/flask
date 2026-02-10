from  flask import Flask, request, render_template, jsonify
from models.user import User
from schema import db
from flask_login import LoginManager
# from flask_migrate import Migrate

app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    
    if username and password:
        #login
        return jsonify({"message": "autenticado"})

    return jsonify({"message": "Credenciais inválidas"}), 400
@app.route("/")
def homepage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)