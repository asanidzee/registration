from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='temp1')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register.html', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/home.html')
def homee():
    return render_template('home.html')

if __name__ == '_main_':
    app.run(debug=True)