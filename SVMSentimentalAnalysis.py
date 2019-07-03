'''
@author: akhilesh
'''
import pandas as pd
import re
import html
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from LogisticRegressionSentimentalAnalysis import training_data

def preprocess_reviews(reviews):
    REPLACE_NO_SPACE = re.compile("[.;:!\'?,\"()\[\]]")
    REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")
    #remove all exclamations with no space
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

df_train = pd.read_excel("drugs_data\\drug_data_train.xlsx",sheet_name="Obesity")
reviews_train = df_train["review"]
reviews_train_clean = preprocess_reviews(reviews_train)
reviews_train_clean = lemmatize_reviews(reviews_train_clean)

df_test = pd.read_excel("drugs_data\\drug_data_test.xlsx",sheet_name="Obesity")
df_test.review = df_test.review.astype(str)
reviews_test = df_test["review"]
reviews_test_clean = preprocess_reviews(reviews_test)
reviews_test_clean =lemmatize_reviews(reviews_test_clean)


ngram_vectorizer = CountVectorizer(binary=True, ngram_range=(1,2))
ngram_vectorizer.fit(reviews_train_clean)
training_data = ngram_vectorizer.transform(reviews_train_clean)
test_data = ngram_vectorizer

#following code is to be used for testing purpose only 
# target = [1 if rating > 5 else 0 for rating in df_train["rating"]]
#  
# X_train, X_val, y_train, y_val = train_test_split(X, target, train_size=0.75)
# 
# for c in [0.01,0.05,0.25,0.5,1]: 
#     lr = LogisticRegression(C=c)
#     lr.fit(X_train, y_train)
#     print("Accuracy for C= ",c,": ",accuracy_score(y_val, lr.predict(X_val)))
#C=1 provides te best results
#above code is to be used for testing purpose only




