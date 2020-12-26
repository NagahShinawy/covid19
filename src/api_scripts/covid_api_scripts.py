import requests
import pandas as pd
import os
API_KEY = os.environ['API_KEY']


def get_covid_data():
    url = "https://covid-193.p.rapidapi.com/statistics"
    headers = {
        'x-rapidapi-key': API_KEY,
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        print(response.json())
        counts = data['results']
        print(counts)
        pd.DataFrame(data['response'][:50]).to_excel('covid19.xlsx', index=False)
        return data
    return None
