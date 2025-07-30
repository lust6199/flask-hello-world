from flask import Flask
import psycopg

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Lucas Stackhouse in 3308!'

@app.route('/db_test')
def db_test():
    conn = psycopg.connect("postgresql://lab10_db_73dc_user:k8B4vhJZNyKhqGS0mwQZa7hHECiYNCkO@dpg-d24qcrfgi27c73baq5f0-a/lab10_db_73dc")
    conn.close()
    return "Database connection successful!"

@app.route('/db_create')
def db_create():
    conn = psycopg.connect("postgresql://lab10_db_73dc_user:k8B4vhJZNyKhqGS0mwQZa7hHECiYNCkO@dpg-d24qcrfgi27c73baq5f0-a/lab10_db_73dc")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
        );
    ''')
    conn.commit()
    cur.close()
    conn.close()
    return "Basketball Table Created"