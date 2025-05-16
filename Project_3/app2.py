#Importing Librabries
import snscrape.modules.twitter as sntwitter
import pandas as pd
import pymongo
import streamlit as st


#Storing the scraped data in MongoDB
client = pymongo.MongoClient("")
    
# select database and collection
db = client.Twitter_data
collections=db.scrapped_tweets

# Define function to scrape Twitter Data
def scrape_twitter_data(keyword, start_date, end_date, tweet_limit):
    
    # Set up search query
    search_query = f"{keyword} since:{start_date} until:{end_date}"
    
    # Intitialize empty list to store scraped data
    scraped_data = []
   
    # Iterate through search results and append revelant data to list
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(search_query).get_items()):
       if i >= tweet_limit:
        break
       scraped_data.append([tweet.date, tweet.id, tweet.url, tweet.content, tweet.user.username, tweet.replyCount, tweet.retweetCount, tweet.lang, tweet.source, tweet.likeCount])
       
       # Convert scraped data to DataFrame
       scraped_data_df = pd.DataFrame(scraped_data, columns=['date', 'id', 'url', 'content', 'user', 'reply_count', 'retweet_count', 'language', 'source', 'like_count'])
 
    # Create dictionary with scraped data and metadata
    data = {
         'Scraped Word': keyword,
         'Scraped Date': pd.Timestamp.now(),
         'Scraped Data': scraped_data_df.to_dict(orient='records'),
    }
    
    # Insert data into MongoDB
    collections.insert_one(data)
   
    return scraped_data_df

# Set up Streamlit app interface

# Set page title
st.set_page_config(page_title='Twitter Scraper', page_icon=':bird:')

st.header('Twitter Data Scraper')
keyword = st.text_input('Enter a keyword or hashtag to search:')
start_date = st.date_input('Select a start date:')
end_date = st.date_input('Select an end date:')
tweet_limit = st.number_input('Number of Tweets to Scrape', min_value=1, max_value=1000, step=1)
    
# Scrape tweets and updload to database
if st.button('Scrape Twitter'):
   with st.spinner('Scraping Twitter tweets...'):
       scraped_data_df = scrape_twitter_data(keyword, start_date, end_date, tweet_limit)
       st.write(scraped_data_df)
       st.success('Data uploaded to MongoDB!')
    
# Convert dataframe to CSV and download it
if st.button('Download as CSV'):
       # download_data_csv()
       scraped_data_df = scrape_twitter_data(keyword, start_date, end_date, tweet_limit)
       csv = scraped_data_df.to_csv(index=False)
       st.download_button('Download CSV', data=csv, file_name='tweets.csv', mime='text/csv')
    
# Convert dataframe to JSON and download it
if st.button('Download as JSON'):
       scraped_data_df = scrape_twitter_data(keyword, start_date, end_date, tweet_limit)
       json = scraped_data_df.to_json(orient='records')
       st.download_button('Download JSON', data=json, file_name='tweets.json', mime='application/json')
