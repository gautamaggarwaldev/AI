# Flask App Routing


from flask import Flask, render_template, request, redirect, url_for, jsonify

# create a simple flask application
app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return "<h1>Welcome to the Home Page</h1>"

@app.route('/index',methods=['GET'])
def index():
    return "<h2>Welcome to the Index Page</h2>"

# Variable Rule

@app.route('/success/<int:score>')
def success(score):
    return "The person is passed with score = " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person is failed with score = " + str(score)



@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        physics = float(request.form['physics'])
        maths = float(request.form['maths'])
        chemistry = float(request.form['chemistry'])

        average_marks = (physics + maths + chemistry) / 3

        res = ""
        if average_marks >= 50 :
            res = "success"
        else :
            res = "fail"
        
        return redirect(url_for(res, score = average_marks))

        # return render_template('form.html', score = average_marks)


@app.route('/api', methods=['POST'])
def calculate_sum():
    data = request.get_json()
    num1 = float(dict(data)['num1'])
    num2 = float(dict(data)['num2'])
    return jsonify(num1 + num2)


if __name__ == "__main__":
    app.run(debug=True)