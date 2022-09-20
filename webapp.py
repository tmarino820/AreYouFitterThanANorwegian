'''
A web application using Flask. Allows users to compare their level of
physical fitness to that of Norwegians.

author: Antonio Marino, Jeremy Beckler
CS 257, Winter 2022
'''

import flask
from flask import render_template, request
import json
import sys
from datasource import DataSource
from webappHelperFunctions import *

#Here, we create a Datasource object and use it to make calls in dataSource.py
database = DataSource()
app = flask.Flask(__name__)
# This line tells the web browser to *not* cache any of the files.
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/errorMessage', methods=['POST', 'GET'])
def errorMessage():
    '''
    Error page for our home page calclator, dataPercentileFromRun.
    Displays a short message to the users that they entered
    something incorrectly and to read the instructions again.
    '''
    if request.method == 'POST':
        result = request.form
        try:
            return render_template('errorMessagePercentileFromRun.html',
            distance=str(result['distance']), time=str(result['time']),
            speed=str(result['speed']),
            distanceUnits=str(result['distanceUnits']),
            timeUnits=str(result['timeUnits']),
            speedUnits=str(result['speedUnits']), gender=str(result['gender']))
        except:
            pass
    return render_template('errorMessagePercentileFromRun.html')

@app.route('/errorMessagePercentileFromTreadmillRuntime', methods=['POST', 'GET'])
def errorMessagePercentileFromTreadmillRuntime():
    '''
    Displays a short message to the users that they entered
    something incorrectly and to read the instructions again.
    '''
    if request.method == 'POST':
        result = request.form
        try:
            return render_template('errorMessagePercentileFromTreadmillRuntime.html',
            distance=str(result['distance']), time=str(result['time']),
            speed=str(result['speed']),
            distanceUnits=str(result['distanceUnits']),
            timeUnits=str(result['timeUnits']),
            speedUnits=str(result['speedUnits']), gender=str(result['gender']))
        except:
            pass
    return render_template('errorMessagePercentileFromTreadmillRuntime.html')

@app.route('/errorMessagePercentileFromVO2', methods=['POST', 'GET'])
def errorMessagePercentileFromVO2():
    '''
    Displays a short message to the users that they entered
    something incorrectly and to read the instructions again.
    '''
    if request.method == 'POST':
        result = request.form
        try:
            return render_template('errorMessagePercentileFromVO2.html',
            distance=str(result['distance']), time=str(result['time']),
            speed=str(result['speed']),
            distanceUnits=str(result['distanceUnits']),
            timeUnits=str(result['timeUnits']),
            speedUnits=str(result['speedUnits']), gender=str(result['gender']))
        except:
            pass
    return render_template('errorMessagePercentileFromVO2.html')

@app.route('/errorMessageRunFromPercentile', methods=['POST', 'GET'])
def errorMessageRunFromPercentile():
    '''
    Displays a short message to the users that they entered
    something incorrectly and to read the instructions again.
    '''
    if request.method == 'POST':
        result = request.form
        try:
            return render_template('errorMessageRunFromPercentile.html',
            distance=str(result['distance']), time=str(result['time']),
            speed=str(result['speed']),
            distanceUnits=str(result['distanceUnits']),
            timeUnits=str(result['timeUnits']),
            speedUnits=str(result['speedUnits']), gender=str(result['gender']))
        except:
            pass
    return render_template('errorMessageRunFromPercentile.html')

@app.route('/errorMessageTreadmillRuntimeFromPercentile', methods=['POST', 'GET'])
def errorMessageTreadmillRuntimeFromPercentile():
    '''
    Displays a short message to the users that they entered
    something incorrectly and to read the instructions again.
    '''
    if request.method == 'POST':
        result = request.form
        try:
            return render_template('errorMessagePeerrorMessageTreadmillRuntimeFromPercentilercentileFromTreadmillRuntime.html',
            distance=str(result['distance']), time=str(result['time']),
            speed=str(result['speed']),
            distanceUnits=str(result['distanceUnits']),
            timeUnits=str(result['timeUnits']),
            speedUnits=str(result['speedUnits']), gender=str(result['gender']))
        except:
            pass
    return render_template('errorMessageTreadmillRuntimeFromPercentile.html')

