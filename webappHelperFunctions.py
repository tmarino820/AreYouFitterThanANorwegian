'''
This file contains helper functions used in
webapp.py in order to process user data
into the inputs for database queries. We
decided to put these functions in a seperate
file because their job of running tests and
processing the input from forms is at a
different layer of abstraction from
than the focus of webapp.py, which
takes in user data, runs queries, and
renders pages.

author(s): Antonio Marino, Jeremy Beckler
'''

import math


def convertMPerSecToMPerMin(mPerSec):
    '''
    Helper method that converts a speed quantity from meters per second
    into meters per minute
    PARAMETERS:
        mPerSec - a speed quantity in meters per second represented as
        a float
    RETURN:
        a speed quantity in meters per minute represented as a float
    '''
    return mPerSec*60

def convertKmPerHrToMPerMin(kmPerHr):
    '''
    Helper method that converts a speed quantity from kilometers per hour
    into meters per minute
    PARAMETERS:
        kmPerHr - a speed quantity in kilometers per hour represented as
        a float
    RETURN:
        a speed quantity in meters per minute represented as a float
    '''
    return kmPerHr*1000/60

def convertMiPerHrToMPerMin(miPerHr):
    '''
    Helper method that converts a speed quantity from miles per hour
    into meters per minute
    PARAMETERS:
        miPerHr - a speed quantity in miles per hour represented as
        a float
    RETURN:
        a speed quantity in meters per minute represented as a float
    '''
    return miPerHr*1609.34/60



def convertSpeedToMPerMin(speed, units):
    '''
    Helper method that converts a speed quantity into meters per minute
    PARAMETERS:
        speed - a speed quantity represented as a float
        units - the units of the corresponding speed quantity
        represented as a string
    RETURN:
        a speed quantity in meters per minute represented as a float
    '''
    if units == 'mi/hr':
        mPerMin = convertMiPerHrToMPerMin(speed)
    elif units == 'km/hr':
        mPerMin = convertKmPerHrToMPerMin(speed)
    elif units == 'm/sec':
        mPerMin = convertMPerSecToMPerMin(speed)
    return mPerMin

def convertMinToSec(min):
    '''
    Helper method that converts a time quantity from minutes
    into seconds
    PARAMETERS:
        min - a time quantity in minutes represented as
        a float
    RETURN:
        a time quantity in seconds represented as a float
    '''
    return min*60

def convertHrToSec(hr):
    '''
    Helper method that converts a time quantity from hours
    into seconds
    PARAMETERS:
        hr - a time quantity in hours represented as
        a float
    RETURN:
        a time quantity in seconds represented as a float
    '''
    return hr*60*60


def convertTimeToSec(time, units):
    '''
    Helper method that converts a time quantity into seconds
    PARAMETERS:
        time - a time quantity represented as a float
        units - the units of the corresponding time quantity
        represented as a string
    RETURN:
        a time quantity in seconds represented as a float
    '''
    if units == 'sec':
        sec = time
    elif units == 'min':
        sec = convertMinToSec(time)
    elif units == 'hr':
        sec = convertHrToSec(time)
    return sec



def convertMiToM(mi):
    '''
    Helper method that converts a distance quantity from miles
    into meters
    PARAMETERS:
        mi - a distance quantity in miles represented as
        a float
    RETURN:
        a distance quantity in meters represented as a float
    '''
    return mi*1609.34

def convertKmToM(km):
    '''
    Helper method that converts a distance quantity from kilometers
    into meters
    PARAMETERS:
        km - a distance quantity in kilometers represented as
        a float
    RETURN:
        a distance quantity in meters represented as a float
    '''
    return km*1000


def convertDistToM(dist, units):
    '''
    Helper method that converts a distance quantity into meters
    PARAMETERS:
        dist - a distance quantity represented as a float
        units - the units of the corresponding distance quantity
        represented as a string
    RETURN:
        a distance quantity in meters represented as a float
    '''
    if units == 'm':
        m = dist
    elif units == 'mi':
        m = convertMiToM(dist)
    elif units == 'km':
        m = convertKmToM(dist)
    return m



