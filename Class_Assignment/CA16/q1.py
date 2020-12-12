from datetime import datetime
from flask import Flask, render_template, request, url_for
import random

q1 = Flask(__name__)

me = {
	"first_name": "Malak",
	"last_name": "Ghanom",
	"description": "The father of Computer Engineering.",
	"social_links": [
			{"site": "Twitter", "url": "https://twitter.com/someone"},
			{"site": "GitHub", "url": "https://github.com/someone"}
	],
	"age": 25,
	"avatarURL": "https://somewebsite.com/someusername/myprofile.jpg",
	"email": "you@email.com",
	"skills": ["Python", "Flask", "JavaScript", "HTML"],
	"projects": [
		{"name": "Tic-Tac-Toe", "description": "A description for the project.",
		    "tags": ["functions", "control structures", "game"]},
		{"name": "Battle of Teams", "description": "A description for the project.",
		    "tags": ["functions", "OOP"]},
		{"name": "Resume", "description": "A description for the project.",
		    "tags": ["flask", "web application", "HTTP routes"]}
	],
	"favourite_quotes": [
		{"quote": "Patience you must have my young Padawan.", "author": "Yoda"},
		{"quote": "The more a thing tends to be permanent, the more it tends to be lifeless.",
		    "author": "Alan Watts"},
		{"quote": "Logic will get you from A to Z; imagination will get you everywhere.",
		    "author": "Albert Einstein"}
	]
}


@q1.route('/')
def index():
	time = datetime.now()
	name = me.get('first_name') + " " + me.get('last_name')
	description = me.get('description')
	menu = [{'title': 'Me', 'url': url_for('personal_info')},
	{'title': 'Skills', 'url': url_for('skills')},
	{'title': 'Projects', 'url': url_for('projects')},
	{'title': 'Qoute of the Day', 'url': url_for('quote_of_the_day')}]

	return render_template('index.html',name = name, time = time, description=description,menu=menu)


@q1.route('/me')
def personal_info():
	me =	{
	"first_name": "Malak",
	"last_name": "Ghanom",
	"description": "The father of Computer Engineering.",
	"social_links": [
	{"site": "Twitter", "url": "https://twitter.com/someone"},
	{"site": "GitHub", "url": "https://github.com/someone"}
	],
	"age": 25,
	"avatarURL": "https://somewebsite.com/someusername/myprofile.jpg",
	"email": "you@email.com"}

	return render_template('me.html', me=me)

@q1.route('/skills')
def skills():
	return render_template('skills.html',me= me)
	

@q1.route('/projects')
def projects():
	return render_template('projects.html',me=me)


@q1.route('/quotes')
def quote_of_the_day():	
	return render_template('qoutes.html',quote=random.choice(me.get('favourite_quotes')))