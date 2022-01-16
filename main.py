from flask import Flask, render_template, request, redirect, url_for
import json
from replit import db
from bs4 import BeautifulSoup as bs
import os
import re
import logging

site = Flask(__name__)


@site.route('/')
def index():
    return render_template('index.html')


@site.route('/getLogin')
def getLogin():
    return render_template('login.html')


@site.route('/register')
def register():
    return render_template('register.html')


@site.route('/findtutor')
def findtutor():
    return render_template('find_a_tutor.html')


@site.route('/tutorprofile')
def tutorprofile():
    return render_template('tutor_profile.html')


@site.route('/contactus')
def contactus():
    return render_template('contact_us.html')


@site.route('/aboutus')
def aboutus():
    return render_template('about_us.html')


@site.route('/home')
def home():
    return render_template('index.html')


@site.route('/submit')
def submit():
    return render_template('contact_thankyou.html')


@site.route('/updateinfo')
def tutor_profile():
    return render_template('tutorprofile.html')


@site.route('/registerUser', methods=['POST'])
def registerUser():
    # Create users key if it doesn't exist
    if 'users' not in db.keys():
        db['users'] = {}
    if 'email' not in db.keys():
        db['email'] = {}
    if 'specialties' not in db.keys():
        db['specialties'] = {}

    username = request.form['new_username']
    password = request.form['new_password']
    db['users'][username] = password

    return render_template('login.html')


@site.route('/checkLogin', methods=['POST', 'GET'])
def checkLogin():
    username = request.form['username']
    password = request.form['password']
    if username in db['users']:
        value = db['users'][username]
        if password == value:
            return render_template('tutor_profile.html')
        else:
            return render_template('login_fail.html')


@site.route('/updateInfo', methods=['POST'])
def updateInfo():
    if 'users' not in db.keys():
        db['users'] = {}
    if 'email' not in db.keys():
        db['email'] = {}
    if 'specialties' not in db.keys():
        db['specialties'] = {}

    name = request.form['name']
    email = request.form['email']
    specialties = request.form['specialties']

    if name in db['users']:
        db['email'][name] = email
        if specialties in db['specialties']:
          temp = db['specialties'][specialties]
          db['specialties'][specialties] = temp + ',' + name
        else:
          db['specialties'][specialties] = name
        return render_template('update_successful.html')


@site.route('/findTutor', methods=['POST'])
def findTutor():
    specialties = request.form['specialties']

    if specialties in db['specialties']:
        temp = db['specialties'][specialties]
        return render_template('find_a_tutor.html', value = db['specialties'][specialties])

site.run(host='0.0.0.0', port=8080)
