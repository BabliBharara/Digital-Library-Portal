from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# ✅ MySQL Configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="devi@1611#",  # your MySQL password
    database="examhacker"
)
cursor = db.cursor(dictionary=True)

# ✅ Default route: Show login first
@app.route('/')
def index():
    return redirect(url_for('login'))

# ✅ Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        query = "SELECT * FROM users WHERE username=%s AND password=%s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        if user:
            flash('Login successful!', 'success')
            return redirect(url_for('work'))
        else:
            flash('Invalid username or password.', 'error')
            return redirect(url_for('login'))
    else:
        return render_template('login.html')

# ✅ Signup Page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            flash('Username already exists. Choose a different one.', 'error')
            return redirect(url_for('signup'))

        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')

# ✅ Work/Dashboard Page
@app.route('/work')
def work():
    return render_template('work.html')

# ✅ Course Routes
@app.route('/bca')
def bca():
    return render_template('bca.html')

@app.route('/btech')
def btech():
    return render_template('btech.html')

@app.route('/bba')
def bba():
    return render_template('bba.html')

@app.route('/bphrma')
def bphrma():
    return render_template('bphrma.html')

# ✅ BCA SEM 1 Content
@app.route('/bca/sem1')
def bcacontent():
    return render_template('bcacontent.html')
@app.route('/bba/sem1')
def bba1sem():
    return render_template('bba1sem.html')
@app.route('/bpharma/sem1')
def bpharm1sem():
    return render_template('bpharm1sem.html')
@app.route('/bpharma/sem2')
def bpharm2sem():
    return render_template('bpharm2sem.html')
@app.route('/btech/sem1')
def btechsem1():
    return render_template('btechsem1.html')
@app.route('/btech/sem2')
def btechsem2():
    return render_template('btechsem2.html')

if __name__ == '__main__':
    app.run(debug=True)

