import os
import re
import csv

class fileInfo:
    def __init__(self, fileName, fullFile):
        self.name = fileName
        file = open(fullFile)
        info = file.read()
        file.close()
        self.subcatchments = isInString(info, "[SUBCATCHMENTS]")
        self.subAreas = isInString(info, "[SUBAREAS]")
        self.infiltration = isInString(info, "[INFILTRATION]")
        self.evaporation = isInString(info, "[EVAPORATION]")
        self.junctions = isInString(info, "[JUNCTIONS]")
        self.outfalls = isInString(info, "[OUTFALLS]")
        self.storage = isInString(info, "[STORAGE]")
        self.conduits = isInString(info, "[CONDUITS]")
        self.orifices = isInString(info, "[ORIFICES]")
        self.xsections = isInString(info, "[XSECTIONS]")
        self.controls = isInString(info, "[CONTROLS]")
        self.inflows = isInString(info, "[INFLOWS]")
        self.timeseries = isInString(info, "[TIMESERIES]")

    
def isInString(string, substring):
    if(string.find(substring) != -1):
        return 1
    else:
        return 0
        

folder = input("Enter folder location of input files: ")
inputList = os.listdir(folder)

fields = ['Name', 'Subcatchments', 'SubAreas', 'Infiltration', 'Evaporation', 'Junctions', 'Outfalls', 'Storage', 'Conduits', 'Orifices', 'XSections', 'Controls', 'Inflows', 'Timeseries']

myList = []
for x in inputList:
    temp = folder + "\\" + x
    fi = fileInfo(x, temp)
    myList.append([fi.name,fi.subcatchments,fi.subAreas,fi.infiltration,fi.evaporation,fi.junctions,fi.outfalls,fi.storage,fi.conduits,fi.orifices,fi.xsections,fi.controls,fi.inflows,fi.timeseries])

print("Number of files: ", len(myList))    
csvFileName = "results.csv"

with open(csvFileName, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(myList)