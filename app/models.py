from app import db


class InfoBanjir(db.Model):
    """This class represents the bucketlist table."""

    __tablename__ = 'infobanjir_'

    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(255))
    station_name = db.Column(db.String(255))
    district = db.Column(db.String(255))
    river_basin = db.Column(db.String(255))
    date = db.Column(db.String(255))
    time = db.Column(db.String(255))
    water_level = db.Column(db.String(255))

    def __init__(self, station_name, district, river_basin, date, time, water_level, state):
        self.state = state
        self.station_name = station_name
        self.district = district
        self.river_basin = river_basin
        self.date = date
        self.time = time
        self.water_level = water_level

    def __repr__(self):
        return "<InfoBanjir: {}>".format(self.state)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return InfoBanjir.query.all()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()