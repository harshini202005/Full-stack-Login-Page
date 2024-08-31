from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

# Route to render the form
@app.route('/')
def index():
    return render_template('login.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def login():
    if request.method == 'POST':
        # Get data from the form
        email = request.form['email']
        password = request.form['password']
        print(email)
        print(password)
        
        # Connect to PostgreSQL database
        conn = psycopg2.connect(
            host='localhost',
            database='practical',
            user='postgres',
            password='1234'
        )
        cur = conn.cursor()
        
        # Insert data into the database
        cur.execute('insert into login_info (email, password) VALUES (%s, %s)', (email, password))
        
        # Commit changes and close connection
        conn.commit()
        cur.close()
        conn.close()
        
        return 'Data submitted successfully'

if __name__ == '__main__':
    app.run(debug=True)
