from flask import Flask
import psycopg2

app = Flask(__name__)

DB_HOST = "db"
DB_NAME = "myapp"
DB_USER = "appuser"
DB_PASS = "password123"

def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

@app.route("/")
def home():
    return "<h1>Hello DevOps!</h1>"

@app.route("/init")
def init_db():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS mahasiswa(
            id SERIAL PRIMARY KEY,
            nama VARCHAR(100)
        );
    """)

    cur.execute("""
        INSERT INTO mahasiswa(nama)
        VALUES('Ridwan');
    """)

    conn.commit()

    cur.close()
    conn.close()

    return "Database berhasil dibuat."

@app.route("/data")
def data():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM mahasiswa")

    rows = cur.fetchall()

    cur.close()
    conn.close()

    hasil = ""

    for row in rows:
        hasil += f"{row}<br>"

    return hasil

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
