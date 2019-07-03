'''
@author: akhilesh
'''
import pandas as pd
import re
import html
from nltk.corpus import stopwords

def preprocess_reviews(reviews):
    REPLACE_NO_SPACE = re.compile("[.;:!\'?,\"()\[\]]")
    REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")
    reviews = [REPLACE_NO_SPACE.sub("", review.lower()) for review in reviews]
    reviews = [REPLACE_WITH_SPACE.sub(" ", review) for review in reviews]
    
    reviews = [html.unescape(review) for review in reviews]
        
    return reviews

def remove_stop_words(corpus):
    english_stop_words = stopwords.words('english')
    removed_stop_words = []
    for review in corpus:
        removed_stop_words.append(' '.join([word for word in review.split()
                                           if word not in english_stop_words]))
    
    return removed_stop_words

df_train = pd.read_excel("drugs_data\\drug_data_train.xlsx",sheet_name="Obesity")
reviews_train = df_train["review"]
reviews_train_clean = preprocess_reviews(reviews_train)
print(reviews_train_clean[0])
no_stop_words = remove_stop_words(reviews_train_clean)
print(no_stop_words[0])




# df_test = pd.read_excel("drugs_data\\drug_data_test.xlsx",sheet_name="Obesity")
# df_test.review = df_test.review.astype(str)
# reviews_test = df_test["review"]
# reviews_test_clean = preprocess_reviews(reviews_test)

