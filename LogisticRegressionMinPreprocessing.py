'''
@author: akhilesh
'''
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import time

def preprocess_reviews(reviews):
    REPLACE_NO_SPACE = re.compile("[.;:!\'?,\"()\[\]]")
    REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")
    reviews = [REPLACE_NO_SPACE.sub("", line.lower()) for line in reviews]
    reviews = [REPLACE_WITH_SPACE.sub(" ", line) for line in reviews]
    
    return reviews

start_time = time.time()
df_train = pd.read_excel("drugs_data\\drug_data_train.xlsx",sheet_name="Obesity")
reviews_train = df_train["review"]
reviews_train_clean = preprocess_reviews(reviews_train)


df_test = pd.read_excel("drugs_data\\drug_data_test.xlsx",sheet_name="Obesity")
df_test.review = df_test.review.astype(str)
reviews_test = df_test["review"]
reviews_test_clean = preprocess_reviews(reviews_test)

tfidf_vectorizer = TfidfVectorizer()
tfidf_vectorizer.fit(reviews_train_clean)
training_data = tfidf_vectorizer.transform(reviews_train_clean)

training_data_output = [1 if rating > 5 else 0
                        for rating in df_train["rating"]]

test_data = tfidf_vectorizer.transform(reviews_test_clean)

test_data_expected_output = [1 if rating > 5 else 0
                             for rating in df_test["rating"]]


model = LogisticRegression(C=1,solver="lbfgs",max_iter=2000)
model.fit(training_data,training_data_output)
predictions = model.predict(test_data)
print("Accuracy is " ,accuracy_score(test_data_expected_output,predictions))
 
feature_to_coef = {
    word: coef 
    for word, coef in zip(tfidf_vectorizer.get_feature_names(),model.coef_[0])
    }

print("Positive: ")
for best_positive in sorted(feature_to_coef.items(),key = lambda x: x[1], reverse = True)[:10]:
    print(best_positive)

print("Negative: ")
for best_negative in sorted(feature_to_coef.items(), key = lambda x: x[1])[:10]:
    print(best_negative)

print("Time taken: ",(time.time() - start_time))