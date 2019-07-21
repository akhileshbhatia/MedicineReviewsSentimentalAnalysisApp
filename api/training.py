'''
Created on Jul 18, 2019
'''
import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import time
from _datetime import datetime
from common_utilities import getSheetName

def preprocess_reviews(reviews):
    REPLACE_NO_SPACE = re.compile("[.;:!\'?,\"()\[\]]")
    REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")
    reviews = [REPLACE_NO_SPACE.sub("", line.lower()) for line in reviews]
    reviews = [REPLACE_WITH_SPACE.sub(" ", line) for line in reviews]
    
    return reviews

def trainModel():
    f = open("training_log.txt", "a")
    f.write("\n-------------------------------------------------------------------------")
    start_time = time.time()
    f.write("\nTraining model function called at: " + str(datetime.today()))
    sheet = getSheetName()
    f.write("\nTraining for sheet: "+sheet)
    df_train = pd.read_excel("F:\\UCC Notes\\Dissertation\\Code\\PythonApp\\drugs_data_original\\drug_data_train.xlsx",sheet_name=sheet)
    reviews_train = df_train["review"]
    reviews_train_clean = preprocess_reviews(reviews_train)
    
    
    df_test = pd.read_excel("F:\\UCC Notes\\Dissertation\\Code\\PythonApp\\drugs_data_original\\drug_data_test.xlsx",sheet_name=sheet)
    df_test.review = df_test.review.astype(str)
    reviews_test = df_test["review"]
    reviews_test_clean = preprocess_reviews(reviews_test)
    
    vectorizer = CountVectorizer(binary=True,ngram_range=(1,3))
    vectorizer.fit(reviews_train_clean)
    training_data = vectorizer.transform(reviews_train_clean)
    
    training_data_output = ["Poor" if rating <= 3 else "Average" if rating > 3 and rating <=6 
                            else "Good" if rating > 6 and rating <=8 else "Excellent" 
                            for rating in df_train["rating"]]
    
    test_data = vectorizer.transform(reviews_test_clean)
     
    test_data_expected_output = ["Poor" if rating <= 3 else "Average" if rating > 3 and rating <=6 
                                 else "Good" if rating > 6 and rating <=8 else "Excellent" 
                                 for rating in df_test["rating"]]
     
     
    model = LogisticRegression(C=1,solver="lbfgs",max_iter=2000,multi_class="auto")
    model.fit(training_data,training_data_output)
    
    predictions = model.predict(test_data)
#     something = predictions.toarray().tolist()
#     print(type(something))
    df_test["review_classification"] = predictions
    df_test.to_excel("trained_dataset.xlsx",sheet_name=sheet,index=False)
    f.write("\nTrained data saved to file")
    
    accuracy = accuracy_score(test_data_expected_output,predictions)
    
    f.write("\nTraining completed in " + str("{0:.2f}".format(time.time() - start_time)) +" seconds with accuracy score " + str(accuracy))
    
    f.close()
    
    return "Training complete"
