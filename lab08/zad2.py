import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import text2emotion as te
# pip install emoji==1.2.0

nltk.download('vader_lexicon')

# A)
positive_opinion = "Wow wow wow! I was taken here by my boyfriend and friends for my birthday and it was truly an amazing experience. One of the best seafood restaurants I have ever visited. The view of the sea from our table was beautiful. We ordered the fish of the day which was cooked and served beautifully to us. We all loved how we were told exactly where the fish was caught that morning, and you could taste how fresh the seafood was in every dish. Every member of the staff is kind, friendly and funny. To end the evening, the birthday cake i was surprised with was superb. I want to thank the staff for making it such a memorable evening for me and my friends. I would 100% recommended this restaurant if you're looking for amazing fresh seafood and beautiful sea vies"

negative_opinion = "Awful service and far below average food for what you're paying. Such a disappointment after reading the reviews and seeing the location. There were 7 of us out for dinner and the night started with them bringing just one persons starter expecting them to start eating while the rest of us watch... The food Fishermans Spaghetti lacked any flavor and the rest was a combination of no seasoning / poor balance / small quantity / poor quality ... the list goes on. Waiting 20 mins at one point for a waiter to come and serve us drinks and after asking for Parmesan for a pasta dish they took 10 minutes to bring it...??? Food cold by that stage. When giving the feedback to the manager he has the cheek to argue with me to top it off... maybe the fact you don't listen to your customers is why your dining experience was muck."

# B)
print("B)")
sid = SentimentIntensityAnalyzer()

positive_scores = sid.polarity_scores(positive_opinion)
negative_scores = sid.polarity_scores(negative_opinion)

print("Positive Opinion Scores:", positive_scores)
print("Negative Opinion Scores:", negative_scores)

aggregate_score = (positive_scores['compound'] + negative_scores['compound']) / 2
print("Aggregate Compound Score:", aggregate_score)

# C)
print("C)")
positive_emotions = te.get_emotion(positive_opinion)
negative_emotions = te.get_emotion(negative_opinion)

print("Positive Opinion Emotions:", positive_emotions)
print("Negative Opinion Emotions:", negative_emotions)

'''
D) 
Scores - Jestem zaskoczony, że tak dużo wartości jest w granicach neutralnych w obu przypadkach. Do tego trochę mogło by być więcej neg w negatywnej opinii

Emotions - Nie wiem skąd wziął się wysoki poziom Fear i Surprise w negatywnej opinii, a czemu zerowe Angry. Positive wygląda dobrze, oprócz Sad
'''
# E)
print("E)")

positive_opinion = "Wow wow wow! I was taken here by my boyfriend and friends for my birthday and it was truly an amazing experience. One of the best seafood restaurants I have ever visited. The view of the sea from our table was beautiful. We ordered the fish of the day which was cooked and served beautifully to us. We all loved how we were told exactly where the fish was caught that morning, and you could taste how fresh the seafood was in every dish. Every member of the staff is kind, friendly and funny. To end the evening, the birthday cake I was surprised with was superb. I want to thank the staff for making it such a memorable evening for me and my friends. I would 100% recommend this restaurant if you're looking for amazing fresh seafood and beautiful sea views."

negative_opinion = "Awful service and far below average food for what you're paying. Such a disappointment after reading the reviews and seeing the location. The food Fisherman's Spaghetti lacked any flavor and the rest was a combination of no seasoning, poor balance, small quantity, poor quality. I was so angry! Waiting 20 minutes at one point for a waiter to come and after asking for Parmesan for a pasta dish they took 10 minutes to bring it! Food cold by that stage which is disgusting. When giving the feedback to the manager he has the cheek to argue with me to top it off! Maybe the fact you don't listen to your customers is why your dining experience was muck and awful. I left the place angry and offended. "



sid = SentimentIntensityAnalyzer()
positive_scores = sid.polarity_scores(positive_opinion)
negative_scores = sid.polarity_scores(negative_opinion)

print("Positive Opinion Scores:", positive_scores)
print("Negative Opinion Scores:", negative_scores)

aggregate_score = (positive_scores['compound'] + negative_scores['compound']) / 2
print("Aggregate Compound Score:", aggregate_score)

positive_emotions = te.get_emotion(positive_opinion)
negative_emotions = te.get_emotion(negative_opinion)

print("Positive Opinion Emotions:", positive_emotions)
print("Negative Opinion Emotions:", negative_emotions)