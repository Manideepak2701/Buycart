from flask import*
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/navbar')
def navbar():
    return render_template('homepage.html')

@app.route('/home')
def home():
    return render_template('contact.html')

@app.route('/login')
def loginpage():
    return render_template('loginpage.html')

@app.route('/register')
def registerpage():
    return render_template('register.html')


@app.route('/contactus')
def contentdetails():
    return render_template('contactus.html')

@app.route('/l',methods=['POST'])
def login():
    uname = request.form['uname']
    passwrd = request.form['pass']
    if uname == "deepak" and passwrd == "12345":
        return render_template("homepage.html")
    else:
        return "<h1>wrong username or password</h1>"

@app.route('/women')
def womendresses():
    return render_template('women.html')

@app.route('/children')
def children():
    return render_template('children.html')


@app.route('/cart')
def cart():
    return render_template('cart.html')


if __name__ == "__main__":
    app.run()