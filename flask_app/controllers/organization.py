from flask_app import app
from flask_app.models.organization import Organization
from flask import render_template, redirect, request,Flask, session

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


class Organization:
    def __init__(self, data):
        self.org_name = data['org_name']
        self.contact_email = data['Email']
        self.org_address = data['org_address']
        self.state= data['state']
        self.password= data['password']  
   


@app.router ('/org/registerorg')
def index_org():
        return render_template('registerorg.html')
'''
    @app.route('/orgs/das')
    def dev_skill_language()
        if 'user_id' in session:
            return redirect('/logout')
        data = {
            "id": session['use']
        }
'''            
def index():
        return render_template('/orgs/register.html')

@app.route('/register',methods=['POST'])
def register_new_org():
        if not Organization.validate_register(request.form):
            return redirect('/orgs/registerorg')
        
        data = {   
            'org_name': request.form ['Organization Name'],
            'contact_email': request.form ['Email'],
            'org_address': request.form ['org_addres'],
            'state': request.form ['state'],
            'password': bcrypt.generate_password_hash(request.form['password'])
    }
        id = Organization.save(data)
        session['user_id']= id
        print ("id usuario",id)
        return redirect("/orgs/dashboard")
