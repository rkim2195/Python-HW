from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)   
app.secret_key = "hi"
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/action", methods=['POST'])
def handle_form():
    session ['data'] = [request.form['user_name']
                        request.form['dojo_location']
                        request.form['fav_lang']
                        request.form['comment']]
    return redirect ("/result")

@app.route("/result")
def show_result():
#    print(session['data'])
    return render_template("result.html")

if __name__=="__main__":
    app.run(debug=True)