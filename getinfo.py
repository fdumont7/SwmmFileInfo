import os
import re
import csv

class fileInfo:
    def __init__(self, fileName, fullFile):
        self.name = fileName
        file = open(fullFile, encoding = "mbcs")
        info = file.read()
        file.close()
        self.title = isInString(info, "[TITLE]")
        self.options = isInString(info, "[OPTIONS]")
        self.report = isInString(info, "[REPORT]")
        self.files = isInString(info, "[FILES]")
        self.raingages = isInString(info, "[RAINGAGES]")
        self.evaporation = isInString(info, "[EVAPORATION]")
        self.temperature = isInString(info, "[TEMPERATURE]")
        self.adjustments = isInString(info, "[ADJUSTMENTS]")
        self.subcatchments = isInString(info, "[SUBCATCHMENTS]")
        self.subareas = isInString(info, "[SUBAREAS]")
        self.infiltration = isInString(info, "[INFILTRATION]")
        self.lidControls = isInString(info, "[LID_CONTROLS]")
        self.lidUsage = isInString(info, "[LID_USAGE]")
        self.aquifers = isInString(info, "[AQUIFERS]")
        self.groundwater = isInString(info, "[GROUNDWATER]")
        self.gwf = isInString(info, "[GWF]")
        self.snowpacks = isInString(info, "[SNOWPACKS]")
        self.junctions = isInString(info, "[JUNCTIONS]")
        self.outfalls = isInString(info, "[OUTFALLS]")
        self.dividers = isInString(info, "[DIVIDERS]")
        self.storage = isInString(info, "[STORAGE]")
        self.conduits = isInString(info, "[CONDUITS]")
        self.pumps = isInString(info, "[PUMPS]")
        self.orifices = isInString(info, "[ORIFICES]")
        self.weirs = isInString(info, "[WEIRS]")
        self.outlets = isInString(info, "[OUTLETS]")
        self.xsections = isInString(info, "[XSECTIONS]")
        self.transects = isInString(info, "[TRANSECTS]")
        self.streets = isInString(info, "[STREETS]")
        self.inlets = isInString(info, "[INLETS]")
        self.losses = isInString(info, "[LOSSES]")
        self.controls = isInString(info, "[CONTROLS]")
        self.pollutants = isInString(info, "[POLLUTANTS]")
        self.landuses = isInString(info, "[LANDUSES]")
        self.coverages = isInString(info, "[COVERAGES]")
        self.loadings = isInString(info, "[LOADINGS]")
        self.buildup = isInString(info, "[BUILDUP]")
        self.washoff = isInString(info, "[WASHOFF]")
        self.treatment = isInString(info, "[TREATMENT]")
        self.inflows = isInString(info, "[INFLOWS]")
        self.dwf = isInString(info, "[DWF]")
        self.rdii = isInString(info, "[RDII]")
        self.hydrographs = isInString(info, "[HYDROGRAPHS]")
        self.curves = isInString(info, "[CURVES]")
        self.timeseries = isInString(info, "[TIMESERIES]")
        self.patterns = isInString(info, "[PATTERNS]")
        

    
def isInString(string, substring):
    if(string.find(substring) != -1):
        return 1
    else:
        return 0
        

folder = input("Enter folder location of input files: ")
inputList = []
for root, dirs, files in os.walk(folder):
    for file in files:
        inputList.append(os.path.join(root,file))
#inputList = os.listdir(folder)
fields = ['Name', 'Title', 'Options', 'Report', \
          'Files', 'Rain gages', 'Evaporation', \
          'Temperature', 'Adjustments', 'Subcatchments', \
          'Subareas', 'Infiltration', 'LID Controls', \
          'LID Usage', 'Aquifers', 'Groundwater', 'GWF', \
          'Snowpacks', 'Junctions', 'Outfalls', \
          'Dividers', 'Storage', 'Conduits', 'Pumps', \
          'Orifices', 'Weirs', 'Outlets', 'X sections', \
          'Transects', 'Streets', 'Inlets', 'Losses', \
          'Controls', 'Pollutants', 'Land uses', \
          'Coverages', 'Loadings', 'Buildup', 'Washoff', \
          'Treatment', 'Inflows', 'DWF', 'RDII', \
          'Hydrographs', 'Curves', 'Timeseries', 'Patterns']

myList = []

for f in inputList:
    if f.split('.')[-1].lower() == 'inp' : 
        #fullFile = folder + "\\" + f
        fi = fileInfo(f.split('\\')[-1], f)
        myList.append([fi.name, fi.title, fi.options, fi.report, \
                       fi.files, fi.raingages, fi.evaporation, \
                       fi.temperature, fi.adjustments, fi.subcatchments, \
                       fi.subareas, fi.infiltration, fi.lidControls, \
                       fi.lidUsage, fi.aquifers, fi.groundwater, fi.gwf, \
                       fi.snowpacks, fi.junctions, fi.outfalls, \
                       fi.dividers, fi.storage, fi.conduits, fi.pumps, \
                       fi.orifices, fi.weirs, fi.outlets, fi.xsections, \
                       fi.transects, fi.streets, fi.inlets, fi.losses, \
                       fi.controls, fi.pollutants, fi.landuses, \
                       fi.coverages, fi.loadings, fi.buildup, fi.washoff, \
                       fi.treatment, fi.inflows, fi.dwf, fi.rdii, \
                       fi.hydrographs, fi.curves, fi.timeseries, fi.patterns])
        #myList.append([fi.name,fi.subcatchments,fi.subAreas,fi.infiltration,fi.evaporation,fi.junctions,fi.outfalls,fi.storage,fi.conduits,fi.orifices,fi.xsections,fi.controls,fi.inflows,fi.timeseries])

print(folder.split('\\')[-1])
print("Number of files: ", len(myList))    
csvFileName = folder.split('\\')[-1] + ".csv"


with open(csvFileName, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(myList)