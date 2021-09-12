from flask import Flask, render_template, request

# create an instance of flask object
app = Flask(__name__)


# home page accessed with http://127.0.0.1:5000/
@app.route("/")
# map URL route for function below
def index():
    return render_template("index.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/christina/")
def christina():
    return render_template("/team/christina.html")


@app.route("/rebecca/")
def rebecca():
    return render_template("/team/rebecca.html")


@app.route("/ritvik/")
def ritvik():
    return render_template("/team/ritvik.html")


@app.route("/william/")
def william():
    return render_template("/team/william.html")


@app.route("/journal/")
def journal():
    return render_template("journal.html")


@app.route('/greetings/', methods=['GET', 'POST'])
def greetings():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:
            return render_template("greetings.html", name=name)
    return render_template("greetings.html", name="name")


@app.route("/all_labs/")
def all_labs():
    return render_template("all_labs.html")


@app.route("/binary/", methods = ['GET', 'POST'])
def binary():
    BITS = 8
    imgBulbOn = "/static/assets/blub_on.gif"
    # second time you call it, its a post action
    if request.method == 'POST':
        BITS = int(request.form['BITS'])
        imgBulbOn = request.form['lightOn']
    return render_template("binary.html", imgBulbOn = imgBulbOn, BITS=BITS)


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


if __name__ == "__main__":
    app.run(debug=True)
