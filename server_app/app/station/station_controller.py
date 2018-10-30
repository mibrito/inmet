from station import Station
from app import session, db
from config import PATH_STATIONS_FILE

import pandas as pd

class StationController:
	def storeStationsDB(self):
		stations_list = []
		stations = pd.read_csv(PATH_STATIONS_FILE, sep=';')

		for i in range(0, len(stations)):
			lat = stations.iloc[i]['Latitude'].split(':')[1].strip()
			lon = stations.iloc[i]['Longitude'].split(':')[1].strip()
			
			coord = 'SRID=4674;POINT({lon} {lat})'.format(lat=lat, lon=lon)
			omm = stations.iloc[i]['Estacao'].split('OMM:')[1].replace(')', '').strip()
			name = stations.iloc[i]['Estacao'].split(' : ')[1].split('-')[0].strip()
			estate = stations.iloc[i]['Estacao'].split('-')[1].split('(')[0].strip()
			altitude = stations.iloc[i]['Altitude'].split(':')[1].strip()

			station = Station(omm=omm, name=name, geom=coord, estate=estate, altitude=altitude)
			stations_list.append(station)
			session.add(station)
			session.commit()


