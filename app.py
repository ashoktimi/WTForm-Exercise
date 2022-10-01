from flask import Flask, render_template, flash, redirect, render_template, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///flask_wtforms"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def homepage():
    p = Pet.query.all()

    return render_template("index.html", pets=p)

@app.route('/hello')
def sayhello():
    return render_template("/hello.html")


@app.route("/add", methods=["GET", "POST"])
def addpage():
    form = PetForm()
 
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        url = form.photo_url.data
        age = form.age.data
        note = form.notes.data
        availability = form.available.data
        pet = Pet(name=name, species=species, photo_url=url, age=age, notes=note, available=availability)
        db.session.add(pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("add_pet.html", form=form)


@app.route("/pets/<int:id>/edit", methods=["GET", "POST"])
def edit_pet(id):
    pet = Pet.query.get(id)
    form = PetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect("/")
    else:
        return render_template("edit_pet_form.html", form=form, pet=pet)

# @app.route("/api/pets/<int:pet_id>", methods=['GET'])
# def api_get_pet(pet_id):
#     """Return basic info about pet in JSON."""

#     pet = Pet.query.get_or_404(pet_id)
#     info = {"name": pet.name, "age": pet.age}

#     return jsonify(info)



        
