from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Database connection
db = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

# Database extensions
db.execute("CREATE EXTENSION IF NOT EXISTS postgis")


base = declarative_base()

# Entities
from app.station.station import Station
from app.mensuration.mensuration import Mensuration


# Create all entities
base.metadata.create_all(db)


Session = sessionmaker(db)
session = Session()

# from app.mensuration.mensuration_controller import MensurationController
# mensurationController = MensurationController()
# mensurationController.storeMensurations()

# from app.station.station_controller import StationController
# stationController = StationController()
# stationController.storeStationsDB()

# Register blueprint(s)
from app.mensuration.mensuration_gateway import mensuration
app.register_blueprint(mensuration)
