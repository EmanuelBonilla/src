# Diego Emanuel Bonilla Soler
# 12/06/2023

from flask import Flask , render_template


app = Flask(__name__)

#Routes from web site

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/shop')
def shop():
	return render_template('shop.html')

@app.route('/about')
def about():
	return render_template('about.html')


if __name__ == '__main__':
	app.run(debug=True)

