from flask import Flask, render_template, request, url_for, redirect, session

app = Flask(__name__)
app.secret_key = 'bruh'

@app.route('/')
def index(): 
    return render_template("index.html")

@app.route('/process', methods =["GET", "POST"])
def result():
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comments"] = request.form["comments"]
    return redirect(url_for("display"))

@app.route("/display")
def display():
    return render_template("display.html")



if __name__=="__main__":
    app.run(debug=True)