@app.route('/errorMessageVO2FromPercentile', methods=['POST', 'GET'])
def errorMessageVO2FromPercentile():
    '''
    Displays a short message to the users that they entered
    something incorrectly and to read the instructions again.
    '''
    if request.method == 'POST':
        result = request.form
        try:
            return render_template('errorMessageVO2FromPercentile.html',
            distance=str(result['distance']), time=str(result['time']),
            speed=str(result['speed']),
            distanceUnits=str(result['distanceUnits']),
            timeUnits=str(result['timeUnits']),
            speedUnits=str(result['speedUnits']), gender=str(result['gender']))
        except:
            pass
    return render_template('errorMessageVO2FromPercentile.html')



@app.route('/')
def dataPercentileFromRun():
    '''
    Renders the homepage which is a simple calculator where
    users can enter a description of their runs.
    '''
    return render_template('dataPercentileFromRun.html')

@app.route('/dataRunFromPercentile')
def dataRunFromPercentile():
    '''
    A calculator where users can enter a
    percentile and the corresponding results page will
    show how fast Norwegians in that percentile can
    perform their runs.
    '''
    return render_template('dataRunFromPercentile.html')

@app.route('/dataPercentileFromVO2')
def dataPercentileFromVO2():
    '''
    A calculator where users can enter a
    VO2 Max Score and the corresponding results page
    will roughly show the percentile rank among
    Norwegians based on that VO2 Max Score.
    '''
    return render_template('dataPercentileFromVO2.html')

@app.route('/dataVO2FromPercentile')
def dataVO2FromPercentile():
    '''
    A calculator where users can enter a
    percentile and the corresponding results page
    will roughly show the VO2 Max Score of Norwegians
    in that percentile rank.
    '''
    return render_template('dataVO2FromPercentile.html')

@app.route('/dataPercentileFromTreadmillRuntime')
def dataPercentileFromTreadmillRuntime():
    '''
    A calculator where users can enter a
    runtime on the Maximal Treadmill Test and the
    corresponding results page will roughly show the
    percentile rank among Norwegians of individuals
    with that runtime.
    '''
    return render_template('dataPercentileFromTreadmillRuntime.html')

@app.route('/dataTreadmillRuntimeFromPercentile')
def dataTreadmillRuntimeFromPercentile():
    '''
    A calculator where users can enter a
    percentile and the corresponding results page
    will roughly show the runtime on the Maximal
    Treadmill Test of Norwegians in that percentile.
    '''
    return render_template('dataTreadmillRuntimeFromPercentile.html')

@app.route('/results', methods=['POST', 'GET'])
def queryPercentileFromRun():
    '''
    This route is the results page for the homepage calculator.
    It displays information about the user's percentile rank among
    Norwegians, estimated VO2 max score, and general skill level.
    The percentile rank among Norwegians means roughly the percentage
    of Norwegians that the user can outrun; the estimated VO2 max score
    is a measure of cardiovascular endurance; and the general skill
    level is just a classification between Beginner and Elite as well
    as a score out of five stars, which allows users to visualize how
    well they stack up overall against Norwegians.
    '''
    if request.method == 'POST':
        result = request.form
        try:
            vO2Max, gender = processInputDataForDataRun(result)
            Percentile = database.getPercentFromVO2(vO2Max, gender)
        except:
            return errorMessage()
    return render_template('resultsPercentileFromRun.html', distance=str(result['distance']),
    time=str(result['time']), speed=str(result['speed']), percent=Percentile,
    distanceUnits=str(result['distanceUnits']),
    timeUnits=str(result['timeUnits']), speedUnits=str(result['speedUnits']),
    vo2max=round(vO2Max, 3), gender=gender)