def jackDanielsEquation(speed, time):
    '''
    Helper method for computing the jack Daniels equation,
    which calculates the VO2 max score of individuals given
    the time and velocity description of their runs entered 
    through the form.
    PARAMETERS:
        speed - a speed quantity in meters per minute
        represented as a float
        time - a time quantity in seconds represented
        as a float
    RETURN:
        VO2Max - an estimated VO2 max score of the
        individual in mL/(kg∙min) represented
        as a float
    '''
    VO2 = -4.60 + 0.182258 * speed + 0.000104 * (speed**2)
    percentMax = 0.8 + 0.1894393 * math.exp(-0.012778 * time) + 0.2989558 * math.exp(-0.1932605 * time)
    VO2Max = VO2/percentMax
    if VO2Max < 0:
        VO2Max = 0
    return VO2Max

def jackDanielsEquationGivenVO2AndTime(vO2Max, time):
    '''
    Helper method for computing the jack Daniels equation,
    which calculates the velocity of individuals given
    the time and VO2 max score description of their runs
    entered through the form.
    PARAMETERS:
        speed - a speed quantity in meters per minute
        represented as a float
        VO2Max - an estimated VO2 max score of the
        individual in mL/(kg∙min) represented as a float
    RETURN:
        time - a time quantity in seconds represented
        as a float
    '''
    percentMax = 0.8 + 0.1894393 * math.exp(-0.012778 * time) + 0.2989558 * math.exp(-0.1932605 * time)
    vO2 = vO2Max*percentMax
    speed = ((-0.182258) + math.sqrt((0.182258**2) - 4*0.000104*(-4.60 - vO2)))/(2*0.000104)
    if speed < 0:
        speed = 0
    return speed


def calcTimeAndSpeed(result, validData):
    '''
    Helper method for computing the time and speed of an individual
    given two of the following descriptions of their runs: time,
    speed, and distance.
    PARAMETERS:
        result - the results of the form
        validData - a dictionary of bools representing the corresponding
        fields in which the user entered valid data
    RETURN:
        time, speed - the time and speed quantities converted into
        seconds and meters per minute, respectively represented as floats
    '''
    if (validData['time']) and (validData['speed']):
        time = convertTimeToSec(result['time'], result['timeUnits'])
        speed = convertSpeedToMPerMin(result['speed'], result['speedUnits'])
    elif (validData['distance']) and (validData['speed']):
        dist = convertDistToM(result['distance'], result['distanceUnits'])
        speed = convertSpeedToMPerMin(result['speed'], result['speedUnits'])
        time = (dist/speed)*60
    elif (validData['distance']) and (validData['time']):
        dist = convertDistToM(result['distance'], result['distanceUnits'])
        time = convertTimeToSec(result['time'], result['timeUnits'])
        speed = (dist/time)*60
    return time, speed

def calcTimeOrSpeedOrDistance(result, validData):
    '''
    Helper method for determining whether a distance, velocity, 
    or time was entered by the user. Then makes the appropriate 
    conversion.
    PARAMETERS:
        result - the results of the form
        validData - a dictionary of bools representing the corresponding
        fields in which the user entered valid data
    RETURN:
        timeOrSpeedOrDistance - the time(s), speed(m/min) or distance(m) quantity 
        converted into their appropriate units
    '''
    timeOrSpeedOrDistance = {}
    if (validData['distance']):
        timeOrSpeedOrDistance['distance'] = convertDistToM(result['distance'], result['distanceUnits'])
    elif (validData['time']):
        timeOrSpeedOrDistance['time'] = convertTimeToSec(result['time'], result['timeUnits'])
    elif (validData['speed']):
        timeOrSpeedOrDistance['speed'] = convertSpeedToMPerMin(result['speed'], result['speedUnits'])
    return timeOrSpeedOrDistance

def checkValidTimeDistanceOrSpeed(timeDistanceOrSpeed):
    '''
    Helper method for checking if the user entered a valid
    time, distance, or speed
    PARAMETERS:
        timeDistanceOrSpeed - the time, distance, or speed
        quantity entered by the user
    RETURN:
        None, but the function throws an error
        if the user entered a time that doesn't make sense.
    '''
    timeDistanceOrSpeed = float(timeDistanceOrSpeed)
    if timeDistanceOrSpeed < 0:
        print("Value error: Detected Negative Distance or Speed")
        raise ValueError
    return

def checkValidPercentile(percentile):
    '''
    Helper method for checking if the user entered a valid
    percentile.
    PARAMETERS:
        percentile - the percentile
        entered by the user
    RETURN:
        None, but the function throws an error
        if the user entered a percentile that doesn't make sense.
        i.e. negative or greater than or equal to 100.
    '''
    percentile = float(percentile)
    if (percentile < 0.00) or (percentile > 99.99):
        print("Value error: Detected Percentile not in range 0.00 to 99.99")
        raise ValueError
    return

