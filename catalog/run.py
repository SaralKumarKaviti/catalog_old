from flask import Flask,render_template

app=Flask(__name__)

@app.route('/wedding-invitation')
def index():
	return render_template('index.html')

@app.route('/about-us')
def aboutUs():
	return render_template('about-us.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')


if __name__=='__main__':
	app.run(debug=True)