'''
@author: akhilesh
'''
import pandas as pd
import re
import html
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import time

def preprocess_reviews(reviews):
    REPLACE_NO_SPACE = re.compile("[.;:!\'?,\"()\[\]]")
    REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")
    #replace all exclamations with no space
    reviews = [REPLACE_NO_SPACE.sub("", review.lower()) for review in reviews]
    #replace all breaks with space
    reviews = [REPLACE_WITH_SPACE.sub(" ", review) for review in reviews]
    #replace all html code characters with their original string values before removing stop words
    reviews = [html.unescape(review) for review in reviews]
    #remove the stop words
    reviews = remove_stop_words(reviews)
        
    return reviews

def remove_stop_words(reviews):
    english_stop_words = stopwords.words('english')
    removed_stop_words = []
    for review in reviews:
        removed_stop_words.append(' '.join([word for word in review.split()
                                           if word not in english_stop_words]))
    
    return removed_stop_words

def lemmatize_reviews(reviews):
    lemmatizer = WordNetLemmatizer()
    lemmatized_reviews = []
    for review in reviews:
        lemmatized_reviews.append(' '.join([lemmatizer.lemmatize(word) for word in review.split()]))
    
    return lemmatized_reviews

start_time = time.time()
df_train = pd.read_excel("drugs_data\\drug_data_train.xlsx",sheet_name="Obesity")
reviews_train = df_train["review"]
reviews_train_clean = preprocess_reviews(reviews_train)
reviews_train_clean = lemmatize_reviews(reviews_train_clean)

df_test = pd.read_excel("drugs_data\\drug_data_test.xlsx",sheet_name="Obesity")
df_test.review = df_test.review.astype(str)
reviews_test = df_test["review"]
reviews_test_clean = preprocess_reviews(reviews_test)
reviews_test_clean = lemmatize_reviews(reviews_test_clean)

vectorizer = TfidfVectorizer(ngram_range=(2,3))
vectorizer.fit(reviews_train_clean)
training_data = vectorizer.transform(reviews_train_clean)

training_data_output = ["Poor" if rating <= 3 else "Average" if rating > 3 and rating <=6 
                        else "Good" if rating > 6 and rating <=8 else "Excellent" 
                        for rating in df_train["rating"]]

test_data = vectorizer.transform(reviews_test_clean)

test_data_expected_output = ["Poor" if rating <= 3 else "Average" if rating > 3 and rating <=6 
                             else "Good" if rating > 6 and rating <=8 else "Excellent" 
                             for rating in df_test["rating"]]


model = LogisticRegression(C=1,solver="lbfgs",multi_class="auto",max_iter=2000)
model.fit(training_data,training_data_output)
predictions = model.predict(test_data)
print("\nAccuracy is" ,accuracy_score(test_data_expected_output,predictions))
 
feature_to_coef = {
    word: coef 
    for word, coef in zip(vectorizer.get_feature_names(),model.coef_[0])
    }
 
print("\nPositive: ")
for best_positive in sorted(feature_to_coef.items(),key = lambda x: x[1], reverse = True)[:10]:
    print(best_positive)
 
print("\nNegative: ")
for best_negative in sorted(feature_to_coef.items(), key = lambda x: x[1])[:10]:
    print(best_negative)

print("\nTime taken: ", (time.time() - start_time))





