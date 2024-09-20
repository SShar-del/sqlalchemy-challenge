# Import the dependencies.

import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import math

from flask import Flask, jsonify


app= Flask(__name__)


#################################################
# Database Setup
#################################################


# reflect an existing database into a new model
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect the tables
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app= Flask(__name__)

#################################################
# Flask Routes
#################################################


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
   
    """Return JSON dictionary using date as the key and precipitation as the value."""
  
       
    # Query 12 month date and precipitation data
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2016-08-23').all()
    
    # Convert list of tuples into dictionary - date as key and temp as value
   
    precipitation_dict = {}
    for date, prcp in results:
        
        precipitation_dict[date] = prcp
        
    return jsonify(precipitation_dict)


@app.route("/api/v1.0/stations")
def stations():
   
    """Return a JSON list of stations from the dataset."""

    # Query all distinct stations
    results = session.query(Measurement.station).distinct().all()    
   
    # Convert list of tuples into normal list
    station_list = list(np.ravel(results))

    return jsonify(station_list)



@app.route("/api/v1.0/tobs")
def tobs():
    """ Return a JSON list of temperature observations for the previous year. """
           
    #Query the dates and temperature observations of the most-active station (USC00519281) for the previous year of data.
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= '2016-08-23').filter(Measurement.station == 'USC00519281').all()
    
    #Return a JSON list of temperature observations for the previous year
    tobs_results =[]
    for result in results:
        tobs_results.append(result[1])
    return jsonify(tobs_results)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def stats(start=None, end=None):
    """Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified  start date or a start-end range. """
   
    try:
        
        canonicalized_start = dt.datetime.strptime(start, "%Y-%m-%d").date()
        if end is not None:
            canonicalized_end = dt.datetime.strptime(end, "%Y-%m-%d").date()
        
        # For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date. 
        #For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive
        if (start is not None) and (end is None):
            result = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= canonicalized_start).all()
            
        else:
            if end is not None:
                
                #canonicalized_end = dt.datetime.strptime(end, "%Y-%m-%d").date()
                result = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= canonicalized_start).filter(Measurement.date <= canonicalized_end).all()

        temp_stats = list(np.ravel(result))
        if temp_stats[0] is not None:
            return(temp_stats)
        else:
            return({"error": f"Start date {start} not found in database."}), 404
    except ValueError:
        
        return({"error": f"Incorrect date format. Expected YYYY-MM-DD."}), 404

session.close()

if __name__ == '__main__':
    app.run(debug=True)
