from user import User
import os
from flask import  session, render_template, request, redirect, g, url_for
from bucketlist import Bucketlist
from app import app


newuser = User()
"""Instantiating objects"""
Newbucketlist = Bucketlist()
app.secret_key = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def reg():
    """Handles the requests for the register view"""
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['cpassword']
        result = newuser.register(email, name, password, cpassword)
        if result == 1:
            session['user'] = name
            return render_template('login.html')
        elif result == 5:
            msg = ("please fill all the fields")
            return render_template('register.html', data=msg)
        elif result == 3:
            msg = ("password mismatch")	
            return render_template('register.html', data=msg)
        elif result == 2:
            error = "email must be a valid email"
            return render_template('register.html', data=error)	
        elif result == 4:
            error = "email already exists"
            return render_template('register.html', data=error)	
    else:
        return render_template('register.html')
                		
@app.route('/login/', methods=['GET', 'POST'])
def logins():
    """Handles the requests for the login view"""
    if request.method == "POST":
        emailLogin = request.form['email']
        passLogin = request.form['password']
        loginResult = newuser.login(emailLogin, passLogin)
        if loginResult == 1:
            name = newuser.get_user_name(emailLogin)
            email = newuser.get_user_email(emailLogin)
            session['user'] = name
            session['email'] = email
            return render_template('home.html', data=session)
        elif loginResult == 2:
            error = "Password mismatch"
            return render_template('login.html', data=error)	
        elif loginResult == 3:
            error = "The user does not exist please register and try again"
            return render_template('login.html', data=error)	
        elif loginResult == 4:
            error = "Please fill all the fields"
            return render_template('register.html', data=error)	 	
        else:
            error = "Wrong credentials please try again"
            return render_template ('login.html',data=error) 
    else:
        return render_template('login.html')

@app.route('/create/', methods=['GET', 'POST'])
def createbucketlist():
    """Handles creation of bucketlists"""
    if g.user:
        if request.method == "POST":
            sentence = request.form['post']
            Postlist = sentence.split(' ')
            post = ''.join(Postlist)
            describe = request.form['description']
            owner = session['email']
            result = Newbucketlist.create(post, describe, owner)
            print(post)
            if result == 2:
                error = "that bucket title already exists"
                return render_template('create.html', data=error)
            if result == 3:

                error = "Please fill all the fields"
                return render_template('create.html', data=error)                   
            if result == 1:
                result = Newbucketlist.get_mybucket_lists(owner)  
                bucketitems = Newbucketlist.getitems() 
                return render_template('mybucketlist.html', datas=result, items=bucketitems)		
            return redirect('/mybuckets/')
        else:
            return render_template('create.html')
    else:
        return render_template('login.html')	

@app.route('/mybuckets/', methods=['GET'])
def getbuckets():
    """defining route to get all buckets"""
    if g.user:
        itemowner = session['email']
        owner = session['email']
        result = Newbucketlist.get_mybucket_lists(owner)
        bucketitems = Newbucketlist.getitems() 
        if (result != {}):
            return render_template('mybucketlist.html', datas=result, items=bucketitems)
        else:
            error = "create a bucket first"
            return render_template('create.html', data=error)
    else:
        return render_template('login.html')		

@app.route('/delete/<post>')
def delete(post):
    """define route to delete a bucketlist"""
    if g.user:
        res = Newbucketlist.get_bucket_list(post)
        if res:
            result = Newbucketlist.delete(post)
            if result == True:
                message = "successfully deleted"
                return redirect(url_for('getbuckets', data=message))
            else:
                message = "Bucket not deleted"
                return redirect(url_for('getbuckets', data=message))				
        else:
            message = "not found"
            return render_template('create.html', data=message)
    else:
        return render_template('create.html')
    return render_template('login.html')

