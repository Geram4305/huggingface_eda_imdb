#### GOAL - To study the imdb reviews dataset from hugging face. Specifically, understand differences and similarities between positive and negative reviews with a labelled dataset. Using IMDB reviews for EDA demo. Ref: https://huggingface.co/datasets/imdb #####

# Reason for choosing this EDA for the demo:
1.  IMDb Reviews is a well-known dataset, and many people are familiar with the IMDb platform. This familiarity can make it easier for anyone to relate to the data.
2. Understand how people use the same words in different contexts because IMDB reviews are open to the public and anyone can leave a review. A labeled dataset helps find words used in both positive and negative reviews. 
3. Answer questions like, do people write a lot more for negative reviews than positive, what are the most common adjectives used in a positive or negative review.
4. Sentiment analysis has practical relevance in various industries including marketing, customer feedback analysis, and social media monitoring. 

# Steps taken:
1. Analyze basic characteristics of dataset like number of reviews, class ratio, etc. including looking for missing values.
3. Splitting data into positive and negative reviews - essential to compare the two classes. 
4. Sentence and word length comparison - Understand whether people spend more time typing longer reviews for negative or positive.
5. Word count histogram to find the most common words - tells us whether the most common words have any relevance.
6. Processing of reviews to remove irrelevant words, symbols, etc.
7. Bi-grams exploration - Identify commonly occurring pairs of words to understand everyday language pattern and get insights into how words are typically used together in positive and negative contexts.
8. Word frequency comparison - Adjectives. Commparing the most common adjectives used to describe movies in both positive and negative contexts, helps us understand how a typical reviewer thinks or reacts. This also shows us the similarities and differences between both classes. Some adjectives may occur in both scenarios often while some adjectives are reserved for one of the classes only.
9. Use Word2Vec to analyze the context of certain words that are common in both scenarios, to check if there is a difference in contextual meaning of the word when used in positive compared to negative reviews.
10. t-SNE plot to visualize the semantic relationships between certain words in both positive and negative contexts. This would also shed some light on hidden characterstics of positive and negative reviews as well as the quality of the dataset.

# How to run the EDA:
1. Use windows machine to run the notebook.
2. Need Python installed for running the notebook.
3. Please run the notebook - dataset_eda.ipynb. The setup of required libraries is automatically integrated. It creates a virtual environment and installs libs in it. 
4. The libraries needed to run the notebook are also provided in a separate file - requirements.txt. Alternatively, to avoid setting up virtual env, please run "pip install -r requirements.txt by opening a command prompt. Then run the notebook. The virtual env method is recommended. 