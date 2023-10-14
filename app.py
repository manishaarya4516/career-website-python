from flask import Flask , render_template , jsonify
app=Flask(__name__)

JOBS=[
    {
        'id':1,
        'title':'data analyst',
        'location':'bengaluru , india',
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
def hello():
    return render_template('home.html',jobs=JOBS)

@app.route("/api/jobs")
def job_list():
    return jsonify(JOBS )

if __name__ =="__main__":
    app.run(debug=True)