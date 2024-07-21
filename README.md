# Twitter List Sentiment Analyzer

## About
This project is a Python-based tool that analyzes the sentiment of tweets from a specified Twitter list. It demonstrates the ability to interact with the Twitter API, process tweet data, perform sentiment analysis, and provide insights into the emotional tone of tweets from specific users or about particular topics.

## Features
- Fetches tweets from a specified Twitter list using the Twitter API
- Performs sentiment analysis on each tweet
- Classifies tweets into positive, neutral, or negative sentiments
- Provides basic statistical analysis of sentiment distribution
- Handles Twitter API rate limiting and pagination

## Technologies Used
- Python 3
- Tweepy for Twitter API interaction
- TextBlob for natural language processing and sentiment analysis
- Pandas for data manipulation and analysis

## How It Works
1. The script authenticates with the Twitter API using provided credentials.
2. It fetches tweets from a specified Twitter list.
3. Each tweet is analyzed using TextBlob to determine its sentiment.
4. The sentiment is classified as positive, neutral, or negative based on the polarity score.
5. Results are compiled into a Pandas DataFrame for easy analysis.
6. Basic statistics about the sentiment distribution are printed.

## Prerequisites
- Twitter Developer Account with API access
- Twitter API credentials (consumer key, consumer secret, access token, access token secret)

## Installation and Usage
1. Clone this repository
2. Install required libraries:
     pip install tweepy pandas textblob
3. Set up your Twitter API credentials in the script
4. Run the script:
  python twitter_sentiment_analyzer.py
## Future Enhancements
- Implement more advanced natural language processing techniques
- Add visualization of sentiment trends over time
- Create a web interface for real-time analysis
- Expand analysis to include hashtag tracking and user mention analysis

## Ethical Considerations
This tool is designed for educational and research purposes. Users should comply with Twitter's terms of service and API usage guidelines. Respect user privacy and use the data responsibly.

## Contribution
Contributions to this project are welcome! Feel free to fork the repository and submit pull requests with improvements or additional features.

## License
This project is open source and available under the [MIT License](LICENSE).

---

Created by Josh Plotkin -

Note: Due to changes in Twitter's API policies as of 2023, access to certain endpoints may require a paid API plan. Always check the current Twitter API documentation and adjust the code accordingly.
