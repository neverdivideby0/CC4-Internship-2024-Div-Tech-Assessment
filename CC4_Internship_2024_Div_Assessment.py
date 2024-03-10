import requests
import json
import pandas as pd
from pandas.errors import EmptyDataError

def load_restaurant_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = json.loads(response.text)
        return data
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None

def process_restaurants(data):
    restaurant_in_list = []
    for results_shown in data:
        for restaurant_info in results_shown['restaurants']:
            restaurant_data = restaurant_info['restaurant']
            restaurant_in_list.append({
                'restaurant_id': restaurant_data['id'],
                'restaurant_name': restaurant_data['name'],
                'country_id': restaurant_data['location']['country_id'],
                'city': restaurant_data['location']['city'],
                'user_rating_votes': restaurant_data['user_rating']['votes'],
                'user_aggregate_rating': float(restaurant_data['user_rating']['aggregate_rating']),
                'cuisines': restaurant_data['cuisines']
            })
    return pd.DataFrame(restaurant_in_list)

def load_country_codes(excel_file_path):
    try:
        return pd.read_excel(excel_file_path)
    except FileNotFoundError:
        print("Excel file not found.")
        return pd.DataFrame()
    except EmptyDataError:
        print("Excel file is empty.")
        return pd.DataFrame()

def merge_with_country_codes(restaurant_df, country_codes_df):
    final_df = restaurant_df.merge(country_codes_df, how='left', left_on='country_id', right_on='country_code')
    return final_df[['restaurant_id', 'restaurant_name', 'country', 'city', 'user_rating_votes', 
                     'user_aggregate_rating', 'cuisines']]

def extract_events(data):
    restaurant_events_list = []
    for results_shown in data:
        for restaurant_info in results_shown['restaurants']:
            restaurant_data = restaurant_info['restaurant']
            if 'zomato_events' in restaurant_data:
                for zomato_events in restaurant_data['zomato_events']:
                    event_details = zomato_events['event']
                    photo_url = event_details['photos'][0]['photo']['url'] if event_details['photos'] else "NA"
                    restaurant_events_list.append({
                        'event_id': event_details['event_id'],
                        'restaurant_id': restaurant_data['id'],
                        'restaurant_name': restaurant_data['name'],
                        'photo_url': photo_url,
                        'event_title': event_details.get('title', "NA"),
                        'event_start_date': event_details.get('start_date', "NA"),
                        'event_end_date': event_details.get('end_date', "NA"),
                    })
    return pd.DataFrame(restaurant_events_list)

def process_ratings(data):
    restaurant_ratings_list = []
    for results_shown in data:
        for restaurant_info in results_shown['restaurants']:
            restaurant_data = restaurant_info['restaurant']
            restaurant_ratings_list.append({
                'restaurant_id': restaurant_data['id'],
                'user_aggregate_rating': float(restaurant_data['user_rating']['aggregate_rating']),
                'rating_text': restaurant_data['user_rating']['rating_text']
            })
    restaurant_ratings_df = pd.DataFrame(restaurant_ratings_list)
    filtered_ratings_df = restaurant_ratings_df[restaurant_ratings_df["rating_text"].isin(["Excellent", "Very Good", "Good", "Average", "Poor"])]
    rating_aggregates = filtered_ratings_df.groupby("rating_text")["user_aggregate_rating"].agg(['min', 'max']).sort_values(by="min")
    return rating_aggregates

def main():
    restaurant_data_url = "https://raw.githubusercontent.com/Papagoat/brain-assessment/main/restaurant_data.json"
    excel_file_path = 'Country-Code.xlsx'

    data = load_restaurant_data(restaurant_data_url)
    if data is not None:
        #1. Extract the following fields and store the data as restaurants.csv.
        restaurant_df = process_restaurants(data)
        country_codes_df = load_country_codes(excel_file_path)
        if not country_codes_df.empty:
            country_codes_df.columns = ['country_code', 'country']
            final_restaurant_df = merge_with_country_codes(restaurant_df, country_codes_df)
            final_restaurant_df.to_csv('restaurants.csv', index=False)
        else:
            print("Failed to process country codes. The DataFrame is empty.")
        
        #2. Extract the list of restaurants that have past event in the month of April 2019 and store the data as restaurant_events.csv.
        events_df = extract_events(data)
        events_df['event_start_date'] = pd.to_datetime(events_df['event_start_date'], format='%Y-%m-%d')
        events_df['event_end_date'] = pd.to_datetime(events_df['event_end_date'], format='%Y-%m-%d')
        april_events_df = events_df[(events_df['event_end_date'] >= '2019-04-01') & (events_df['event_end_date'] <= '2019-04-30')]
        april_events_df.to_csv('restaurant_events.csv', index=False)
        
        #3.	From the dataset (restaurant_data.json), determine the threshold for the different rating text based on aggregate rating. Return aggregates for the following ratings only:
        rating_aggregates = process_ratings(data)
        print(rating_aggregates)
    else:
        print("Failed to load restaurant data.")

if __name__ == "__main__":
    main()
