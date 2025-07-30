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

@app.route('/db_insert')
def db_insert():
    conn = psycopg.connect("postgresql://lab10_db_73dc_user:k8B4vhJZNyKhqGS0mwQZa7hHECiYNCkO@dpg-d24qcrfgi27c73baq5f0-a/lab10_db_73dc")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        VALUES
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2),
        ('Lucas', 'Stackhouse', 'CU Boulder', 'Buffs', 3308);
    ''')
    conn.commit()
    cur.close()
    conn.close()
    return "Basketball Table Populated"