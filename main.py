from flask import Flask, render_template, request
from image import image_data

# create an instance of flask object
app = Flask(__name__)


# home page accessed with http://127.0.0.1:5000/
@app.route("/")
# map URL route for function below
def index():
    return render_template("index.html")


@app.route("/about/")
def about():
    return render_template("layouts/about.html")


@app.route("/christina/")
def christina():
    return render_template("team/christina.html")


@app.route("/rebecca/")
def rebecca():
    return render_template("team/rebecca.html")


@app.route("/ritvik/")
def ritvik():
    return render_template("team/ritvik.html")


@app.route("/william/")
def william():
    return render_template("team/william.html")


@app.route("/journal/")
def journal():
    return render_template("journals/journal.html")


@app.route("/pld/")
def project_layout():
    return render_template("journals/project_layout.html")


@app.route("/study_sheet/")
def study_sheet():
    return render_template("journals/study_sheet.html")

@app.route("/logicGates/")
def logicGates():
    return render_template("pbl/logicGates.html")


@app.route('/greetings/', methods=['GET', 'POST'])
def greetings():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:
            return render_template("pbl/greetings.html", name=name)
    return render_template("pbl/greetings.html", name="name")


@app.route("/all_labs/")
def all_labs():
    return render_template("all_labs.html")


@app.route("/binary/", methods=['GET', 'POST'])
def binary():
    BITS = 8
    imgBulbOn = "/static/assets/blub_on.gif"
    # second time you call it, its a post action
    if request.method == 'POST':
        BITS = int(request.form['BITS'])
        imgBulbOn = request.form['lightOn']
    return render_template("pbl/binary.html", imgBulbOn=imgBulbOn, BITS=BITS)


@app.route("/christinaBinary/", methods=['GET', 'POST'])
def christinaBinary():
    BITS = 8
    imgBulbOn = "/static/assets/pbl_ttt/binary_img/blub_on.gif"
    # second time you call it, its a post action - Christina Lee
    if request.method == 'POST':
        BITS = int(request.form['BITS'])
        imgBulbOn = request.form['lightOn']
    return render_template("pbl/christinaBinary.html", BITS=BITS, imgBulbOn=imgBulbOn)


@app.route("/brainwrite/")
def brainwrite():
    return render_template("brainwrite.html")


@app.route("/wireframes/")
def wireframes():
    return render_template("wireframes.html")


@app.route("/tpt3/")
def tpt3():
    return render_template("tpt3.html")


@app.route("/prototypes/")
def prototypes():
    return render_template("prototypes.html")


@app.route("/constellations/")
def constellations():
    return render_template("celestial objects/constellations.html")


@app.route("/comets/")
def comets():
    return render_template("celestial objects/comets.html")


@app.route("/planets/")
def planets():
    return render_template("celestial objects/planets.html")


@app.route("/galaxies/")
def galaxies():
    return render_template("celestial objects/galaxies.html")


@app.route("/blackholes/")
def blackholes():
    return render_template("celestial objects/blackholes.html")


@app.route("/nebulae/")
def nebulae():
    return render_template("celestial objects/nebulae.html")


@app.route("/binary_william/")
def binary_william():
    return render_template("pbl/binary_william.html")


@app.route("/binary_ritvik/")
def binary_ritvik():
    return render_template("pbl/binary_ritvik.html")


@app.route("/rgb/", methods=["GET", "POST"])
def RGB():
    return render_template("pbl/rgb.html", images=image_data())


@app.route("/RGBChristina/", methods=["GET", "POST"])
def RGBChristina():
    return render_template("pbl/christina_rgb.html", images=image_data())


@app.route("/rosetta/")
def rosetta():
    return render_template("celestial objects/rosetta.html")


@app.route("/halleys")
def halleys():
    return render_template("celestial objects/halleys.html")


@app.route("/hale_bopp")
def hale_bopp():
    return render_template("celestial objects/hale-bopp.html")

@app.route("/studySheet")
def studySheet():
    return render_template("journals/study_sheet.html")


# from image import hide_msg
# @app.route("/rgbhide")
# def hidemsg():
#    hide_msg()

if __name__ == "__main__":
    app.run(debug=True)
