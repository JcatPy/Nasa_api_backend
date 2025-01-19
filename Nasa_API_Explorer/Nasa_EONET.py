import requests
import os

api_key = os.environ.get('api_key')

def get_natural_disasters_by_events(limit=5, days=20, status='open' ):
    list_of_natural_disasters = []

    # get the url for the eonet api to get the natural disasters according to the givine limit and days
    url = (f'https://eonet.gsfc.nasa.gov/api/v2.1/events?api_key={api_key}&source=InciWeb,Eo&status={status}'
           f'&limit={limit}&days{days}'
           )

    response = requests.get(url)  # Send a GET request to the URL
    natural_disaster_by_events = response.json()  # Parse the JSON response into a Python dictionary
    print(natural_disaster_by_events)
    for event_data in natural_disaster_by_events['events']:
        event_description = {
            'title': event_data['title'],
            'description': event_data['description'],
        }
        list_of_natural_disasters.append(event_description)

    return list_of_natural_disasters

def get_natural_disasters_by_categories(limit=5, days=6, status = 'open'):
    url = (f'https://eonet.gsfc.nasa.gov/api/v2.1/categories?api_key={api_key}source=InciWeb,Eo&status={status}'
           f'&limit={limit}&days{days}')
    list_of_natural_disasters = []

    response = requests.get(url) # Send a GET request to the URL
    natural_disaster_by_categories = response.json() # Parse the JSON response into a Python dictionary
    for categories in natural_disaster_by_categories['categories']:
        category_description = {
            'title': categories['title'], 
            'description': categories['description'],
        }
        list_of_natural_disasters.append(category_description)
    return list_of_natural_disasters

def get_natural_disasters_by_layers(limit=5, days=6, status = 'open'):
    url = (f'https://eonet.gsfc.nasa.gov/api/v2.1/layers?api_key={api_key}&source=InciWeb,Eo&status={status}'
           f'&limit={limit}&days{days}'
           )
    list_of_natural_disasters = []

    response = requests.get(url) # Send a GET request to the URL
    natural_disaster_by_layers = response.json() # Parse the JSON response into a Python dictionary
    print(natural_disaster_by_layers)


if __name__ == '__main__':
    get_natural_disasters_by_layers()