def checkValidTreadmillRuntime(runtime):
    '''
    Helper method for checking if the user entered a valid
    treadmill runtime
    PARAMETERS:
        runtime - the maximal treadmill test runtime
        quantity entered by the user
    RETURN:
        None, but the function throws an error
        if the user entered a treadmill runtime that doesn't
        make sense.
    '''
    runtime = int(runtime)
    if runtime < 0:
        print("Value error: Detected Negative Treadmill Runtime")
        raise ValueError
    return

def checkValidVO2(vO2):
    '''
    Helper method for checking if the user entered a valid
    VO2 score
    PARAMETERS:
        vO2 - the VO2 Max Score
        entered by the user
    RETURN:
        None, but the function throws an error
        if the user entered a VO2 score that doesn't make sense.
    '''
    vO2 = float(vO2)
    if vO2 < 0:
        print("Value error: Detected Negative VO2 Max Score")
        raise ValueError
    return

def checkValidTimeUnits(units):
    '''
    Helper method for checking if the user entered valid
    time units
    PARAMETERS:
        units - the time units entered by the user
    RETURN:
        None, but the function throws an error
        if the user entered time units that don't make sense.
    '''
    units = str(units)
    if ((units != 'sec') and (units != 'min')) and (units != 'hr'):
        print("Time Units error: Detected Invalid Time Units")
        raise ValueError
    return

def checkValidDistanceUnits(units):
    '''
    Helper method for checking if the user entered valid
    distance units
    PARAMETERS:
        units - the distance units entered by the user
    RETURN:
        None, but the function throws an error
        if the user entered distance units that don't make sense.
    '''
    units = str(units)
    if ((units != 'm') and (units != 'mi')) and (units != 'km'):
        print("Distance Units error: Detected Invalid Distance Units")
        raise ValueError
    return

def checkValidSpeedUnits(units):
    '''
    Helper method for checking if the user entered valid
    speed units
    PARAMETERS:
        units - the speed units entered by the user
    RETURN:
        None, but the function throws an error
        if the user entered distance units that don't make sense.
    '''
    units = str(units)
    if ((units != 'mi/hr') and (units != 'km/hr')) and (units != 'm/sec'):
        print("Speed Units error: Detected Invalid Speed Units!")
        raise ValueError
    return

def buildValidDataDict(dataInField, validData, numInputs):
    '''
    Helper method for building a dictionary with the keys
    being the inputted data fields, and the values being
    whether or not it was valid data.
    PARAMETERS:
        dataInField - the data entered by the user in a given input
        field
        validData - a dictionary of bools with keys corresponding to
        fields for which the user has entered valid data
        numInputs - the number of valid inputs the user has already
        entered represented as an int
    RETURN:
        validData - an updated dictionary of bools with keys
        corresponding to fields for which the user has entered valid
        data
        numInputs - the updated number of valid inputs the user has
        entered represented as an int
    '''
    if (str(dataInField) != ""):
        checkValidTimeDistanceOrSpeed(dataInField)
        numInputs+=1
        valid = True
    else:
        valid = False
    return valid, numInputs

def buildValidDataDictForDataTreadmillRuntimeFromPercentile(dataInField, validData, numInputs):
    '''
    Helper method for building a dictionary with the keys
    being the inputted data fields, and the values being
    whether or not it was valid data for this calculator.
    PARAMETERS:
        dataInField - the data entered by the user in a given input
        field
        validData - a dictionary of bools with keys corresponding to
        fields for which the user has entered valid data
        numInputs - the number of valid inputs the user has already
        entered represented as an int
    RETURN:
        validData - an updated dictionary of bools with keys
        corresponding to fields for which the user has entered valid
        data
        numInputs - the updated number of valid inputs the user has
        entered represented as an int
    '''
    if (str(dataInField) != ""):
        checkValidPercentile(dataInField)
        numInputs+=1
        valid = True
    else:
        valid = False
    return valid, numInputs

