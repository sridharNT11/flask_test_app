class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'mysql+mysqldb://urbanedg_train:P&,1(r7-+o2o@72.52.161.232:3306/urbanedg_training_project'
    # ENV = "development"

class ProductionConfig(Config):
    DATABASE_URI = 'mysql+mysqldb://root:@127.0.0.1:3306/test_app'
    CACHE_TYPE  = 'NULL'
    
class DevelopmentConfig(Config):
    DEBUG = True

class SECRET_KEY(Config):
    SECRET_KEY = '5678906567890543346789976565'