@app.route('/editbucketlist/<post>')
def editbucketlist(post):
    """defining route to get the post to edit"""
    if g.user:
        res = Newbucketlist.get_bucket_list(post)
        if res:
            return render_template('edit.html', data=res)	
        return redirect('/mybuckets')
    else:
        return render_template('login.html')	

@app.route('/editbucket/', methods=['GET', 'POST'])
def editbucket():
    """defining route to edit a bucketlist"""
    if g.user:
        if request.method == "POST":
            old = request.form['old']
            sentence = request.form['post']
            Postlist = sentence.split(' ')
            post = ''.join(Postlist)
            describe = request.form['description']
            owner = session['email']
            result = Newbucketlist.edit(old, post, describe, owner)
            if result == 1:
                message = "bucket successfully updated"
                result = Newbucketlist.get_mybucket_lists(owner)
                bucketitems = Newbucketlist.getitems()    
                return render_template('mybucketlist.html', datas=result, msg=message, items=bucketitems)
            elif result == 2:
                return redirect('/mybuckets')	
            elif result == 3:
                return redirect('/mybuckets')
            elif result == 4:
                return redirect('/mybuckets')	
    else:
        return render_template('login.html')

@app.route('/createitem/', methods=['GET', 'POST'])
def additems():
    """Handles the  requests for creating an item"""
    if g.user:
        if request.method == "POST":
            sentence = request.form['item']
            itemlist = sentence.split(' ')
            item = ''.join(itemlist)
            post = request.form['post']
            owner = session['email']
            result = Newbucketlist.createitem(post, item)
            if result == 1:
                bucketitems = Newbucketlist.getitems()
                print (bucketitems)
                print('yes')
                result = Newbucketlist.get_mybucket_lists(owner)       
                return render_template('mybucketlist.html', datas=result, items=bucketitems,)			
            elif result == 3:
                bucketitems = Newbucketlist.getitems()
                message = "item already exists"
                result = Newbucketlist.get_bucket_lists()       
                return render_template('mybucketlist.html',datas=result,items=bucketitems, data=message)	
        else:
            return render_template('create.html' )
    return render_template('login.html' )	

@app.route('/edititem/<item>', methods=['GET','POST'])
def edititem(item):
    """Handles  requests for editing an item"""
    if g.user:
        if request.method == "POST":
            sentence = request.form['item']
            itemlist = sentence.split(' ')
            item = ''.join(itemlist)
            post = request.form['post']
            old = request.form['old']
            owner = session['email']
            result = Newbucketlist.itemedit(item, old)
            if result == 1:
                bucketitems = Newbucketlist.getitems()
                print(bucketitems)
                result = Newbucketlist.get_mybucket_lists(owner)        
                return render_template('mybucketlist.html', datas=result, items=bucketitems)
            elif result == 2:
                return redirect('/mybuckets/')
            else:
                return redirect('/mybuckets/')	
        else:
            bucketitems = Newbucketlist.getitems()
            for dic in bucketitems:
                result = Newbucketlist.get_bucket_lists()       
                return render_template('mybucketlist.html', datas=result, items=bucketitems)		
    else:
        return render_template('login.html')

@app.route('/deleteitem', methods=['GET', 'POST'])
def deleteitem():
    """Handles requests for deleting an item"""
    if g.user:
        item = request.form['item']
        post = request.form['post']
        owner = session['email']
        itemowner = session['email']
        result = Newbucketlist.deleteitem(item)
        if result == True:
            message = "successfully deleted"
            bucketitems = Newbucketlist.getitems()
            results = Newbucketlist.get_mybucket_lists(owner)			
            return render_template('mybucketlist.html', msg=message, datas=results, items=bucketitems )
        else:
            return render_template('create.html')
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Handles requests to logout a user"""
    session.pop('user', None)
    return redirect(url_for('logins'))

@app.route('/home/')
def protected():
    """Handles request to get the homepage"""
    if g.user:
        return render_template('home.html')

    return redirect(url_for('logins'))

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']