def buildValidDataDictForDataPercentileFromTreadmillRuntime(dataInField, validData, numInputs):
    '''
    Helper method for building a dictionary with the keys
    being the inputted data fields, and the values being
    whether or not it was valid data for this calculator.
    PARAMETERS:
        dataInField - the data entered by the user in a given input
        field
        validData - a dictionary of bools with keys corresponding to
        fields for which the user has entered valid data
        numInputs - the number of valid inputs the user has already
        entered represented as an int
    RETURN:
        validData - an updated dictionary of bools with keys
        corresponding to fields for which the user has entered valid
        data
        numInputs - the updated number of valid inputs the user has
        entered represented as an int
    '''
    if (str(dataInField) != ""):
        checkValidTreadmillRuntime(dataInField)
        numInputs+=1
        valid = True
    else:
        valid = False
    return valid, numInputs

def buildValidDataDictForDataPercentileFromVO2(dataInField, validData, numInputs):
    '''
    Helper method for building a dictionary with the keys
    being the inputted data fields, and the values being
    whether or not it was valid data for this calculator.
    PARAMETERS:
        dataInField - the data entered by the user in a given input
        field
        validData - a dictionary of bools with keys corresponding to
        fields for which the user has entered valid data
        numInputs - the number of valid inputs the user has already
        entered represented as an int
    RETURN:
        validData - an updated dictionary of bools with keys
        corresponding to fields for which the user has entered valid
        data
        numInputs - the updated number of valid inputs the user has
        entered represented as an int
    '''
    if (str(dataInField) != ""):
        checkValidVO2(dataInField)
        numInputs+=1
        valid = True
    else:
        valid = False
    return valid, numInputs

def buildValidDataDictForDataRunFromPercentile(typeAndData, validData, numInputs):
    '''
    Helper method for building a dictionary with the keys
    being the inputted data fields, and the values being
    whether or not it was valid data for this calculator.
    PARAMETERS:
        typeAndData - a two element list containing the name of the 
        data and the data itself entered by the user
        validData - a dictionary of bools with keys corresponding to
        fields for which the user has entered valid data
        numInputs - the number of valid inputs the user has already
        entered represented as an int
    RETURN:
        validData - an updated dictionary of bools with keys
        corresponding to fields for which the user has entered valid
        data
        numInputs - the updated number of valid inputs the user has
        entered represented as an int
    '''
    if (str(typeAndData[1]) != ""):
        if typeAndData[0] == 'percent':
            checkValidPercentile(typeAndData[1])
        else:
            checkValidTimeDistanceOrSpeed(typeAndData[1])
        numInputs+=1
        valid = True
    else:
        valid = False
    return valid, numInputs

def checkValidUnits(result):
    '''
    Helper method for checking if all the fields have valid units
    PARAMETERS:
        result - the unformatted data retrieved by the form
        on the html page
    RETURN:
        None, but the function throws an error
        if the user entered distance units that don't make sense.
    '''
    checkValidTimeUnits(result['timeUnits'])
    checkValidDistanceUnits(result['distanceUnits'])
    checkValidSpeedUnits(result['speedUnits'])
    return

def checkValidQuantitiesForDataRun(result):
    '''
    Helper method for checking if valid quantites have been
    entered by the user on the dataRun.html page with route '/'
    PARAMETERS:
        result - the unformatted data retrieved by the form
        on the html page
    RETURN:
        validData - a dictionary of bools that show which fields
        of data have been correctly entered by the user
    '''
    numInputs = 0
    validData = {}
    for field in ('distance', 'time', 'speed'):
        validData[field], numInputs = buildValidDataDict(result[field], validData, numInputs)
    if numInputs != 2:
        print("Number of Inputs error:",
        "You must input two of the following values:",
        "distance, time, and/or speed")
        raise ValueError
    return validData

def checkValidQuantitiesForDataTreadmillRuntimeFromPercentile(result):
    '''
    Helper method for checking if valid quantites have been
    entered by the user on the DataTreadmillRuntimeFromPercentile.html 
    page with route '/DataTreadmillRuntimeFromPercentile'
    PARAMETERS:
        result - the unformatted data retrieved by the form
        on the DataTreadmillRuntimeFromPercentile.html page
    RETURN:
        validData - a dictionary of bools that show which fields
        of data have been correctly entered by the user
    '''
    numInputs = 0
    validData = {}
    validData['percent'], numInputs = buildValidDataDictForDataTreadmillRuntimeFromPercentile(result['percent'], validData, numInputs)
    if numInputs != 1:
        print("Number of Inputs error:",
        "You must input a percentile")
        raise ValueError
    return validData

