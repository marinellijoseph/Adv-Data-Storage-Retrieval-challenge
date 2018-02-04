from flask import Flask, jsonify
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#################################################
# Database Setup
#################################################

# reflect an existing database into a new model
Base = automap_base()

# create engine
engine = create_engine("sqlite:///hawaii.sqlite")


# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to the invoices and invoice_items tables
Measurement = Base.classes.measurements
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

session.query.delete(Station)
session.query.delete(Measurement)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################


app = Flask(__name__)

@app.route('/')
def home():
    return (
        f"Home Page"

        f"Avalable Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"- description<br/>"

        f"/api/v1.0/tobs"
        f"- description<br/>"

        f"/api/v1.0/<start>` and `/api/v1.0/<start>/<end> <br/>"
        f"- Invoice Total for a given country (defaults to 'USA')<br/>"
    )
        
@app.route('/ api / v1.0 / precipitation')
def precipitation():
        "returns json of precipitation query"

        results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= "2011-01-09", Measurement.date <= "2012-01-09").\
        all()

    # creates JSONified list
        precipitation_list = [results]
        return jsonify(precipitation_list)
