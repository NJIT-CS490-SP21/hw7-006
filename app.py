import os
import datetime
from flask import Flask, render_template

app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

@app.route("/")
def index():
<<<<<<< HEAD
    return render_template("index.html",
    image='static/patrick1.jpg')
=======
    professor = "Professor Agrawal"
    t = datetime.datetime.now()
    date = "Today is "+ t.strftime("%A") + " " + t.strftime("%B") + " " + t.strftime("%d") + ", " + t.strftime("%Y")
    return render_template(
        "index.html",
        professor=professor,
        date = date,
    )
>>>>>>> 3c3bd4a4e02effae4112244a9ce036946ea78668

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug = False
)

