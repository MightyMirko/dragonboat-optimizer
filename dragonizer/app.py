from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

# Formularklasse erstellen
class PassengerForm(FlaskForm):
    passenger1 = StringField('Passenger 1', validators=[DataRequired()])
    passenger2 = StringField('Passenger 2', validators=[DataRequired()])
    # Füge weitere Felder für die Passagierdaten hinzu

# Routen definieren
@app.route('/', methods=['GET', 'POST'])
def index():
    form = PassengerForm()
    seating_arrangement = None

    if form.validate_on_submit():
        # Verarbeite die eingegebenen Passagierdaten und generiere das Sitzarrangement
        passenger1 = form.passenger1.data
        passenger2 = form.passenger2.data
        # Verarbeite weitere eingegebene Felder für die Passagierdaten

        # Hier kannst du deine Logik für die Generierung des Sitzarrangements einfügen
        seating_arrangement = generate_seating_arrangement(passenger1, passenger2)  # Funktion zum Generieren des Sitzarrangements

    return render_template('index.html', form=form, seating_arrangement=seating_arrangement)

# Beispiel-Funktion zur Generierung des Sitzarrangements
def generate_seating_arrangement(passenger1, passenger2):
    # Hier deine Logik zum Generieren des Sitzarrangements einfügen
    seating_arrangement = ['Row 1: {} and {}'.format(passenger1, passenger2)]

    return seating_arrangement

if __name__ == '__main__':
    app.run()
