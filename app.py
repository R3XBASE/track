from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import requests

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Konfigurasi PostgreSQL
DB_HOST = "your_host"
DB_NAME = "your_database"
DB_USER = "your_username"
DB_PASS = "your_password"

def connect_db():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    ip = request.remote_addr
    korupsi_input = request.form['korupsi_input']
    
    # Simpan ke database
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO korban (ip, korupsi_input) VALUES (%s, %s)", (ip, korupsi_input))
    conn.commit()
    conn.close()
    
    # Redirect ke halaman sukses
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
