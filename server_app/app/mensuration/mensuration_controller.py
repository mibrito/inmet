from app import session
from app.station.station import Station
from app.mensuration.mensuration import Mensuration
from config import PATH_MENSURATIONS_FILES

from sqlalchemy import func, extract, desc

import pandas as pd
import datetime


class MensurationController:
    def storeMensurations(self):
        stations = session.query(Station.omm).all()

        for station in stations:
            file = '{}/s{}.csv'.format(PATH_MENSURATIONS_FILES, station[0])
            df_station = pd.read_csv(file, sep=';')

            for i in range(len(df_station)):
                station = int(df_station.iloc[i]['Estacao'])
                day, month, year = df_station.iloc[i]['Data'].split('/')
                tempMax = float(df_station.iloc[i]['TempMax'])
                tempMin = float(df_station.iloc[i]['TempMin'])
                tempAvg = float(df_station.iloc[i]['TempMedia'])
                evp = float(df_station.iloc[i]['Evaporacao'])
                prec = float(df_station.iloc[i]['Precipitacao'])
                insolation = float(df_station.iloc[i]['Insolacao'])
                humidity = float(df_station.iloc[i]['Umidade'])

                mensuration = Mensuration(station=station, source='INMET', date=datetime.date(int(year), int(month), int(day)), tempMax=tempMax, tempMin=tempMin, tempAvg=tempAvg,
                                          evp=evp, prec=prec, insolation=insolation, humidity=humidity)
                session.add(mensuration)
                session.commit()


    def getFrequencyPerYear(self):
        mensurationPerYear = session\
            .query(Mensuration.station.label('station'), func.date_part('year', Mensuration.date).label('year'), func.count(func.date_part('year', Mensuration.date)))\
            .group_by(Mensuration.station, func.date_part('year', Mensuration.date))\
            .order_by('year')\
            .all()\

        totals = session \
                .query(Mensuration.station.label('station'), func.count(Mensuration.station))\
                .group_by(Mensuration.station)\
                .order_by('station')\
                .all()\

        response = []
        for row in mensurationPerYear:
            for row_2 in totals:
                if (row_2[0] == row[0]):
                    total = row_2[1]
                    break

            response.append({
                'station': str(row[0]),
                'year': int(row[1]),
                'frequency': int(row[2]),
                'total': int(total)
            })

        return response
