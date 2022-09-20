'''
A DataSource class definition that describes
an object that can interact with the 'run' database
on a sql server and execute queries given specific
inputs with the help of methods.

author: Antonio Marino, Jeremy Beckler
CS 257, Winter 2022
'''

import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs
import psqlConfig as config
from datasourceHelperFunctions import *


class DataSource:
    '''
    DataSource executes all of the queries on the database.
    It also formats the data to send back to the frontend,
    typically in a list or some other collection or object.
    In this case, I chose to just return integers or floats
    due to the simple nature of the queries.
    '''

    def __init__(self):
        '''
        This constructor initializes a connection to the
        database via information specified in the
        psqlConfig.py file.
        '''
        try:
            self._databaseConnection =  psycopg2.connect(database=config.database, user=config.user, password=config.password, host="localhost")
        except Exception as e:
            print("Connection error: ", e)
            exit()

    def runQuery(self, query, parameters):
        '''
        Helper method for executing a sql query given the general
        code for the query as well as the parameters applied in
        the query.
        PARAMETERS:
            query - the general sql code with temporary placeholders
            for specific values
            parameters - the specific values of types int, float, or
            string that will be passed into the query
        RETURN:
            result - the unformatted data retrieved by the query
        '''
        query = psycopg2.sql.SQL(query)
        cursor = self._databaseConnection.cursor()
        cursor.execute(query, parameters)
        result = cursor.fetchall()
        return result

    def getPercentFromVO2(self, vO2, gender):
        '''
        Returns a fitness percentile rank among Norwegians
        given a VO2 Max Score.
        PARAMETERS:
            vO2 - the VO2 Max score of the user represented as a
            positive float
            gender - the gender of the user in the form of a string:
            'Male', 'Female', or 'Other'
        RETURN:
            percentile - a float between 0.0 and 99.99 representing the
            fitness percentile rank among Norwegians
        '''
        try:
            gender = convertGenderToVO2TableCategory(gender)
            '''This query compares the VO2 Max score across  
            individuals in the database, and finds the row with the VO2 Max
            Score that is closest to the one inputted by the user, and returns
            the corresponding percentile'''
            query = """WITH cte
AS
(
SELECT percentile, ROW_NUMBER() over(order by abs(%s - %s)) as rw
FROM run
)SELECT *
FROM cte
WHERE rw<=1;"""
            queryResult = self.runQuery(query, (AsIs(gender), vO2))
            percentile = int(queryResult[0][0])/100
            return percentile

        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None


    def getVO2FromPercent(self, percentile, gender):
        '''
        Returns a VO2 max score given a fitness
        percentile rank among Norwegians.
        PARAMETERS:
            percentile - a float between 0.0 and 99.99 representing the
            fitness percentile rank among Norwegians
            gender - the gender of the user in the form of a string:
            'Male', 'Female', or 'Other'
        RETURN:
            vO2 - the corresponding VO2 Max score represented as a
            positive float
        '''
        try:
            percentile = convertFloatToPercentile(percentile)
            VO2TableCategory = convertGenderToVO2TableCategory(gender)
            query = "SELECT %s FROM run WHERE percentile::float BETWEEN %s AND %s ORDER BY percentile;"
            queryResult = self.runQuery(query, (AsIs(VO2TableCategory), percentile, percentile))
            vO2 = queryResult[0][0]
            return vO2

        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None

    def getPercentFromTreadRuntime(self, treadRuntime, gender):
        '''
        Returns a fitness percentile rank among Norwegians
        given a treadmill runtime.
        PARAMETERS:
            treadRunTime - a treadmill run time in seconds represented
            as an int
            gender - the gender of the user in the form of a string:
            'Male', 'Female', or 'Other'
        RETURN:
            percentile - a float between 0.0 and 99.99 representing the
            fitness percentile rank among Norwegians
        '''
        try:
            TreadTableCategory = convertGenderToTreadTableCategory(gender)
            '''This query compares the treadRunTime across
            individuals in the database, and finds the row with the VO2 Max
            Score that is closest to the one inputted by the user, and returns
            the corresponding percentile'''
            query = """WITH cte
AS
(
SELECT percentile, ROW_NUMBER() over(order by abs(%s - %s)) as rw
FROM run
)SELECT *
FROM cte
WHERE rw<=1;"""
            queryResult = self.runQuery(query, (AsIs(TreadTableCategory), treadRuntime))
            percentile = int(queryResult[0][0])/100
            return percentile


        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None

    def getTreadRuntimeFromPercent(self, percentile, gender):
        '''
        Returns a treadmill runtime given a fitness percentile
        rank among Norwegians.
        PARAMETERS:
            percentile - a float between 0.0 and 99.99 representing the
            fitness percentile rank among Norwegians
            gender - the gender of the user in the form of a string:
            'Male', 'Female', or 'Other'
        RETURN:
            treadRunTime - a treadmill run time in seconds represented
            as an int
        '''
        try:
            percentile = convertFloatToPercentile(percentile)
            treadTableCategory = convertGenderToTreadTableCategory(gender)
            query = "SELECT %s FROM run WHERE percentile::float BETWEEN %s AND %s ORDER BY percentile;"
            queryResult = self.runQuery(query, (AsIs(treadTableCategory), percentile, percentile))
            treadRunTime = queryResult[0][0]
            return treadRunTime

        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None


if __name__ == '__main__':
    source = DataSource()
    print("Outputs percentiles from VO2 scores:")
    print(source.getPercentFromVO2(43.3769999999995, "Male"))
    print(source.getPercentFromVO2(43.3769999999995, "Female"))
    print(source.getPercentFromVO2(43.3769999999995, "Other"))
    print(type(source.getPercentFromVO2(43.3769999999995, "Other")))
    print("Outputs VO2 scores from percentiles:")
    print(source.getVO2FromPercent(0, "Male"))
    print(source.getVO2FromPercent(0, "Female"))
    print(source.getVO2FromPercent(0, "Other"))
    print(source.getVO2FromPercent(50, "Male"))
    print(source.getVO2FromPercent(50, "Female"))
    print(source.getVO2FromPercent(50, "Other"))
    print(type(source.getVO2FromPercent(50, "Other")))
    print("Outputs percentiles from Treadmill Runtimes:")
    print(source.getPercentFromTreadRuntime(600, "Male"))
    print(source.getPercentFromTreadRuntime(600, "Female"))
    print(source.getPercentFromTreadRuntime(600, "Other"))
    print(type(source.getPercentFromTreadRuntime(600, "Other")))
    print("Outputs Treadmill Runtimes from percentiles:")
    print(source.getTreadRuntimeFromPercent(50.0, "Male"))
    print(source.getTreadRuntimeFromPercent(50.0, "Female"))
    print(source.getTreadRuntimeFromPercent(50.0, "Other"))
    print(type(source.getTreadRuntimeFromPercent(50.0, "Other")))
