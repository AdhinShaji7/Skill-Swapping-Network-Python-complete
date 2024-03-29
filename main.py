from flask import Flask
from public import public
from admin import admin
from staff import staff
from pro import pro
from api import api

app=Flask(__name__)

app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(staff)
app.register_blueprint(pro)

app.register_blueprint(api,url_prefix="/api")

app.secret_key="akhila"


app.run(debug=True,port=5854,host="0.0.0.0")