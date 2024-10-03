from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

API_KEY = "036eb3435b6bcfcf84b05bb0e23be739"

SEARCH_URL= "https://api.themoviedb.org/3/search/movie"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

##CREATE DB
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


##CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

class UpdateForm(FlaskForm):
    nrating = StringField("Your Rating Out of 10" ,validators=[DataRequired()])
    nreview = StringField("Your Review" ,validators=[DataRequired()])
    done = SubmitField("Done")

class AddForm(FlaskForm):
    title = StringField("MOvie Title" ,validators=[DataRequired()])
    add = SubmitField("Add")

@app.route("/")
def home():
    result = db.session.execute(db.select(Movie))
    all_movies = result.scalars().all()
    return render_template("index.html", movies=all_movies)

@app.route('/edit/<int:id>' , methods = ["GET","POST"])
def update(id):
    form = UpdateForm()
    movie = Movie.query.get_or_404(id)
    if request.method == "POST":
        if form.validate_on_submit():
            movie.rating = request.form.get("nrating")
            movie.review = request.form.get("nreview")
            db.session.commit()
            print("updated\n")
            return redirect(url_for('home'))
    return render_template("edit.html" , form=form)

@app.route('/delete')
def delete():
    movie = request.args.get('id')
    db.session.delete(movie)
    db.session.commit()
    return    redirect(url_for('home'))

@app.route('/add', methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(SEARCH_URL,  params={"api_key": API_KEY , "query" : movie_title })
        data = response.json()["results"]
        db.session.add(data)
        return  redirect(url_for('select.html', options = data))
    return  render_template("add.html")


if __name__ == '__main__':
    app.run(debug=True)