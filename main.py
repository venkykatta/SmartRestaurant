from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
 
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Shikhar@970'
app.config['MYSQL_DB'] = 'mysqldb'

mysql = MySQL(app)

@app.route("/")
def signup_page():
    return render_template("signup.html")


@app.route("/signup", methods=["POST"])
def manager_page():

    role = request.form["role"]
    if role == "manager":
            if request.method == "POST":
                user_data = request.form
                Name = user_data['name']
                email = user_data['mail']
                Password = user_data['password']
                Role = user_data['role']
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO SignUp(Name, email, Password, Role) VALUES(%s, %s, %s, %s)", (Name, email, Password, Role))
                mysql.connection.commit()
                cur.close()
                return render_template("manager.html")
    else:
        if request.method == "POST":
            user_data = request.form
            Name = user_data['name']
            email = user_data['mail']
            Password = user_data['password']
            Role = user_data['role']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO SignUp(Name, email, Password, Role) VALUES(%s, %s, %s, %s)", (Name, email, Password, Role))
            mysql.connection.commit()
            cur.close()
            return render_template("chef.html")


if __name__ == "__main__":
    app.run(debug=True)