def checkValidQuantitiesForDataPercentileFromTreadmillRuntime(result):
    '''
    Helper method for checking if valid quantites have been
    entered by the user on the DataPercentileFromTreadmillRuntime.html 
    page with route '/DataPercentileFromTreadmillRuntime'
    PARAMETERS:
        result - the unformatted data retrieved by the form
        on the DataPercentileFromTreadmillRuntime.html page
    RETURN:
        validData - a dictionary of bools that show which fields
        of data have been correctly entered by the user
    '''
    numInputs = 0
    validData = {}
    validData['treadRuntime'], numInputs = buildValidDataDictForDataPercentileFromTreadmillRuntime(result['treadRuntime'], validData, numInputs)
    if numInputs != 1:
        print("Number of Inputs error:",
        "You must input a percentile")
        raise ValueError
    return validData


def checkValidQuantitiesForDataVO2FromPercentile(result):
    '''
    Helper method for checking if valid quantites have been
    entered by the user on the DataVO2FromPercentile.html page 
    with route '/DataVO2FromPercentile'
    PARAMETERS:
        result - the unformatted data retrieved by the form
        on the DataVO2FromPercentile.html page
    RETURN:
        validData - a dictionary of bools that show which fields
        of data have been correctly entered by the user
    '''
    numInputs = 0
    validData = {}
    validData['percent'], numInputs = buildValidDataDictForDataTreadmillRuntimeFromPercentile(result['percent'], validData, numInputs)
    if numInputs != 1:
        print("Number of Inputs error:",
        "You must input a percentile")
        raise ValueError
    return validData

def checkValidQuantitiesForDataPercentileFromVO2(result):
    '''
    Helper method for checking if valid quantites have been
    entered by the user on the DataPercentileFromVO2.html page 
    with route '/DataPercentileFromVO2'
    PARAMETERS:
        result - the unformatted data retrieved by the form
        on the DataPercentileFromVO2.html page
    RETURN:
        validData - a dictionary of bools that show which fields
        of data have been correctly entered by the user
    '''
    numInputs = 0
    validData = {}
    validData['vO2Max'], numInputs = buildValidDataDictForDataPercentileFromVO2(result['vO2Max'], validData, numInputs)
    if numInputs != 1:
        print("Number of Inputs error:",
        "You must input a percentile")
        raise ValueError
    return validData

def checkValidQuantitiesForDataRunFromPercentile(result):
    '''
    Helper method for checking if valid quantites have been
    entered by the user on the DataRunFromPercentile.html page 
    with route '/DataRunFromPercentile'
    PARAMETERS:
        result - the unformatted data retrieved by the form
        on the DataRunFromPercentile.html page
    RETURN:
        validData - a dictionary of bools that show which fields
        of data have been correctly entered by the user
    '''
    numInputs = 0
    validData = {}
    for field in ('percent', 'time'):
        validData[field], numInputs = buildValidDataDictForDataRunFromPercentile([field, result[field]], validData, numInputs)
    if numInputs != 2:
        print("Number of Inputs error:",
        "You must input a percentile")
        raise ValueError
    return validData

def checkValidGender(result):
    '''
    Helper function for checking if the user entered a
    valid answer for gender.
    PARAMETERS:
        result - the unformatted data retrieved by the form
    RETURN:
        None, but throws an error if the gender is not a
        valid answer
    '''
    gender = str(result['gender'])
    if ((gender != 'Male') and (gender != 'Female')) and (gender != 'Other'):
        print("Gender error: Detected Invalid Gender Input")
        raise ValueError
    return


def checkValidInputsForDataRun(result):
    '''
    Helper function for checking if the user entered a
    valid data on the dataRun.html page with route '/'
    PARAMETERS:
        result - the unformatted data retrieved by the form
        on the dataRun.html page
    RETURN:
        validData - a dictionary of bools that show which fields
        of data have been correctly entered by the user, but
        throws an error if any of the entered data is invalid
    '''
    validData = checkValidQuantitiesForDataRun(result)
    checkValidUnits(result)
    checkValidGender(result)
    return validData

