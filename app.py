from flask_restful import Resource,Api,reqparse
from flask_cors import CORS
from flask import Flask , render_template , request , redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import os
import psycopg2


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://manokarthij_2412:3EyrhOjjc98GpMQIeR7kLlE54Jm1LPEe@dpg-cfubsdirrk0c831mshag-a.oregon-postgres.render.com/bank_details"

db = SQLAlchemy(app)
app.app_context().push()
api = Api(app)
CORS(app)

class bank_details(db.Model):
    ifsc = db.Column(db.String,primary_key=True)
    bank_id = db.Column(db.Integer)
    branch = db.Column(db.String)
    address = db.Column(db.String)
    city = db.Column(db.String)
    district = db.Column(db.String)
    state = db.Column(db.String)
    bank_name = db.Column(db.String)

class BANK_SEARCH(Resource):
    def get(self):
        conn = psycopg2.connect("postgresql://manokarthij_2412:3EyrhOjjc98GpMQIeR7kLlE54Jm1LPEe@dpg-cfubsdirrk0c831mshag-a.oregon-postgres.render.com/bank_details")
        cur=conn.cursor()
        posts = cur.execute('SELECT * FROM bank_branches')
        lists=cur.fetchall()
        cur.close()
        conn.close()
        query = request.args.get('q').upper()
        limit = int(request.args.get('limit'))
        offset = int(request.args.get('offset'))
        ind = []
        
        for i in lists:
            flag=0
            for j in range(2,8):
                if i[j] and query in i[j]:
                    flag=1
            if flag:
                ind.append(i)

    
        obj = ind[(offset+1):(offset+limit+1)]
        l=[]
        for i in obj:
            l.append((i[0],{"ifsc":i[0],
                              "bank_id":i[1],
                              "branch":i[2],
                              "address":i[3],
                              "city":i[4],
                              "district":i[5],
                              "state":i[6],
                              "bank_name":i[7]
                              }))
        l.sort()
        temp=[]
        for i in l:
           temp.append(i[1])
        return {
            "branches":temp
        }

class BANK_BRANCH(Resource):
    def get(self):
        conn = psycopg2.connect("postgresql://manokarthij_2412:3EyrhOjjc98GpMQIeR7kLlE54Jm1LPEe@dpg-cfubsdirrk0c831mshag-a.oregon-postgres.render.com/bank_details")
        cur=conn.cursor()
        posts = cur.execute('SELECT * FROM bank_branches')
        lists=cur.fetchall()
        cur.close()
        conn.close()
        query = request.args.get('q').lower()
        limit = int(request.args.get('limit'))
        offset = int(request.args.get('offset'))
        ind = []
        
        for i in lists:
            flag=0
            for j in range(2,8):
                if i[j] and query in i[j].lower():
                    flag=1
            if flag:
                ind.append(i)

    
        obj = ind[(offset+1):(offset+limit+1)]
        l=[]
        for i in obj:
            l.append((i[0],{"ifsc":i[0],
                              "bank_id":i[1],
                              "branch":i[2],
                              "address":i[3],
                              "city":i[4],
                              "district":i[5],
                              "state":i[6],
                              "bank_name":i[7]
                              }))

        l.sort(reverse=True)
        temp=[]
        for i in l:
           temp.append(i[1])
        return {
            "branches":temp
        }      

api.add_resource(BANK_SEARCH,'/api/search')
api.add_resource(BANK_BRANCH,'/api/branch')

if __name__ == '__main__':
    app.run(debug=True,port=5050)
