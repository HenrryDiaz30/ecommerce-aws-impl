from flask import Flask, jsonify
import pymysql
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Plataforma e-commerce desplegada en AWS ECS",
        "status": "ok"
    })

@app.route("/db")
def db_check():
    try:
        connection = pymysql.connect(
            host=os.environ.get("DB_HOST"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
            database=os.environ.get("DB_NAME", "mysql"),
            port=int(os.environ.get("DB_PORT", "3306"))
        )

        cursor = connection.cursor()
        cursor.execute("SELECT NOW()")
        result = cursor.fetchone()
        connection.close()

        return jsonify({
            "database_time": str(result[0]),
            "db_status": "connected"
        })

    except Exception as e:
        return jsonify({
            "error": str(e),
            "db_status": "failed"
        })