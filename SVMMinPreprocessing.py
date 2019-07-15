
'''
@author: akhilesh
'''
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
import time

def preprocess_reviews(reviews):
    REPLACE_NO_SPACE = re.compile("[.;:!\'?,\"()\[\]]")
    REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")
    #replace all exclamations with no space
    reviews = [REPLACE_NO_SPACE.sub("", review.lower()) for review in reviews]
    #replace all breaks with space
    reviews = [REPLACE_WITH_SPACE.sub(" ", review) for review in reviews]
      
    return reviews


start_time = time.time()
df_train = pd.read_excel("drugs_data\\drug_data_train.xlsx",sheet_name="Obesity")
reviews_train = df_train["review"]
reviews_train_clean = preprocess_reviews(reviews_train)

df_test = pd.read_excel("drugs_data\\drug_data_test.xlsx",sheet_name="Obesity")
df_test.review = df_test.review.astype(str)
reviews_test = df_test["review"]
reviews_test_clean = preprocess_reviews(reviews_test)

vectorizer = TfidfVectorizer(ngram_range=(1,2))
vectorizer.fit(reviews_train_clean)
training_data = vectorizer.transform(reviews_train_clean)
test_data = vectorizer.transform(reviews_test_clean)

training_data_output = ["Poor" if rating <= 3 else "Average" if rating > 3 and rating <=6 
                        else "Good" if rating > 6 and rating <=8 else "Excellent" 
                        for rating in df_train["rating"]]

test_data_expected_output = ["Poor" if rating <= 3 else "Average" if rating > 3 and rating <=6 
                        else "Good" if rating > 6 and rating <=8 else "Excellent" 
                        for rating in df_test["rating"]]

svm = LinearSVC(C=1, max_iter=7000)
svm.fit(training_data,training_data_output)
predictions = svm.predict(test_data)
print("Accuracy is ",accuracy_score(test_data_expected_output, predictions))

feature_to_coef = {
    word: coef 
    for word, coef in zip(vectorizer.get_feature_names(),svm.coef_[0])
    }
 
print("Positive: ")
for best_positive in sorted(feature_to_coef.items(),key = lambda x: x[1], reverse = True)[:10]:
    print(best_positive)
 
print("Negative: ")
for best_negative in sorted(feature_to_coef.items(), key = lambda x: x[1])[:10]:
    print(best_negative)

print("Time taken: ", (time.time() - start_time))

