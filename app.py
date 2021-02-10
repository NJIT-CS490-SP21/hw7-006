import os
import datetime
import random
from flask import Flask, render_template

Folder_Images = os.path.join('static', 'images')

app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.config['UPLOAD_FOLDER'] = Folder_Images

@app.route("/")
def index():
    professor = "Professor Agrawal"
    t = datetime.datetime.now()
    date = "Today is "+ t.strftime("%A") + " " + t.strftime("%B") + " " + t.strftime("%d") + ", " + t.strftime("%Y")
    number=random.randint(1,10)
    shows = ['Band of Brothers', 'The Pacific', 'Fullmetal Alchemist Brotherhood', 'My Hero Academia', 'The Mandalorian']
    Pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'band-of-brothers.jpg')
    Pic2 = os.path.join(app.config['UPLOAD_FOLDER'], 'pacific.jpg')
    Pic3 = os.path.join(app.config['UPLOAD_FOLDER'], 'Fullmetal.jpg')
    Pic4 = os.path.join(app.config['UPLOAD_FOLDER'], 'hero.jpg')
    Pic5 = os.path.join(app.config['UPLOAD_FOLDER'], 'Mandalorian.jpg')
    pics_list = [Pic1, Pic2, Pic3, Pic4, Pic5]

    return render_template(
        "index.html",
        professor=professor,
        date = date,
        my_shows_list = shows,
        my_pic_list = pics_list,
        number=number
    )

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug = False
)

