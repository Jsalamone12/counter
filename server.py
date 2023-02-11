from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)  

app.secret_key = "safe"


@app.route('/')
def index():

    if "num" in session:
        session["num"] += 1
    else:
        session["num"] = 1

    if "num_two" in session:
        session["num_two"] += 1
    else:
        session["num_two"] = 1

    return render_template('index.html', num=session["num"])

@app.route('/remove_session')
def remove_session():
    session.clear()
    num = 0
    num_two = 0
    return redirect('/')

@app.route('/count', methods=["POST"])          
def count():
    session["num"] = session["num"]
    print(request.form)
    return redirect('/')

@app.route('/count_two', methods=["POST"])          
def count_two():
    session["num_two"] = session["num_two"]
    print(request.form)
    return redirect('/')


if __name__=="__main__":   
    app.run(debug=True)   

