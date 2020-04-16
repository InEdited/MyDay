from flask import Flask , request, render_template
import flask, flask_login, os
from flask_login import  LoginManager, current_user, login_user, logout_user, login_required, UserMixin
import DBUtil as db
from flask_sqlalchemy import SQLAlchemy

dirPath = os.path.abspath(os.path.dirname(__file__))
dbPath = os.path.join(dirPath, 'Database/main.db')

app = Flask(__name__)
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = "login"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + dbPath
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = "eraseme"

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))
        

@login_manager.user_loader
def load_user(user_id):
    if User.query.get(int(user_id)):
        print(User.query.get(int(user_id)))
        return User.query.get(int(user_id))
    else:
        return None

@app.route("/")
def home():
    print(current_user.is_anonymous)
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/Login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['email-address']
        password = request.form['password']     
        print(username)   
        login = User.query.filter_by(username=username, password=password).first()
        if login is not None:
            login_user(username)
            return flask.redirect(flask.url_for("home"))
        else:
            return flask.abort(401)
    else:
        return render_template('login.html')
    

@app.route("/Register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form['username']
        mail = request.form['email-address']
        passw = request.form['password']

        register = User(username = uname, email = mail, password = passw)
        db.session.add(register)
        db.session.commit()

        return flask.redirect(flask.url_for("login"))
    return render_template('register.html')

@app.route("/catalog/<name>")
def catalog(name):    
    return render_template('catalog.html')

@app.route("/sub_catalogs/<name>")
def subcatalog(name):
    # women_fashions
    stuff = db.get_sub_catalogs(name)
    return render_template('sub_catalogs.html', things = stuff)

@app.route("/sub_catalogs/services/<name>")
def services(name):
    stuff = db.get_services(name)
    return render_template('services.html', things = stuff)


@app.route("/debug")
def debug():
    db.get_services("Shops")

@app.route("/todo")
@login_required

def todo():
    return render_template('todo.html')

@app.route("/Logout")
def logout():
    logout_user()
    return flask.redirect(flask.url_for("home"))

@app.errorhandler(401)
def page_not_found(e):
    return flask.Response('<p>Login failed</p>')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=4000,use_reloader=True)