@app.route('/resultsRunFromPercentile', methods=['POST', 'GET'])
def queryRunFromPercentile():
    '''
    This route is the results page for the homepage calculator.
    It displays information about the user's percentile rank among
    Norwegians, estimated VO2 max score, and general skill level.
    The percentile rank among Norwegians means roughly the percentage
    of Norwegians that the user can outrun; the estimated VO2 max score
    is a measure of cardiovascular endurance; and the general skill
    level is just a classification between Beginner and Elite as well
    as a score out of five stars, which allows users to visualize how
    well they stack up overall against Norwegians.
    '''
    if request.method == 'POST':
        result = request.form
        try:
            time, percent, gender = processInputDataForDataRunFromPercentile(result)
            vO2Max = database.getVO2FromPercent(percent, gender)
            speed, time, distance = processOutputDataForDataRunFromPercentile(vO2Max, time)
        except:
            return errorMessageRunFromPercentile()
    return render_template('resultsRunFromPercentile.html',
    time=str(result['time']), percent=percent,
    timeUnits=str(result['timeUnits']),
    resultingDistance=round(distance, 3), resultingTime=round(time), resultingSpeed=round(speed, 0),
    vo2max=round(vO2Max, 3), gender=gender)

@app.route('/resultsPercentileFromVO2', methods=['POST', 'GET'])
def queryPercentileFromVO2():
    '''
    Results page that
    will roughly show the percentile rank among
    Norwegians based on an inputted VO2 Max Score.
    '''
    if request.method == 'POST':
        result = request.form
        try:
            vO2Max, gender = processInputDataForDataPercentileFromVO2(result)
            percent = database.getPercentFromVO2(vO2Max, gender)
        except:
            return errorMessagePercentileFromVO2()
    return render_template('resultsPercentileFromVO2.html', percent=percent,
    vO2Max=round(vO2Max, 3), gender=gender)

@app.route('/resultsVO2FromPercentile', methods=['POST', 'GET'])
def queryVO2FromPercentile():
    '''
    A results page that will
    roughly show the VO2 Max Score of Norwegians
    in an inputted percentile.
    '''
    if request.method == 'POST':
        result = request.form
        try:
            percent, gender = processInputDataForDataVO2FromPercentile(result)
            vO2Max = database.getVO2FromPercent(percent, gender)
        except:
            return errorMessageVO2FromPercentile()
    return render_template('resultsVO2FromPercentile.html', percent=percent,
    vo2max=round(vO2Max, 3), gender=gender)

@app.route('/resultsPercentileFromTreadmillRuntime', methods=['POST', 'GET'])
def queryPercentileFromTreadmillRuntime():
    '''
    This will be the results page that will roughly
    show the percentile rank among Norwegians of
    individuals with an inputted Maximal Treadmill
    runtime.
    '''
    if request.method == 'POST':
        result = request.form
        try:
            treadRuntime, gender = processInputDataForDataPercentileFromTreadmillRuntime(result)
            percent = database.getPercentFromTreadRuntime(treadRuntime, gender)
        except:
            return errorMessagePercentileFromTreadmillRuntime()
    return render_template('resultsPercentileFromTreadmillRuntime.html', percent=percent,
    treadRuntime=treadRuntime, gender=gender)

@app.route('/resultsTreadmillRuntimeFromPercentile', methods=['POST', 'GET'])
def queryTreadmillRuntimeFromPercentile():
    '''
    This will be the results page that
    will roughly show the runtime on the Maximal
    Treadmill Test of Norwegians in an inputted
    percentile.
    '''
    if request.method == 'POST':
        result = request.form
        try:
            percent, gender = processInputDataForDataTreadmillRuntimeFromPercentile(result)
            treadRuntime = database.getTreadRuntimeFromPercent(percent, gender)
        except:
            return errorMessageTreadmillRuntimeFromPercentile()
    return render_template('resultsTreadmillRuntimeFromPercentile.html', treadRuntime=treadRuntime,
     percent=percent, gender=gender)

@app.route('/about')
def about():
    '''
    This will be the about page that
    will describe the source of the data,
    how the data was collected, and the
    licensing information associated with
    the data.
    '''
    return render_template('about.html')

@app.route('/standards')
def standards():
    '''
    This will be the standards page that
    will have a screenshot of the original
    data we generated our data from, and a
    brief description.
    '''
    return render_template('standards.html')


'''
Run the program by typing 'python3 localhost [port]', where [port] is one of
the port numbers you were sent by my earlier this term.
'''
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()
    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
