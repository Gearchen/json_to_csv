#!/usr/bin/env python
#coding=utf-8
import sys
print sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('utf-8')
import json
import csv
import types
import urllib2

def registerUrl(url):  
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
    outputFileName = 'jsonToCsvResult'
    for i in data:
        for j in i.keys():
            if j not in header:
                header.append(j)
    with open(outputFileName+".csv", 'wb') as output_file:
        fieldnames = list(header)
        writer = csv.DictWriter(output_file, fieldnames, delimiter=',', quotechar='"')
        result.append(header)
        for x in data:
            # print x
            row_value = {}
            for y in x.keys():
                yValue = x.get(y)
                # print yValue
                if type(yValue) == int or type(yValue) == bool or type(yValue) == float or type(yValue) == list:
                    row_value[y] = str(yValue).encode('utf8')
                elif type(yValue) == unicode:
                    row_value[y] = yValue.encode('utf-8')
                # print row_value.values()
            result.append(row_value.values())
    return fieldnames,result

if __name__ == '__main__':
    url = sys.argv[1]
    data_load = registerUrl(url) # load data from the API
    jsonFile(data_load) # write to json file
    filednames,trans_data = transformData() # transform json to csv
    with open('jsonToCsvResult.csv','wb') as f:
        writer = csv.writer(f)
        # writer.writerow(filednames)
        writer.writerows(trans_data)
    f.close()

