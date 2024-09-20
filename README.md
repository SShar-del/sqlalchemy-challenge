# Sqlalchemy-Challenge

A climate analysis project for planning a long holiday vacation in Honolulu, Hawaii. 

For this project,  I accomplished this task as presented in the two sections outlining the steps taken. Also, created a Climate App using Flask.  


## Jupyter NoteBook Database connection

Used the SQLAlchemy functions like create_engine(), automap_base()function to connect to the hawaii SQLite database and reflect  the 2 tables, measurement and station, into classes.  

Saved references to the classes named station and measurement and created a SQLAlchemy session.  

## Analysis on Jupyter Notebook - climate_starter_solution

### Precipitation Analysis
- Created a query that finds the most recent date in the dataset  

- Created a query that collects only the date and precipitation for the last year of data without passing the date as a variable  

- Saved the query results to a Pandas DataFrame, prcp_df, to create Date and Precipitation columns  

- Sorted the DataFrame by date using sort_values function  

- Plotted the results by using the DataFrame plot method with date as the x and precipitation as the y variables  

- Used Pandas describe function to print the summary statistics for the precipitation data  

### Station Analysis

- Created a query that to find the number of stations in the dataset  

- Created a query that lists the stations and observation counts in descending order and finds the most active station (USC00519281)  

- Created a query that finds the min, max, and average temperatures for the most active station (USC00519281)  

- Created a query to get the previous 12 months of temperature observation (TOBS) data that filters by the most active station  

- Saved the query results to a Pandas DataFrame, tobs_df  

- Plotted a histogram with bins=12 for the last year of data using tobs as the column to count  

### Climate App using Flask - app.py


- Generated the engine to the hawaii sqlite  

- Used automap_base() and reflected the database schema  

- Saved references to the tables in the sqlite file (measurement and station)  

- Created the session between the python app and database  

- Displayed the available routes on the landing page  


#### Created routes as follows:

- /  
 Starts at the homepage. Lists all the available routes  

- /api/v1.0/precipitation  

Converted the precipitation analysis (i.e. the last 12 months of data) to a dictionary using date as the key and prcp as the value.

Returns the JSON representation of your dictionary.

- /api/v1.0/stations  

Returns a JSON list of stations from the dataset  

- /api/v1.0/tobs  

Queries the dates and temperature observations of the most-active station for the previous year of data  

Returns a JSON list of temperature observations for the previous year  

- /api/v1.0/<start> and /api/v1.0/<start>/<end>  

Returns a JSON list of the min temperature, the avg temperature, and the max temperature for all the dates greater than or equal to the specified start date and for the dates from the start date to the end date, inclusive for the specified start-end range.  


## Acknowledgements

 - Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xml