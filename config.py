import os
SQLALCHEMY_TRACK_MODIFICATIONS = False

class Config:

    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgres://gsapdsysaudhdt:1a505e7763ceec04f1b563b24b24c5b5681104b5d03dce8fa973c5c2bda26fe5@ec2-52-86-73-86.compute-1.amazonaws.com:5432/d3okpr2s0frj1h'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}