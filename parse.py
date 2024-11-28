import csv
import pandas as pd
import nltk
from nltk.corpus import stopwords
import string
from collections import Counter
import math

def main():

    nltk.download('stopwords')
    stopwords_list = stopwords.words('english')

    # Read specific columns from CSV file
    columns = ['Title', 'description', 'Category', 'Sentiment']  # Replace with your column names
    df = pd.read_csv('annotation.csv', usecols=columns)

    category_word_counts = {}
    sentiment_word_counts = {}

    for category, group in df.groupby('Category'):
        all_words = []
        for index, row in group.iterrows():
            text = f"{row['Title']} {row['description']}".lower()
            words = text.translate(str.maketrans("","", string.punctuation)).split()
            filtered_words = [word for word in words if word not in stopwords_list]
            all_words.extend(filtered_words)

        # Count the frequency of each word for the category
        word_counts = Counter(all_words)
        category_word_counts[category] = word_counts

    # Calculate tf-idf scores
    tf_idf_dict = {}

    for category, word_counts in category_word_counts.items():
        for word in word_counts.keys():
            tf = word_counts[word]
            num_categories = 5
            num_word_in_category = 0

            # Count how many other categories include the word
            for my_category, my_word_counts in category_word_counts.items():
                if word in my_word_counts.keys():
                    num_word_in_category += 1
            
            idf = math.log(num_categories / num_word_in_category)

            # Change the count to the tf_idf score
            tf_idf = round(tf*idf, 2)
            word_counts[word] = tf_idf


            

    ##Display the most common words for each category
    for category, word_counts in category_word_counts.items():
        print(f"Category: {category}")
        print(word_counts.most_common(10))
        print("-" * 40)



if __name__ == "__main__":
    main()
