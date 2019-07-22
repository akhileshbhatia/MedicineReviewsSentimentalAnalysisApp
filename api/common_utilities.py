'''
Created on Jul 21, 2019

'''
def getSheetName():
    return "Multiple"

def getReviewClassificationWeights():
    map = {}
    map["Poor"] = -0.2
    map["Average"] = 0.2
#     map["Average"] = 0.5
    map["Good"] = 0.5
#     map["Good"] = 0.7
    map["Excellent"] = 0.9
    return map