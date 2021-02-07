from flask import Flask, render_template, request, redirect

app = Flask(__name__ )

@app.route('/')
def signup_page():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def manager_page():
    
    role = request.form['role']
    if role == "manager":
        return render_template('manager.html')
    else:
        return render_template('chef.html')
            
if __name__ == "__main__":
    app.run(debug=True)