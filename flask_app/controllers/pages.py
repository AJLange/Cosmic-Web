from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models.user import User
from flask_app.models.page import Page
from flask import render_template,redirect,request, session, flash

@app.route('/edit')        
def edit():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    users = User.get_all()
    return render_template('edit.html', user=User.get_by_id(data), posts=Page.get_posts())

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
    return render_template('member-l.html')


