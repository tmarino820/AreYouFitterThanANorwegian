"""
dataGeneration.py
author: Antonio Marino

This file includes the python code used
to normalize the Norwegian dataset.
I used the pandas library in python
along with two other libraries in order
to generate 10,000 'synthetic' Norwegians
uniformly across percentiles.
"""


import random
import numpy
import pandas as pd


def generateDataBetween5(df, domain, startingPoint, percentile):
    # generates data across rows between a range of percentiles
    start, stop = domain[0], domain[1]
    slope = (df[stop] - df[start]) / (5)
    for i in range(500):
        df[percentile] = startingPoint
        df[percentile][3] = int(df[percentile][3])
        df[percentile][13] = int(df[percentile][13])
        startingPoint += (slope) * (5 / 500)
        percentile += 1
    return df

def generateDataBetween10(df, domain, startingPoint, percentile):
    # generates data across rows between a range of percentiles
    start, stop = domain[0], domain[1]
    slope = (df[stop] - df[start]) / (10)
    for i in range(1000):
        df[percentile] = startingPoint
        df[percentile][3] = int(df[percentile][3])
        df[percentile][13] = int(df[percentile][13])
        startingPoint += (slope) * (5 / 500)
        percentile += 1
    return df

def generateData0To5ThPercentiles(df):
    # generate 500 values between 0 and 5
    startingPoint = df[' 5th'] - (df[' 10th'] - df[' 5th'])
    percentile = int(0)
    domain = (' 5th', ' 10th')
    df = generateDataBetween5(df, domain, startingPoint, percentile)
    return df

def generateData5To10ThPercentiles(df):
    # generate 500 values between 5 and 10
    startingPoint = df[" 5th"]
    percentile = int(500)
    domain = (" 5th", " 10th")
    df = generateDataBetween5(df, domain, startingPoint, percentile)
    return df

def generateData10To90ThPercentiles(df):
    # generate 1000 values between 10 and 20,
    # 20 and 30, ..., 80 and 90
    percentile = int(1000)
    listOfDomains = [(" 10th", " 20th"), (" 20th", " 30th"), (" 30th", " 40th"), (" 40th", " 50th"), (" 50th", " 60th"), (" 60th", " 70th"), (" 70th", " 80th"), (" 80th", " 90th")]
    for i in range(8):
        domain = listOfDomains[i]
        startingPoint = df[domain[0]]
        df = generateDataBetween10(df, domain, startingPoint, percentile)
        percentile += 1000
    return df

def generateData90To95ThPercentiles(df):
    # generate 500 values between 90 and 95
    startingPoint = df[" 90th"]
    percentile = int(9000)
    domain = (" 90th", " 95th")
    df = generateDataBetween5(df, domain, startingPoint, percentile)
    return df

def generateData95To100ThPercentiles(df):
    # generate 500 values between 95 and 100
    percentile = int(9500)
    startingPoint = df[" 95th"]
    domain = (" 90th", " 95th")
    df = generateDataBetween5(df, domain, startingPoint, percentile)
    return df

def generateValuesInRow(df):
    #generates data between the 0th to 100th percentiles
    df = generateData0To5ThPercentiles(df)
    df = generateData5To10ThPercentiles(df)
    df = generateData10To90ThPercentiles(df)
    df = generateData90To95ThPercentiles(df)
    df = generateData95To100ThPercentiles(df)
    return df

def extractRows(df):
    #uses data normalization to extract the desired row information
    index1 = (df[" Variable"] == " Treadmill run time(min:sec)")
    index2 = (df[" Variable"] == " Est. VO2peak(mL∙kg^-1∙min^-1)")
    index = index1 + index2
    desiredRows = df[index]
    return desiredRows

def extractCols(df):
    #uses data normalization to extract the desired column information
    df.__delitem__(' n')
    return df

def convertValueToSeconds(value):
    #converts the time data to seconds
    value = value.split(":")
    newValue = int(value[0])*60
    newValue += int(value[1])
    return newValue

def convertTimeValues(df, i):
    #converts the values in the treadmill runtime rows to seconds
    df[i][3] = convertValueToSeconds(df[i][3])
    df[i][13] = convertValueToSeconds(df[i][13])
    return df

def convertVO2MaxValues(df, i):
    #converts the VO2 max scores to floats
    df[i][4] = float(df[i][4])
    df[i][14] = float(df[i][14])
    return df

def convertTimeAndVO2Max(df):
    # converts the time and VO2 max scores to appropriate types
    keys = df.keys()
    iterableKeys = []
    for j in keys:
        if (j !=' Variable') and (j !='Sex'):
            iterableKeys.append(j)
    for i in iterableKeys:
        df = convertTimeValues(df, i)
        convertVO2MaxValues(df, i)
    return df

def deleteRedundantCols(df):
    df.__delitem__(' 5th')
    for i in range(9):
        df.__delitem__(' ' + str(10 + 10*i)+'th')
    df.__delitem__(' 95th')
    return df

def addColumnsToData(df):
    column1 = df.iloc[:,1]
    column2 = df.iloc[:,3]
    column3 = (column1 + column2)/2
    column3 = column3.astype(int)

    column4 = df.iloc[:,2]
    column5 = df.iloc[:,4]
    column6 = ((column4 + column5) / 2)
    column6.astype(float)
    df = pd.concat([df, column3], ignore_index = False, axis = 1)
    df = pd.concat([df, column6], ignore_index = False, axis = 1)
    return df

def removeRows(df):
    df = df.to_csv('newlyGeneratedData.csv', header=False)
    df = pd.read_csv('newlyGeneratedData.csv')
    df = df.to_csv('newlyGeneratedData.csv', index=False, header=False)
    df = pd.read_csv('newlyGeneratedData.csv')
    df = pd.read_csv('newlyGeneratedData.csv')
    df = df.to_csv('newlyGeneratedData.csv', index=False)
    df = pd.read_csv('newlyGeneratedData.csv')
    return df

def alterCSV():
    #alters the existing csv file by performing data normalization
    #and generating values
    df = pd.read_csv("data.csv")
    df = extractRows(df)
    df = extractCols(df)
    df = convertTimeAndVO2Max(df)
    df = generateValuesInRow(df)
    df = deleteRedundantCols(df)
    df = df.T
    df = removeRows(df)
    df = addColumnsToData(df)
    df = df.to_csv('newlyGeneratedData.csv', header=False, index=False)
    return df

def main():
    alterCSV()

if __name__ == "__main__":
    main()
