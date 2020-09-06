from nltk.sentiment.vader import SentimentIntensityAnalyzer

def get_sentiment(review): #this function return the sentiment score for a given reviews
    new_words = {'cushiony':1, 'comfort':0,'support':0, 'unsupportive':-1, 'lightweight':1, 'heavyweight':-1, 'stabilize':1, 'instability':-1, 'unresponsive':-1, 'durable':1, 'breathable':1, 'protective':1, 'too':0, 'flimsy':-1, 'freedom':0, 'tore':-1.5, 'narrow':-1, 'strike':0, 'right':1.5, 'hole':-1.5, 'never':-.5, 'holes':-1.5, "stiff":-1, 'return':-.5, 'returning':-.5, 'issue':-1, "untied":-1, 'clunky':-1, 'stiffness':-1, 'swollen':-1, 'stylish':1, 'rip':-1, 'returned':-.5, 'bulky':-1} #this list specifies sentiment scores for certain common words that are related to running shoes, in other words it adds context to the sentiment analysis
    sid = SentimentIntensityAnalyzer()
    sid.lexicon.update(new_words) #updates the lexicon with the specified sentiment scores
    score = sid.polarity_scores(review) #calculates the positive, negative, neutral, and compound sentiment score for the review
    compound = score.get('compound') 
    return compound

review = '' #variable of the string type
get_sentiment(review) #function call