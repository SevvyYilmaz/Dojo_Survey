from flask import Flask,render_template, request, redirect, session
app = Flask(__name__)
app.secret_key="Shhh, this is a secret"

@app.route('/')
def root():
    return render_template("index.html")

# cannot render on a Post method redirect instead to a diff url and render the new html there 
@app.route('/process', methods= ['POST'])
def process_form():
    session['user_information'] = request.form
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['favorite_language'] = request.form['favorite_language']
    session['comments'] = request.form ['comments']
    return redirect('/show/user')

@app.route('/show/user')
def show_user():
    return render_template("show_user.html")

if __name__ == "__main__":
    app.run(debug=True)
