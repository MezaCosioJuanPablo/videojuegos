import os

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://u223049366_sitemasquinto:/4dU0mFKn1B@srv1838.hstgr.io/u223049366_sitemasquinto"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_RECYCLE = 280
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_MAX_OVERFLOW = 20
    SECRET_KEY = os.urandom(24)