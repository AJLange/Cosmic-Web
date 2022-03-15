from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models.user import User
from flask_app.models.page import Page
from flask import render_template,redirect,request, session, flash


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
    '''
    if 'user_id' not in session:
        return redirect('/logout')
    '''
    data = {
        "id": id
    }    
    user= User.get_by_id(data)
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




