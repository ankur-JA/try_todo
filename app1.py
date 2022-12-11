from flask import Flask,render_template
from flask import request

app = Flask(__name__)

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

if __name__ == ('__main__'):
    app.run(debug=True)