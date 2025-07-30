from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Lucas Stackhouse in 3308!'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://lab10_db_73dc_user:k8B4vhJZNyKhqGS0mwQZa7hHECiYNCkO@dpg-d24qcrfgi27c73baq5f0-a/lab10_db_73dc")
    conn.close()
    return "Database connection successful!"