'''
Created on Jul 21, 2019

'''
def getSheetName():
    return "Multiple"

def getReviewClassificationWeights():
    classificationMap = {}
    classificationMap["Poor"] = -0.2
    classificationMap["Average"] = 0.2
#     classificationMap["Average"] = 0.5
    classificationMap["Good"] = 0.5
#     classificationMap["Good"] = 0.7
    classificationMap["Excellent"] = 0.9
    classificationMap[""] = 1
    return classificationMap