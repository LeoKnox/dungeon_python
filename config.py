import os

class Config(object):
    SECRET_KEY = os.environment.get('SECRET_KEY') or "supersecret"

    MONGODB_SETTINGS = { 'db' : 'Python_DungeonDB'}