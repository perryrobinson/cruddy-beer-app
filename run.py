# run.py

from app import app
from db_setup import init_db, db_session
from flask import flash, render_template, request, redirect, url_for, session
from models import Brewery, Beer
from forms import BreweryForm, BeerForm

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route("/view_all_beers")
def view_all_beers():
    beer_qry = db_session.query(Beer).order_by(Beer.type)

    return render_template('view_all_beers.html', data=beer_qry)

@app.route('/add_beer', methods=['GET', 'POST'])
def add_beer():
    '''
    Add and save a beer to the database
    '''

    # need to pass the brewery dropdown data to the template, because this
    # information can change overtime as users add new breweries to the db
    brewery_dropdown_data = []
    qry = Brewery.query.order_by(Brewery.name)
    for brewery in qry:
        brewery_dropdown_data.append(brewery.name)

    form = BeerForm()
    if form.validate_on_submit():
        # this section is used to find the correct brewery_id for the selected
        # brewery, this is then passed to the beer object to be saved in the db
        selected_brewery = request.form.get("brewery", None)
        existing_breweries = Brewery.query.order_by(Brewery.name)
        for brewery in existing_breweries:
            if selected_brewery == brewery.name:
                brewery_id = brewery.id

        beer = Beer(name=form.name.data,
                    type=form.type.data,
                    abv=form.abv.data,
                    brewery_id=brewery_id)

        # save beer to database
        db_session.add(beer)
        db_session.commit()
        flash('You have successfully added a beer!')

        #redirect to view_all_beers
        return redirect(url_for('view_all_beers'))

    return render_template('add_beer.html', form=form, brewery_dropdown_data=brewery_dropdown_data)

@app.route('/view_all_beers/delete/<int:id>', methods=['GET', 'POST'])
def delete_beer(id):
    '''
    Delete a beer from the database
    '''
    beer = Beer.query.get_or_404(id)
    current_db_session = db_session.object_session(beer)
    current_db_session.delete(beer)
    current_db_session.commit()
    flash('You have successfully deleted the role.')

    return redirect(url_for('view_all_beers'))

@app.route('/add_brewery', methods=['GET', 'POST'])
def add_brewery():
    '''
    Add and save a brewery to the database
    '''
    form = BreweryForm()

    if form.validate_on_submit():

        brewery = Brewery(name=form.name.data,
                    city=form.city.data,
                    state=form.state.data)

        # save brewery to database
        db_session.add(brewery)
        db_session.commit()
        flash('You have successfully added a brewery!')

        #redirect to view_all_beers
        return redirect(url_for('view_all_beers'))

    return render_template('add_brewery.html', form=form)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
