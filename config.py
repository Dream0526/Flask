#!/usr/bin/env python3


class BaseConfig:

    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(BaseConfig):

    DEBUG = True
    SECRET_KEY = b'0qf\xcd^R\x05\xcem\x88d\x8c\x85~\x05\xe4\\1\xc4\x90\xb3z\xc4e'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:crush@localhost:3306/pan'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 文件存储位置
    UPLOAD_FILE_REPOSITORY = 'C:\\Users\\ZouSK\\Desktop\\Flask\\Repository'


class ProductionConfig(BaseConfig):

    pass


class TestingConfig(BaseConfig):

    pass


Configs = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
