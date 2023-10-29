from flask import Flask, render_template, request, redirect, url_for, session,jsonify
import pymongo


app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this to a more secure secret key
client = pymongo.MongoClient("mongodb+srv://manishaarya4516:manish@login-register.zteavzx.mongodb.net/")
db = client.get_database("user_db")
users_collection = db.get_collection("users")



JOBS=[
    {
        'id':1,
        'title':'data analyst',
        'location':'Bengaluru , india',
        'salary':' Rs. 2,00000'
    },
    {
        'id':2,
        'title':'data engineer',
        'location':'hyderabad , india',
        'salary':' Rs. 2,00000'
    },
    {
        'id':3,
        'title':'machine learning',
        'location':'noida , india',
        'salary':' Rs. 5,00000'
    },
    {
        'id':4,
        'title':'ful stack',
        'location':'bengaluru , india',
        'salary':' Rs. 3,00000'
    },
    {
        'id':5,
        'title':'prompt enggg',
        'location':'pune , india',
        
    },
]

@app.route("/")
def root():
    return redirect(url_for('login'))  # Redirect to the login page when accessing the website

@app.route("/home")
def home():
    if 'username' in session:
        return render_template('home.html', jobs=JOBS)
    else:
        return redirect(url_for('login'))  # Redirect to the login page if not logged in

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = users_collection.find_one({"username": username, "password": password})

        if user:
            session['username'] = username
            return redirect(url_for('home'))  # Redirect to the home page after successful login
        else:
            return "Login failed. Please check your username and password."

    return render_template('login.html')

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if users_collection.find_one({"username": username}):
            return "This username is already taken. Please choose another."

        if password != confirm_password:
            return "Password and Confirm Password do not match. Please try again."

        users_collection.insert_one({"username": username, "email": email, "password": password})
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route("/api/jobs")
def job_list():
    return jsonify(JOBS )

if __name__ =="__main__":
    app.run(debug=True)