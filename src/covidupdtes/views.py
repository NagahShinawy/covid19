from django.shortcuts import render
from api_scripts.covid_api_scripts import covid_data


def home(request):
    data = covid_data()
    if data is not None:
        results = data['results']
        countries_objs = data['response']
        countries_names = [country['country'] for country in countries_objs]
        counts = len(countries_objs)
        data = {
            'covid_data': True,
            'results': results,
            'countries': countries_objs,
            'counts': counts,
            'countries_names': countries_names
        }
    else:
        data = {'covid_data': None}
    return render(request, 'covidupdtes/home.html', context=data)
