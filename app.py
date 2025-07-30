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

@app.route('/db_select')
def db_select():
    conn = psycopg.connect("postgresql://lab10_db_73dc_user:k8B4vhJZNyKhqGS0mwQZa7hHECiYNCkO@dpg-d24qcrfgi27c73baq5f0-a/lab10_db_73dc")
    cur = conn.cursor()
    cur.execute('SELECT * FROM Basketball;')
    records = cur.fetchall()

    response = """
    <table border='1'>
        <tr>
            <th>First</th>
            <th>Last</th>
            <th>City</th>
            <th>Name</th>
            <th>Number</th>
        </tr>
    """

    for record in records:
        response += "<tr>"
        for value in record:
            response += f"<td>{value}</td>"
        response += "</tr>"
    response += "</table>"
    cur.close()
    conn.close()
    return response

@app.route('/db_drop')
def db_drop():
    conn = psycopg.connect("postgresql://lab10_db_73dc_user:k8B4vhJZNyKhqGS0mwQZa7hHECiYNCkO@dpg-d24qcrfgi27c73baq5f0-a/lab10_db_73dc")
    cur = conn.cursor()
    cur.execute('DROP TABLE Basketball;')
    conn.commit()
    cur.close()
    conn.close()
    return "Basketball Table Dropped"