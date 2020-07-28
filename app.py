from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet, default_img
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def show_pets():
    """Show homepage"""
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Route that both shows the form to add a new pet and that adds a new pet"""
    form = AddPetForm()

    if form.validate_on_submit():
        form_data = form.data
        form_data.pop('csrf_token', None)
        form_data = form_data

        new_pet = Pet(**form_data)

        if not new_pet.photo_url:
            new_pet.photo_url = None

        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added new pet: {new_pet.name}!")
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)

@app.route('/<int:pet_id>', methods=["GET", "POST"])
def display_edit_pet(pet_id):
    """Route that displays pet's information, shows a form to edit the pet, and edits the pet"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        pic = form.photo_url.data
        # This line doesn't work here for some reason.  Still trying to figure this out.  Even though pic gets set to None if
        # the photo_url is an empty string, it still doesn't get set to the default_img value.  I have to set it manually below
        # in the else: block
        # pic = pic if pic else None

        if pic:
            pet.photo_url = pic
        else:
            pet.photo_url = default_img

        pet.name = form.name.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        flash(f"Successfully edited {pet.name}!")
        return redirect(f'/{pet.id}')
    else:
        return render_template('display-edit.html', form=form, pet=pet)