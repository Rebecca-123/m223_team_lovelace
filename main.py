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


@app.route("/rebecca/", methods=["GET", "POST"])
def rebecca():
    # submit button pushed
    if request.form:
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        # store submission in name variable
        # if not empty string
        if num1 != "" or num2 != "":
            # for arithmetic round answer to ten thousandths place
            if request.form["action"] == "Add numbers!":
                num = float(num1) + float(num2)
                return render_template("team/rebecca.html", num=round(num, 4))
            elif request.form["action"] == "Subtract numbers!":
                num = float(num1) - float(num2)
                return render_template("team/rebecca.html", num=round(num, 4))
            # for multiplication and division round answer to 8 places after decimal point
            elif request.form["action"] == "Multiply numbers!":
                num = float(num1) * float(num2)
                return render_template("team/rebecca.html", num=round(num, 8))
            elif request.form["action"] == "Divide numbers!":
                num = float(num1) / float(num2)
                return render_template("team/rebecca.html", num=round(num, 8))
    # tell user to input numbers if they haven't
    return render_template("team/rebecca.html", num="Input numbers to sum!")


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


@app.route("/logic_gates/")
def logic_gates():
    return render_template("pbl/logic_gates.html")


@app.route("/unsigned_addition/")
def unsigned_addition():
    BITS = 8
    imgBulbOn = "/static/assets/blub_on.gif"
    # second time you call it, its a post action
    if request.method == 'POST':
        BITS = int(request.form['BITS'])
        imgBulbOn = request.form['lightOn']
    return render_template("pbl/unsigned_addition.html", imgBulbOn=imgBulbOn, BITS=BITS)


@app.route("/color_code/")
def color_code():
    return render_template("pbl/color_code.html")


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


@app.route("/signed_addition/")
def signed_addition():
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

@app.route("/mantras/")
def mantras():
    return render_template("mantras.html")


@app.route('/joke', methods=['GET', 'POST'])
def joke():
    """
    # use this url to test on and make modification on you own machine
    url = "http://127.0.0.1:5222/api/joke"
    """
    url = "https://csp.nighthawkcodingsociety.com/api/joke"
    response = requests.request("GET", url)
    return render_template("starter/joke.html", joke=response.json())


@app.route('/jokes', methods=['GET', 'POST'])
def jokes():
    """
    # use this url to test on and make modification on you own machine
    url = "http://127.0.0.1:5222/api/jokes"
    """
    url = "https://csp.nighthawkcodingsociety.com/api/jokes"

    response = requests.request("GET", url)
    return render_template("starter/jokes.html", jokes=response.json())


@app.route('/covid19', methods=['GET', 'POST'])
def covid19():
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
    headers = {
        'x-rapidapi-key': "dec069b877msh0d9d0827664078cp1a18fajsn2afac35ae063",
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)


    return render_template("starter/covid19.html", stats=response.json())

@app.route('/variable_ritvik')
def variable_ritvik():
    return render_template("individual_videos/variable_ritvik.html")

# from image import hide_msg
# @app.route("/rgbhide")
# def hidemsg():
#    hide_msg()

if __name__ == "__main__":
    app.run(debug=True)
