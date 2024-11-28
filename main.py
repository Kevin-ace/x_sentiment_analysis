import tweepy
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import time
import csv
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import io
from flask import Flask, render_template, request

# Step 1: Define a function to handle rate limits
def handle_rate_limit(error):
    reset_time = int(error.response.headers["x-rate-limit-reset"])
    sleep_time = reset_time - int(time.time())
    print(f"Rate limit reached. Sleeping for {sleep_time} seconds.")
    time.sleep(sleep_time)

# Step 2: Download the VADER lexicon for sentiment analysis
nltk.download('vader_lexicon')

# Step 3: Authenticate with Twitter's API using Bearer Token
client = tweepy.Client(bearer_token='Your Bearer Token')

# Step 4: Initialize the SentimentIntensityAnalyzer for VADER sentiment analysis
sia = SentimentIntensityAnalyzer()

# Initialize Flask app
app = Flask(__name__)

# Step 5: Web Route to handle form submission
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        keyword = request.form["keyword"]
        
        # List to store tweet data
        tweet_data = []
        
        # Initialize counters for sentiment
        positive_count = 0
        negative_count = 0
        neutral_count = 0
        
        # Step 6: Request tweets using the Twitter API
        try:
            tweets = client.search_recent_tweets(query=keyword, max_results=10, tweet_fields=["author_id", "created_at", "text"])
        except tweepy.TooManyRequests as e:
            handle_rate_limit(e)
            tweets = None
        except tweepy.TweepyException as e:
            print(f"Error occurred: {e}")
            tweets = None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            tweets = None
        
        # Step 7: Process the tweets and perform sentiment analysis
        if tweepy and hasattr(tweets, 'data'):
            for tweet in tweets.data:
                sentiment_score = sia.polarity_scores(tweet.text)['compound']
                sentiment = "Positive" if sentiment_score > 0.05 else "Negative" if sentiment_score < -0.05 else "Neutral"

                # Store tweet data
                tweet_data.append({
                    "author_id": tweet.author_id,
                    "created_at": tweet.created_at,
                    "sentiment": sentiment,
                    "text": tweet.text,
                    "sentiment_score": sentiment_score
                })

                # Increment counters
                if sentiment == "Positive":
                    positive_count += 1
                elif sentiment == "Negative":
                    negative_count += 1
                else:
                    neutral_count += 1

        # Prepare data for plotting
        sentiment_labels = ['Positive', 'Negative', 'Neutral']
        sentiment_values = [positive_count, negative_count, neutral_count]
        
        # Create the bar chart in memory
        fig, ax = plt.subplots()
        ax.bar(sentiment_labels, sentiment_values, color=["green", "red", "yellow"])
        ax.set_xlabel("Sentiment")
        ax.set_ylabel("Number of Tweets")
        ax.set_title(f"Sentiment Analysis for '{keyword}'")

        # Convert the plot to PNG and encode it to base64
        img = BytesIO()
        fig.savefig(img, format='png')
        img.seek(0)
        img_b64 = base64.b64encode(img.getvalue()).decode('utf-8')

        # Save sentiment analysis data to CSV
        with open("sentiment_analysis_results.csv", "w", newline='', encoding="utf-8") as csvfile:
            fieldnames = ["author_id", "created_at", "sentiment", "text", "sentiment_score"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in tweet_data:
                writer.writerow(row)

        print("Sentiment data saved to sentiment_analysis_results.csv")
        
        return render_template("index.html", img_b64=img_b64, keyword=keyword, sentiment_data=tweet_data)

    return render_template("index.html", img_b64=None)

if __name__ == "__main__":
    app.run(debug=True)
