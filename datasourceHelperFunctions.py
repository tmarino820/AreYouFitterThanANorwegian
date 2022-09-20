'''
This file contains helper functions used in
datasource.py in order to process the inputs
for database methods into sql queries. We
decided to put these functions in a seperate
file because their job converting inputs is
at a different layer of abstraction from
than the focus of datasource.py, which
takes in parameters and executes queries.

author(s): Antonio Marino, Jeremy Beckler
'''


def convertFloatToPercentile(percentile):
    '''
    Helper function that converts a Float
    to a percentile -- an intger -- in the
    format used to index into the table
    PARAMETERS:
        percentile - a float between 0.0 and 99.99 representing the
        fitness percentile rank among Norwegians
    RETURN:
        an integer between 0 and 9999 representing the
        fitness percentile rank among Norwegians used
        to index into the table
    '''
    percentile = int(100*percentile)
    if percentile == 10000:
        percentile = 9999
    if not ((percentile >= 0) and (percentile <= 9999)):
        raise ValueError('Incorrect float value representing a percentile!')
    return percentile

def convertGenderToTreadTableCategory(gender):
    '''
    Helper function that converts the gender of the user
    into the appropriate column for treadmill runtime
    PARAMETERS:
        gender - the gender of the user in the form of a string:
        'Male', 'Female', or 'Other'
    RETURN:
        a string representing the treadmill runtime category for
        indexing into the table
    '''
    if gender == 'Male':
        gender = 'Men_Treadmill_run_time'
    elif gender == 'Female':
        gender = 'Women_Treadmill_run_time'
    else:
        gender = 'Combined_Treadmill_run_time'
    return gender

def convertGenderToVO2TableCategory(gender):
    '''
    Helper function that converts the gender of the user
    into the appropriate column for VO2 Score
    PARAMETERS:
        gender - the gender of the user in the form of a string:
        'Male', 'Female', or 'Other'
    RETURN:
        a string representing the VO2 score category for
        indexing into the table
    '''
    if gender == 'Male':
        gender = 'Men_Est_VO2peak'
    elif gender == 'Female':
        gender = 'Women_Est_VO2peak'
    else:
        gender = 'Combined_Est_VO2peak'
    return gender
