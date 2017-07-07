from flask import Flask, session, request, render_template, redirect
from logins import reset_globals, add_user, check_user, users, get_name_user
import responses

app = Flask(__name__)
app.secret_key="iauhdiadg"


@app.route("/login", methods=["GET"])
def login():
    if 'logged_in' in session:
        return redirect("/home")
    return render_template('login.txt', login_url="/login", new_account_url="/createaccount", username_error=responses.WRONG_USERNAME, password_error=responses.WRONG_PASSWORD)

@app.route("/login", methods=["POST"])
def check_login():
    check_user(request.form['login'], request.form['pass'])
    if responses.OK:
        session['logged_in'] = True
        session['name'] = get_name_user(request.form['login'])
        return redirect("/home")
    return redirect("/login")

@app.route("/logout")
def logout():
    session.pop('logged_in')
    session.pop('name')
    reset_globals()
    return redirect("/login")

@app.route("/home")
def home():
    if 'logged_in' in session:
        return render_template('home.txt', name=session['name'], logout_url="/logout")
    return "oie, faz login primeiro ae", 401 


@app.route("/createaccount", methods=['GET'])
def ask_for_new_account_things():
    if 'logged_in' in session:
        return redirect("/home")
    print(responses.USERNAME_ALREADY_EXISTS)
    return render_template('new_account.txt', new_account_url="/createaccount", username_error=responses.USERNAME_ALREADY_EXISTS)

@app.route("/createaccount", methods=['POST'])
def create_account():
    print("oi")
    add_user(request.form['username'], request.form['password'], request.form['name'])
    if responses.USER_CREATED:
        session['logged_in'] = True
        session['name'] = request.form['name']
        return redirect("/home")
    else:
        print("deu ruim")
    return redirect("/createaccount")

@app.route("/")
def default():
    if 'logged_in' in session:
        return redirect("/home")
    else:
        return redirect("/login")

if __name__ == '__main__':
    app.run()
