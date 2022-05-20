from dotenv import load_dotenv
import os

load_dotenv()

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'my_db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