def checkValidInputsForDataTreadmillRuntimeFromPercentile(result):
    '''
    Helper function for checking if the user entered a
    valid data on the DataTreadmillRuntimeFromPercentile.html
    page with route '/DataTreadmillRuntimeFromPercentile'
    PARAMETERS:
        result - the unformatted data retrieved by the form
        on the DataTreadmillRuntimeFromPercentile.html page
    RETURN:
        validData - a dictionary of bools that show which fields
        of data have been correctly entered by the user, but
        throws an error if any of the entered data is invalid
    '''
    validData = checkValidQuantitiesForDataTreadmillRuntimeFromPercentile(result)
    checkValidGender(result)
    return validData

def checkValidInputsForDataPercentileFromTreadmillRuntime(result):
    '''
    Helper function for checking if the user entered a
    valid data on the DataPercentileFromTreadmillRuntime.html
    page with route '/DataPercentileFromTreadmillRuntime'
    PARAMETERS:
        result - the unformatted data retrieved by the form
        on the DataPercentileFromTreadmillRuntime.html page
    RETURN:
        validData - a dictionary of bools that show which fields
        of data have been correctly entered by the user, but
        throws an error if any of the entered data is invalid
    '''
    validData = checkValidQuantitiesForDataPercentileFromTreadmillRuntime(result)
    checkValidGender(result)
    return validData

def checkValidInputsForDataVO2FromPercentile(result):
    '''
    Helper function for checking if the user entered a
    valid data on the DataVO2FromPercentile.html page 
    with route '/DataVO2FromPercentile'
    PARAMETERS:
        result - the unformatted data retrieved by the form
        on the DataVO2FromPercentile.html page
    RETURN:
        validData - a dictionary of bools that show which fields
        of data have been correctly entered by the user, but
        throws an error if any of the entered data is invalid
    '''
    validData = checkValidQuantitiesForDataVO2FromPercentile(result)
    checkValidGender(result)
    return validData

def checkValidInputsForDataPercentileFromVO2(result):
    '''
    Helper function for checking if the user entered a
    valid data on the DataPercentileFromVO2.html page
    with route '/DataPercentileFromVO2'
    PARAMETERS:
        result - the unformatted data retrieved by the form
        on the DataPercentileFromVO2.html page
    RETURN:
        validData - a dictionary of bools that show which fields
        of data have been correctly entered by the user, but
        throws an error if any of the entered data is invalid
    '''
    validData = checkValidQuantitiesForDataPercentileFromVO2(result)
    checkValidGender(result)
    return validData

def checkValidInputsForDataRunFromPercentile(result):
    '''
    Helper function for checking if the user entered a
    valid data on the DataRunFromPercentile.html page
    with route '/DataRunFromPercentile'
    PARAMETERS:
        result - the unformatted data retrieved by the form
        on the DataRunFromPercentile.html page
    RETURN:
        validData - a dictionary of bools that show which fields
        of data have been correctly entered by the user, but
        throws an error if any of the entered data is invalid
    '''
    validData = checkValidQuantitiesForDataRunFromPercentile(result)
    checkValidGender(result)
    return validData

def castTypesOnInputsForDataRun(result, validData):
    '''
    Helper function that forces the data entered by the
    user to be a certain type before we begin performing
    calculations and queries on that data
    PARAMETERS:
        result - the unformatted data retrieved by the form
        on the dataRun.html page
        validData - a dictionary of bools that show which fields
        of data have been correctly entered by the user
    RETURN:
        newResult - the formatted data retrieved by the form
        on the dataRun.html page with each field forced to be
        a non-executable type
    '''
    newResult = {}
    for field in validData.keys():
        if validData[field] == True:
            newResult[field] = float(result[field])
    for field in ('distanceUnits', 'timeUnits', 'speedUnits', 'gender'):
        newResult[field] = str(result[field])
    return newResult

def castTypesOnInputsForDataTreadmillRuntimeFromPercentile(result, validData):
    '''
    Helper function that forces the data entered by the
    user to be a certain type before we begin performing
    calculations and queries on that data
    PARAMETERS:
        result - the unformatted data retrieved by the form
        on the DataTreadmillRuntimeFromPercentile.html page
        validData - a dictionary of bools that show which fields
        of data have been correctly entered by the user
    RETURN:
        newResult - the formatted data retrieved by the form
        on the DataTreadmillRuntimeFromPercentile.html page with each field forced to be
        a non-executable type
    '''
    newResult = {}
    for field in validData.keys():
        if validData[field] == True:
            newResult[field] = float(result[field])
    newResult['gender'] = str(result['gender'])
    return newResult

