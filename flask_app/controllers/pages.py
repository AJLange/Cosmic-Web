from xmlrpc.client import _iso8601_format
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
import json
import requests
from flask_app.models.user import User
from flask_app.models.page import Page
from flask import render_template,redirect,request, session, jsonify
import os 
import datetime
import iso8601
print( os.environ.get("FLASK_APP_API_KEY") )

@app.route('/')        
def index():
    if 'user_id' in session:   
        data = {
            'id': session['user_id']
        } 
    else:
        data = {
            'id': 0
        } 
    user = User.get_by_id(data)
    posts = Page.get_posts_users()
    return render_template('index.html', posts=posts, user=user)

@app.route('/talent')        
def talent():    
    return render_template('talent.html')

@app.route('/about')        
def about():    
    return render_template('about.html')

@app.route('/policy')        
def policy():
    return render_template('policy.html')


@app.route('/contact')        
def contact():    
    return render_template('contact.html')

@app.route('/edit/<int:id>')
def edit_post(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }    
    post= Page.get_by_id(data)
    return render_template("edit.html", post=post)

@app.route('/delete/<int:id>')
def delete_post(id):
    '''
    if 'user_id' not in session:
        return redirect('/logout')
        '''
    data = {
        "id": id
    }    
    Page.destroy(data)
    return redirect('/dashboard')

@app.route('/dashboard')        
def dashboard(): 
    
    if 'user_id' not in session:
        return redirect('/logout')
    
    data = {
        'id': session['user_id']
    }  
    user = User.get_by_id(data)
    posts = Page.get_posts_users()
    return render_template('dashboard.html', user=user, posts=posts)


@app.route('/addpost')
def add_post():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('create.html')

@app.route('/create', methods=["POST"])
def create_post():

    if 'user_id' not in session:
        return redirect('/logout')

    data = {
        "message":request.form['message'],
        "header": request.form['header'],
        "posted_by": request.form['posted_by'],
    }
    Page.save(data)
    return redirect('/dashboard')

@app.route('/update', methods=["POST"])
def update():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "message": request.form['message'],
        "header": request.form['header'],
        "posted_by": request.form['posted_by'],
        "id": request.form['id'],
    }
    Page.update(data)
    return redirect('/dashboard')

@app.route('/member-1')        
def member1():
    url = "https://api.twitch.tv/helix/schedule?broadcaster_id=40091555"
    headers = {
            "Authorization": f"Bearer {os.environ.get('FLASK_API_KEY')}",
            "Client-Id": f"{os.environ.get('FLASK_CLIENT_ID')}"
    }
    r = requests.get(url, headers=headers)
    data = json.loads(r.content)
    print(data)

    date = date_clean("2018-09-07T04:57:58.050-07:00")
    return render_template('member-l.html', data=data, date=date)

def date_clean(data):
    date_obj=iso8601.parse_date(data)
    return date_obj

#This was just to test, commenting it out for now

@app.route('/calendar')
def calendar_get():
    url = "https://api.twitch.tv/helix/schedule?broadcaster_id=40091555"
    headers = {
            "Authorization": f"Bearer {os.environ.get('FLASK_API_KEY')}",
            "Client-Id": f"{os.environ.get('FLASK_CLIENT_ID')}"
    }
    r = requests.get(url, headers=headers)
    return jsonify( r.json() )  
