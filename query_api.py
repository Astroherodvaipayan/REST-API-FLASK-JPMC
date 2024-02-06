from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Change the following values to match yours
db_name = "creditcard"
db_user = "postgres"
db_password ="qwerty"
db_host = "localhost"
db_port = "5432"

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(database=db_name, user=db_user, password=db_password,host=db_host, port=db_port)
cur = conn.cursor()

# Define a route that accepts POST requests to run SQL queries
@app.route("/query", methods=["GET"])
def query():
    query_text = request.args.get("query")
    cur.execute(query_text)
    result = cur.fetchall()

    # Return the result as JSON
    return jsonify(result)

# Run the Flask app on port 7000
if __name__ == "__main__":
    app.run(port=7000)
