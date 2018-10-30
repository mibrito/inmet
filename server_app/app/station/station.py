from sqlalchemy import Column, Integer, String, DECIMAL
from geoalchemy2 import Geometry
from app import base


class Station(base):
	__tablename__ = 'stations'

	omm = Column(DECIMAL(5), primary_key=True)
	name = Column(String(35))
	geom = Column(Geometry(geometry_type='POINT', srid=4674))
	estate = Column(String(2))
	altitude = Column(DECIMAL(6,2))