import requests
import os

api_key = os.environ.get('api_key')

def get_natural_disasters_by_events(limit=10, days=6 ):
    list_of_natural_disasters = []

    # get the url for the eonet api to get the natural disasters according to the givine limit and days
    url = (f'https://eonet.gsfc.nasa.gov/api/v2.1/events?api_key={api_key}&source=InciWeb,Eo&status=closed'
           f'&limit={limit}&days{days}'
           )

    response = requests.get(url)  # Send a GET request to the URL
    natural_disaster_by_events = response.json()  # Parse the JSON response into a Python dictionary

    for event_data in natural_disaster_by_events['events']:
        event_description = {
            'title': event_data['title'],
            'description': event_data['description'],
        }
        list_of_natural_disasters.append(event_description)

    return list_of_natural_disasters

l1 = get_natural_disasters_by_events()
print(l1)