# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
import os

PEOPLE_FOLDER = os.path.join('static', 'Images')
# create the application object
app = Flask(__name__)

# @app.route('/_get_ajax_data/')
# def get_ajax_data():
#     data = {"hello": "world"}
#     response = jsonify(data)
#     response.cache_control.max_age = 60 * 60 * 24  # 1 day (in seconds)
#     return response

app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

# use decorators to link the function to a url
@app.route('/')
def welcome():
	full_filenameLogo = os.path.join(app.config['UPLOAD_FOLDER'],'HeaderLogo.png')
	burglarBars = os.path.join(app.config['UPLOAD_FOLDER'],'burglarBars.png')
	fredLee = os.path.join(app.config['UPLOAD_FOLDER'],'fredlee.jpg')
	return render_template('welcome.html', logo_image = full_filenameLogo, fredLee = fredLee, burglarBars = burglarBars) # render a template

@app.route('/about')
def about():
	full_filenameLogo = os.path.join(app.config['UPLOAD_FOLDER'],'HeaderLogo.png')
	burglarBars = os.path.join(app.config['UPLOAD_FOLDER'],'burglarBars.png')
	return render_template('about.html', logo_image = full_filenameLogo, burglarBars = burglarBars)

@app.route('/GrantInfo')
def GrantInfo():
	full_filenameLogo = os.path.join(app.config['UPLOAD_FOLDER'],'HeaderLogo.png')
	burglarBars = os.path.join(app.config['UPLOAD_FOLDER'],'burglarBars.png')
	GrantPolicy = os.path.join(app.config['UPLOAD_FOLDER'],'GrantMakingPolicyV5.pdf')
	return render_template('GrantInfo.html', logo_image = full_filenameLogo, burglarBars = burglarBars, GrantPolicy = GrantPolicy)

@app.route('/programs')
def programs():
	full_filenameLogo = os.path.join(app.config['UPLOAD_FOLDER'],'HeaderLogo.png')
	burglarBars = os.path.join(app.config['UPLOAD_FOLDER'],'burglarBars.png')
	return render_template('programs.html', logo_image = full_filenameLogo, burglarBars = burglarBars)

@app.route('/contact')
def contact():
	full_filenameLogo = os.path.join(app.config['UPLOAD_FOLDER'],'HeaderLogo.png')
	burglarBars = os.path.join(app.config['UPLOAD_FOLDER'],'burglarBars.png')
	return render_template('contact.html', logo_image = full_filenameLogo, burglarBars = burglarBars)

@app.route('/PF990')
def PF990():
	full_filenameLogo = os.path.join(app.config['UPLOAD_FOLDER'],'HeaderLogo.png')
	burglarBars = os.path.join(app.config['UPLOAD_FOLDER'],'burglarBars.png')
	pdf990_2017 = os.path.join(app.config['UPLOAD_FOLDER'],'2017_990.pdf')
	pdf990_2016 = os.path.join(app.config['UPLOAD_FOLDER'],'2016_990.pdf')
	return render_template('PF990.html', logo_image = full_filenameLogo, burglarBars = burglarBars, pdf990_2017 = pdf990_2017, pdf990_2016 = pdf990_2016)

@app.route('/members')
def members():
	full_filenameLogo = os.path.join(app.config['UPLOAD_FOLDER'],'HeaderLogo.png')
	burglarBars = os.path.join(app.config['UPLOAD_FOLDER'],'burglarBars.png')
	return render_template('members.html', logo_image = full_filenameLogo, burglarBars = burglarBars)

# start the server with the 'run()' method
if __name__ == '__main__':
	app.run(debug=True)


