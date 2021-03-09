from flask import Flask, render_template

app = Flask(__name__)

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

@app.route('/')
def index():
    return render_template('index.html', data=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/<string:title>') # parametruose nurodomas kintamasis (title) ir jo tipas (string)
def article(title): # kintamąjį būtinai nurodykite ir funkcijos parametruose
    return render_template('article.html', title=title, data=data) # taip pat ir čia reikia jį perduoti

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
