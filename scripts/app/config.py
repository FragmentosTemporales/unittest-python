import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    """ Base configuration application class """
    print("MODE: BaseConfig")


class DevConfig(BaseConfig):
    """ Development configuration class """
    pass


class ProductionConfig(BaseConfig):
    """ Production configuration class """
    pass


class TestConfig(BaseConfig):
    """ Testing configuration class """
    pass


config = {
    "dev": DevConfig,
    "prod": ProductionConfig,
    "test": TestConfig
}
