from flask import Flask,render_template, jsonify
from flask import request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)

db = client.school
students = db.students

@app.route("/")
def hello_world():
    return render_template("index.html", temp="Varun")

@app.route("/odd_even_function", methods=["POST"])
def function_handler():
    # step 1 - getting the value from frontend to backend
    input_param = request.form["input_param"]

    try:
        input_param = int(input_param)
    except:
        return render_template("index.html", response={"odd_even":None, "message":"Input is not a number"})

    # step 2 - process
    response_var = "Odd" if input_param%2==1 else "Even"

    # step 3 - respond back to the frontend
    return render_template("index.html", response={"odd_even":response_var, "message":"Success"})

@app.route("/check_odd_even", methods=['POST'])
def check_odd_even():
    input = request.get_json()
    number = input['number']
    if number & 1 == 0:
        return jsonify({'result': 'Even'})
    else:
        return jsonify({'result': 'Odd'})

@app.route("/students", methods=['POST'])   # Create
def create():
    input = request.get_json()
    students.insert_one(input)
    return jsonify({"success": True})

@app.route("/students", methods=['GET'])   # Read
def read():
    data = list(students.find())
    for i in range(len(data)):
        del data[i]['_id']
    print(data)
    return jsonify({"data": data})

@app.route("/students", methods=['PUT'])   # Update
def update():
    return jsonify({"success": True})

@app.route("/students", methods=['DELETE'])   # Delete
def delete():
    return jsonify({"success": True})

if __name__ == ('__main__'):
    app.run(debug=True)