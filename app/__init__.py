from flask import Flask


# location where file uploads will be stored
UPLOAD_FOLDER = './app/static/uploads'
SECRET_KEY = 'Sup3r$3createsecretecodekey'

app = Flask(__name__)
app.config.from_object(__name__)
from app import views
