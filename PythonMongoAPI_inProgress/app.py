from flask import request, Flask
from pymongo import MongoClient
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
# from mongoengine import *
import json
 
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'secret-key'
jwt = JWTManager(app)

#Connections to communicate with MongoDb database 
client = MongoClient("mongodb://localhost:5003/")
db = client["profiles_db"]
profiles = db["profiles"]


class User(db.Document):
    email = db.StringField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    created = db.DateTimeField(required=True)
    updated = db.DateTimeField(required=True)


class Profile(db.Document):
    id_user = db.StringField(User, required=True)
    name = db.StringField()
    surname = db.StringField()
    phone = db.StringField()
    created = db.DateTimeField(required=True)
    updated = db.DateTimeField(required=True)

@app.route('/Authenticate', methods = ['POST'])
def Authenticate():
    return {'username' : request.form['username'], 'password' : request.form['password']}


#The route used if a client wants to register
@app.route("/register", methods = ['POST'])
def register():
    try:
        email = request.json.get('email')
        password = request.json.get('password')
        name = request.json.get('name')
        surname = request.json.get('surname')
        phone = request.json.get('phone')

        if User.objects(email = email):
            return {"error": "Email already exists"}, 400

        if not email or not password:
            return {"error": "Email and password are required"}, 400

        user = User(email=email, password=password, created='', updated='').save()
        profile = Profile(id_user=user, name=name, surname=surname, phone=phone, created='', updated='').save()
        return ({'message' : 'Profile created'}, 201)
        
    except Exception as e:
        return json.dumps({'error'}, 400)


#The route used if a client wants to login
@app.route("/login", methods = ['GET', 'POST'])
def login():
    try:
        email = request.json.get('email')
        password = request.json.get('password')
        
        user = User.objects(email=email).first()
        if not user:
            return {"error": "Email not found"}, 400

        if user.password != password:
            return {"error": "Incorrect password"}, 400

        access_token = create_access_token(identity=email)
        return {"access_token": access_token}, 200

    except Exception as e:
        return json.dumps({'error': str(e)}, 400)


#The route used if a client created a profile, wants to update or delete the profile
@app.route("/profile", methods = ['GET', 'PUT', 'DELETE'])
@jwt_required
def profile():
    try:
        username = request.args.get('username')

        if username is None:
            return {"error": "Username is required"}, 400

        profile = profiles.find_one({"username": username})

        if request.method == 'GET':
            if profile is None:
                return {"error": "Profile not found"}, 404
        return {"profile" : profile}, 200

        if request.method == 'PUT':
            if profile is None:
                return {"error": "Profile not found"}, 404

            profile = profiles.find_one_and_update(
                {"username": username}, 
                {"$set": request.json}
            )

            return {"profile": profile}, 200

        if request.method == 'DELETE':
            if profile is None:
                return {"error": "Profile not found"}, 404

            profiles.delete_one({"username": username})
            return {"message": "Profile deleted"}, 200

    except Exception as e:
        return json.dumps({'error'}, 400)
    

#The route used if information on the database is requested
@app.route("/profiles", methods = ['GET'])
@jwt_required
def profiles():
    try:
        list_profiles = [i for i in profiles.find()]
        return {"profiles": list_profiles}, 200
    except Exception as e:
        return json.dumps({'error'} , 400)

         
if __name__ == "__main__":
     app.run()

