from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
import requests
from flask_app.models.user import User
from flask_app.models.page import Page
from flask import render_template,redirect,request, session, make_response, jsonify
import os
print( os.environ.get("FLASK_APP_API_KEY") )

@app.route('/')        
def index():
    data = {
        "id": id
    }    
    posts = Page.get_posts()
    return render_template('index.html', posts=posts)

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

@app.route('/member-1')        
def member1():
    jsonData = searching()
    print(jsonData)
    return render_template('member-l.html')


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

    posts = Page.get_posts()
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


@app.route('/get_data')
def get_data():
    # jsonify will serialize data into JSON format.
    return jsonify(message="Hello World")

@app.route('/calendar')
def searching():
    url = "https://api.twitch.tv/helix/schedule?broadcaster_id=40091555"
    headers = {
            "Authorization": f"Bearer {os.environ.get('FLASK_API_KEY')}",
            "Client-Id": f"{os.environ.get('FLASK_CLIENT_ID')}"
    }
    r = requests.get(url, headers=headers)
    return jsonify( r.json() )