def castTypesOnInputsForDataPercentileFromTreadmillRuntime(result, validData):
    '''
    Helper function that forces the data entered by the
    user to be a certain type before we begin performing
    calculations and queries on that data
    PARAMETERS:
        result - the unformatted data retrieved by the form
        on the DataPercentileFromTreadmillRuntime.html page
        validData - a dictionary of bools that show which fields
        of data have been correctly entered by the user
    RETURN:
        newResult - the formatted data retrieved by the form
        on the DataPercentileFromTreadmillRuntime.html page with each field forced to be
        a non-executable type
    '''
    newResult = {}
    for field in validData.keys():
        if validData[field] == True:
            newResult[field] = int(result[field])
    newResult['gender'] = str(result['gender'])
    return newResult

def castTypesOnInputsForDataVO2FromPercentile(result, validData):
    '''
    Helper function that forces the data entered by the
    user to be a certain type before we begin performing
    calculations and queries on that data
    PARAMETERS:
        result - the unformatted data retrieved by the form
        on the DataVO2FromPercentile.html page
        validData - a dictionary of bools that show which fields
        of data have been correctly entered by the user
    RETURN:
        newResult - the formatted data retrieved by the form
        on the DataVO2FromPercentile.html page with each field forced to be
        a non-executable type
    '''
    newResult = {}
    for field in validData.keys():
        if validData[field] == True:
            newResult[field] = float(result[field])
    newResult['gender'] = str(result['gender'])
    return newResult

def castTypesOnInputsForDataPercentileFromVO2(result, validData):
    '''
    Helper function that forces the data entered by the
    user to be a certain type before we begin performing
    calculations and queries on that data
    PARAMETERS:
        result - the unformatted data retrieved by the form
        on the DataPercentileFromVO2.html page
        validData - a dictionary of bools that show which fields
        of data have been correctly entered by the user
    RETURN:
        newResult - the formatted data retrieved by the form
        on the DataPercentileFromVO2.html page with each field forced to be
        a non-executable type
    '''
    newResult = {}
    for field in validData.keys():
        if validData[field] == True:
            newResult[field] = float(result[field])
    newResult['gender'] = str(result['gender'])
    return newResult

def castTypesOnInputsForDataRunFromPercentile(result, validData):
    '''
    Helper function that forces the data entered by the
    user to be a certain type before we begin performing
    calculations and queries on that data
    PARAMETERS:
        result - the unformatted data retrieved by the form
        on the DataRunFromPercentile.html page
        validData - a dictionary of bools that show which fields
        of data have been correctly entered by the user
    RETURN:
        newResult - the formatted data retrieved by the form
        on the DataRunFromPercentile.html page with each field forced to be
        a non-executable type
    '''
    newResult = {}
    for field in result.keys():
        newResult[field] = str(result[field])
    for field in validData.keys():
        if validData[field] == True:
            newResult[field] = float(result[field])
    newResult['gender'] = str(result['gender'])
    return newResult

def outputTime(validData, result):
    '''
    Helper function to output the time input of
    any given calculator.
    PARAMETERS:
        validData - a dictionary of bools that show which fields
        of data have been correctly entered by the user
        result - the unformatted data retrieved by the form
        on the DataRunFromPercentile.html page
    RETURN:
        time - the inputted amount for time given as a float in seconds
    '''
    for key in validData.keys():
        if validData[key] == True:
            label = key
            if key == 'time':
                time = convertTimeToSec(result[key], result[key+'Units'])
    return time

def processInputDataForDataRun(result):
    '''
    Helper method for processing the input data from
    the dataRun.html page with route '/'
    PARAMETERS:
        result - the unformatted data retrieved by the form
        on the dataRun.html page
        validData - a dictionary of bools that show which fields
        of data have been correctly entered by the user
    RETURN:
        VO2Max, gender - the estimated VO2 Max score and
        gender of the user, which can be fed as parameters
        to a query
    '''
    validData = checkValidInputsForDataRun(result)
    result = castTypesOnInputsForDataRun(result, validData)
    time, velocity = calcTimeAndSpeed(result, validData)
    VO2Max = jackDanielsEquation(velocity, time)
    gender = result['gender']
    return VO2Max, gender

