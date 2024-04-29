from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///job.db'
db = SQLAlchemy(app)
class Form(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  position = db.Column(db.String(80), nullable=False)
  salary = db.Column(db.Integer, nullable=False)
  more = db.Column(db.String(10000), nullable=False)
  location = db.Column(db.String, nullable=False)

  def __repr__(self):
      return f'Form{self.position} '
app.app_context().push()

@app.route("/")
@app.route('/home')
def home_page():
    return render_template('home.html')
@app.route('/form')
def form_page():
    jobs = Form.query.all()
    return render_template('form.html', jobs=jobs)

@app.route('/about')
def about_page():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
