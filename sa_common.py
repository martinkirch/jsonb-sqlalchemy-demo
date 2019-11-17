from logging.config import fileConfig
from configparser import SafeConfigParser
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from sa_metadata import Base
from sqlalchemy.orm import configure_mappers

# load all modules containing mapped classes:
import model1
import model2
import model3
import model4

configure_mappers()

def connect(config_path='conf.ini'):
    fileConfig(config_path, disable_existing_loggers=False)
    config_parser = SafeConfigParser()
    config_parser.read(config_path)
    settings = dict(config_parser.items('sqlalchemy'))
    engine = engine_from_config(settings)
    Base.prepare(engine)
    Session = sessionmaker(bind=engine)
    return Session()
