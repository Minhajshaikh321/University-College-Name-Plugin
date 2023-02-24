from flask import Flask ,jsonify, redirect,request, url_for
from flask_sqlalchemy import SQLAlchemy
import csv
from io import TextIOWrapper
from flask_marshmallow import Marshmallow

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Universities(db.Model):
    Sno= db.Column(db.Integer, primary_key = True)
    university = db.Column(db.String)
    college_name=db.Column(db.String ) 
    college_type=db.Column(db.String ) 
    state =db.Column(db.String)
    district = db.Column(db.String)
    
    def __init__(self ,university, college_name, college_type, state, district):
        self.university=university
        self.college_name=college_name
        self.college_type = college_type
        self.state=state
        self.district = district

class UniversitySchema(ma.Schema):
    class Meta:
        fields = ("university","college_name","college_type", "state", "district")
 
university_schema = UniversitySchema()
universities_schema = UniversitySchema(many=True)


# upload csv file into database
@app.route('/', methods=['GET', 'POST'])
def upload_csv():
    if request.method == 'POST':
        csv_file = request.files['filename']
        csv_file = TextIOWrapper(csv_file,encoding='utf-8')
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            user = Universities(university=row[1], college_name=row[2],college_type=row[3],state=row[4],district=row[5])
            print('user',user)
            print('user',row[0],row[1],row[2],row[3],row[4])
            db.session.add(user)
            db.session.commit()
        return redirect(url_for('upload_csv'))
    return ""


# get all of the universities details 
@app.route("/getall", methods=["GET"])
def get_all_deatils():
    details=Universities.query.all()
    result=universities_schema.dump(details) 
    return jsonify(result)
 

# get specific universities by passing university name
@app.route("/get/university/<university>", methods=["GET"])
def get_university_detail(university):
    all_university = db.session.query(Universities).filter(Universities.university.ilike(f'%{university}%')).all()
    university_count = db.session.query(Universities).filter(Universities.university.ilike(f'%{university}%')).count()
    result=universities_schema.dump(all_university)
    return jsonify({"Total Colleges in university":university_count},result)



# get specific universities by passing district name
@app.route("/get/district/<district>", methods=["GET"])
def get_university_by_district(district):
    district_university=Universities.query.filter_by(district=district).all()
    district_count=Universities.query.filter_by(district=district).count()
    result=universities_schema.dump(district_university)
    return jsonify({"Total Colleges in district":district_count},result)



# get specific universities by passing state name
@app.route("/get/state/<state>", methods=["GET"])
def get_university_by_state(state):
    state_university=Universities.query.filter_by(state=state).all()
    state_count=Universities.query.filter_by(state=state).count()
    result=universities_schema.dump(state_university)
    return jsonify({"Total Colleges in state":state_count},result)



# get specific universities by  college type(Affiliated College,Constituent / University College,Recognized Center)
@app.route("/get/collegetype/<collegetype>", methods=["GET"])
def get_university_by_collegetype(collegetype):
   colleges = db.session.query(Universities).filter(Universities.college_type.ilike(f'%{collegetype}%')).all()
   print(colleges)
   result=universities_schema.dump(colleges)
   return jsonify(result)


# create database 
with app.app_context():
    db.create_all() 

# create database 
# @app.route("/create")
# def database():
#     db.create_all()
#     return ({"msg":"database created"})


if __name__== "__main__":
    app.run(debug=True)