def processInputDataForDataRunFromPercentile(result):
    '''
    Helper method for processing the input data from
    the DataRunFromPercentile.html page with route '/DataRunFromPercentile'
    PARAMETERS:
        result - the unformatted data retrieved by the form
        on the DataRunFromPercentile.html page
        validData - a dictionary of bools that show which fields
        of data have been correctly entered by the user
    RETURN:
        VO2Max, gender - the estimated VO2 Max score and
        gender of the user, which can be fed as parameters
        to a query
    '''
    validData = checkValidInputsForDataRunFromPercentile(result)
    result = castTypesOnInputsForDataRunFromPercentile(result, validData)
    percent = result['percent']
    gender = result['gender']
    time = outputTime(validData, result)
    return time, percent, gender

def processOutputDataForDataRunFromPercentile(vO2Max, time):
    '''
    Helper method for processing the input data from
    the DataRunFromPercentile.html page with route '/DataRunFromPercentile'
    PARAMETERS:
        result - the unformatted data retrieved by the form
        on the DataRunFromPercentile.html page
        validData - a dictionary of bools that show which fields
        of data have been correctly entered by the user
    RETURN:
        VO2Max, gender - the estimated VO2 Max score and
        gender of the user, which can be fed as parameters
        to a query
    '''
    speed = jackDanielsEquationGivenVO2AndTime(vO2Max, time)
    distance = (time/60)*speed
    return speed, time, distance


def processInputDataForDataPercentileFromVO2(result):
    '''
    Helper method for processing the input data from
    the DataPercentileFromVO2.html page with route '/DataPercentileFromVO2'
    PARAMETERS:
        result - the unformatted data retrieved by the form
        on the DataPercentileFromVO2.html page
        validData - a dictionary of bools that show which fields
        of data have been correctly entered by the user
    RETURN:
        VO2Max, gender - the estimated VO2 Max score and
        gender of the user, which can be fed as parameters
        to a query
    '''
    validData = checkValidInputsForDataPercentileFromVO2(result)
    result = castTypesOnInputsForDataPercentileFromVO2(result, validData)
    vO2Max = result['vO2Max']
    gender = result['gender']
    return vO2Max, gender


def processInputDataForDataVO2FromPercentile(result):
    '''
    Helper method for processing the input data from
    the DataVO2FromPercentile.html page with route '/DataVO2FromPercentile'
    PARAMETERS:
        result - the unformatted data retrieved by the form
        on the DataVO2FromPercentile.html page
        validData - a dictionary of bools that show which fields
        of data have been correctly entered by the user
    RETURN:
        VO2Max, gender - the estimated VO2 Max score and
        gender of the user, which can be fed as parameters
        to a query
    '''
    validData = checkValidInputsForDataVO2FromPercentile(result)
    result = castTypesOnInputsForDataVO2FromPercentile(result, validData)
    percentile = result['percent']
    gender = result['gender']
    return percentile, gender


def processInputDataForDataPercentileFromTreadmillRuntime(result):
    '''
    Helper method for processing the input data from
    the DataPercentileFromTreadmillRuntime.html page with route '/DataPercentileFromTreadmillRuntime'
    PARAMETERS:
        result - the unformatted data retrieved by the form
        on the DataPercentileFromTreadmillRuntime.html page
        validData - a dictionary of bools that show which fields
        of data have been correctly entered by the user
    RETURN:
        VO2Max, gender - the estimated VO2 Max score and
        gender of the user, which can be fed as parameters
        to a query
    '''
    validData = checkValidInputsForDataPercentileFromTreadmillRuntime(result)
    result = castTypesOnInputsForDataPercentileFromTreadmillRuntime(result, validData)
    treadmillRuntime = result['treadRuntime']
    gender = result['gender']
    return treadmillRuntime, gender



def processInputDataForDataTreadmillRuntimeFromPercentile(result):
    '''
    Helper method for processing the input data from
    the DataTreadmillRuntimeFromPercentile.html page with route '/DataTreadmillRuntimeFromPercentile'
    PARAMETERS:
        result - the unformatted data retrieved by the form
        on the DataTreadmillRuntimeFromPercentile.html page
        validData - a dictionary of bools that show which fields
        of data have been correctly entered by the user
    RETURN:
        VO2Max, gender - the estimated VO2 Max score and
        gender of the user, which can be fed as parameters
        to a query
    '''
    validData = checkValidInputsForDataTreadmillRuntimeFromPercentile(result)
    result = castTypesOnInputsForDataTreadmillRuntimeFromPercentile(result, validData)
    percentile = result['percent']
    gender = result['gender']
    return percentile, gender
