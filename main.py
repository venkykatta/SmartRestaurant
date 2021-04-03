from flask import Flask, render_template, request, redirect, session, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors
 
app = Flask(__name__)

app.secret_key = "secret"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Shikhar@970'
app.config['MYSQL_DB'] = 'mysqldb'

mysql = MySQL(app)

@app.route("/")
def signup_page():
    return render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup_data():

    role = request.form["role"]
    if role == "manager":
            if request.method == "POST":
                user_data = request.form
                name = user_data['name']
                email = user_data['mail']
                password = user_data['password']
                role = user_data['role']
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO users(name, email, password, role) VALUES(%s, %s, %s, %s)", (name, email, password, role))
                mysql.connection.commit()
                cur.close()
                return render_template("manager.html")
    else:
        if request.method == "POST":
            user_data = request.form
            name = user_data['name']
            email = user_data['mail']
            password = user_data['password']
            role = user_data['role']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users(name, email, password, role) VALUES(%s, %s, %s, %s)", (name, email, password, role))
            mysql.connection.commit()
            cur.close()
            return render_template("chef.html")

@app.route("/login", methods=['POST', 'GET'])
def login_data():
    msg = ""
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form:
        name = request.form['name']
        password = request.form['password']
        role = request.form['role']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            "SELECT * FROM users WHERE name = % s AND password = % s AND role = %s",
            (
                name,
                password,
                role,
            ),
        )
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['name'] = account['name']
            msg = "logged in successfully!"
            if role == "manager":
                return render_template('manager.html', msg=msg)
            else:
                msg = "logged in successfully!"
                return render_template('chef.html', msg=msg)
        else:
            msg = 'Incorrect name and password!'
    return render_template("login.html", msg=msg)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('name', None)
    return redirect(url_for('login_data'))

if __name__ == "__main__":
    app.run(debug=True)