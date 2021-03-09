from flask import Flask, render_template, request
from forms import ContactForm
import os


app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

data =[{
    'data':'2020 01 01',
    'autorius': 'Autorius 1',
    'pavadinimas': 'Apie nieką',
    'status': 'published',
    'tekstas': 'Zombie ipsum reversus ab viral inferno, nam rick grimes malum cerebro. De carne lumbering animata corpora quaeritis. Summus brains sit​​, morbo vel maleficia? De apocalypsi gorger omero undead survivor dictum mauris.'
},
{
    'data':'2020 02 01',
    'autorius': 'KITAS AUTORIUS',
    'pavadinimas': 'Apie zombius',
    'status': 'published',
    'tekstas': 'Zombie ipsum reversus ab viral inferno, nam rick grimes malum cerebro. De carne lumbering animata corpora quaeritis. Summus brains sit​​, morbo vel maleficia? De apocalypsi gorger omero undead survivor dictum mauris. '
},
{
    'data':'2020 03 01',
    'autorius': 'Dar kažkas',
    'pavadinimas': 'Braiiins!',
    'status': 'unpublished',
    'tekstas': 'Zombie ipsum reversus ab viral inferno, nam rick grimes malum cerebro. De carne lumbering animata corpora quaeritis. Summus brains sit​​, morbo vel maleficia? De apocalypsi gorger omero undead survivor dictum mauris.'
}]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        date = request.form['date']
        autorius = request.form['autorius']
        tekstas = request.form['tekstas']
        pavadinimas = request.form['pavadinimas']
        data.append({
            'data': date,
            'autorius': autorius,
            'pavadinimas': pavadinimas,
            'tekstas': tekstas,
            '`status`': 'published'
        })
    return render_template('index.html', data=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/add_article')
def add_article():
    return render_template('add_article.html')

@app.route('/<string:title>')
def article(title):
    return render_template('article.html', title=title, data=data)

@app.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
    form = ContactForm()
    if form.validate_on_submit():
        return render_template('contact_success.html', form=form)
    return render_template('contact_us.html', form=form)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
