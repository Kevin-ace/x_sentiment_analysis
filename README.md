# Sentiment Analysis of Tweets

## Overview

This web application performs sentiment analysis on recent tweets based on a user-specified keyword. It fetches tweets using the Twitter API and uses VADER (Valence Aware Dictionary and sEntiment Reasoner) for sentiment analysis. The sentiment of each tweet is classified as Positive, Negative, or Neutral, and the results are displayed with a bar chart and a downloadable CSV.

## Features

**Keyword Search**: Enter any keyword to fetch relevant tweets.
**Sentiment Analysis**: Analyzes the sentiment of each tweet (Positive, Negative, or Neutral).
**Visualization**: Displays a bar chart that shows the distribution of sentiments.
**CSV Export**: Allows you to download a CSV file with tweet details and sentiment scores.

## Tech Stack

- Python: Main programming language used.
- Flask: Web framework to build the interactive web app.
- Tweepy: Library to interact with the Twitter API.
- NLTK (VADER): For sentiment analysis of tweets.
- Matplotlib: To create the bar chart visualization.
- HTML/CSS: For frontend user interface.

## Prerequisites

Before running the app, ensure you have the following installed:

- Python 3.x
- pip (Python package manager)
- You also need to create a Twitter Developer account and generate a Bearer Token to use the Twitter API.

## Setup

Step 1: Clone the repository
```bash
  git clone git@github.com:Kevin-ace/x_sentiment_analysis.git
  cd sentiment-analysis-twitter
```

Step 2: Set up a Virtual Environment (Optional but recommended)
```bash
  python3 -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Step 3: Install dependencies
```bash
  Install the required Python libraries using pip:
  pip install -r requirements.txt
```

Step 4: Configure Twitter API
- Create a Twitter Developer account at https://developer.twitter.com.
- Create a project and an app to generate your Bearer Token.
- Replace the following line in the app.py file with your Bearer Token:
```python
  client = tweepy.Client(bearer_token='YOUR_TWITTER_BEARER_TOKEN')
```
Step 5: Run the Application
```bash
python app.py
```
The application will start running on http://127.0.0.1:5000/ by default. Open this URL in your browser to use the app.

## How It Works

  The app uses the Twitter API to fetch recent tweets based on the keyword provided by the user.
  The VADER sentiment analysis (from the NLTK library) is used to analyze the sentiment of each tweet.
  The sentiment is categorized as Positive, Negative, or Neutral based on the compound sentiment score from VADER.
  A bar chart is created using Matplotlib to visualize the distribution of sentiments.
  The tweet data along with sentiment scores is saved to a CSV file that can be downloaded.

    Example;
      Enter a keyword (e.g., "Python") in the input field.

  The app will fetch tweets related to the keyword.
  Sentiment analysis results will be displayed along with a bar chart showing the distribution of sentiments (Positive, Negative, Neutral).
  You can download the results in CSV format.

  Sample Output
  ```
  Tweet 1:
    Sentiment: Positive
    Sentiment Score: 0.8
  ```
  ```
  Tweet 2:
    Sentiment: Neutral
    Sentiment Score: 0.1
  ```

### Bar Chart
A bar chart is displayed showing sentiment distribution, such as:

Positive: 6 tweets
Negative: 2 tweets
Neutral: 2 tweets
CSV Download

The CSV file includes the following columns:

author_id
created_at
sentiment
text
sentiment_score

Example CSV Output:
  ```cvs
  author_id,created_at,sentiment,text,sentiment_score
  1234567890,2024-11-27 12:00:00,Positive,"I love Python! #Python",0.8
  0987654321,2024-11-27 13:00:00,Negative,"I hate bugs in my code! #frustrated",-0.7
...
```

## Contributing

Contributions are welcome! Feel free to fork the repository, submit issues, or create pull requests. Please ensure that your contributions follow the existing code style and that tests are updated accordingly.

## License

This project is licensed under the MIT License – see the LICENSE file for details.

## Directory Structure

sentiment-analysis-twitter/
│
├── main.py                # Main Flask app
├── sentiment_analysis_results.csv  # Output CSV with sentiment data
├── requirements.txt      # Python dependencies
├── templates/            # HTML templates
│   └── index.html        # Main page HTML template
└── static/               # Static assets like CSS files
    └── style.css         # Custom styles for the app
