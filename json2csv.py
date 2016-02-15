#!/usr/bin/env python
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
import csv
import types
import urllib2

def GetUrl(url):  
    try:  
        data = urllib2.urlopen(url).read()  
        return data  
    except Exception,e:  
        print e 


def jsonFile(fileData):  
    file = open("output.json","w")  
    file.write(fileData)  
    file.close() 

def transformData(primaryKey=""):
    input = open("output.json")
    data = json.load(input)
    input.close()
    header = []
    result = []
    outputFileName = 'Json2CsvResult'
    for i in data:
        for j in i.keys():
            if j not in header:
                header.append(j)
    with open(outputFileName+".csv", 'wb') as output_file:
        fieldnames = list(header)
        writer = csv.DictWriter(output_file, fieldnames, delimiter=',', quotechar='"')
        result.append(header)
        for x in data:
            row_value = {}
            for y in x.keys():
                yValue = x.get(y)
                if type(yValue) == int or type(yValue) == bool or type(yValue) == float or type(yValue) == list:
                    row_value[y] = str(yValue).encode('utf8')
                elif type(yValue) == unicode:
                    row_value[y] = yValue.encode('utf-8')
            result.append(row_value.values())
    return fieldnames,result

if __name__ == '__main__':
    url = sys.argv[1]
    data_load = GetUrl(url) # load data from the API
    jsonFile(data_load) # write to json file
    filednames,trans_data = transformData() # transform json to csv
    with open('jsonToCsvResult.csv','wb') as f:
        writer = csv.writer(f)
        writer.writerows(trans_data)
    f.close()

