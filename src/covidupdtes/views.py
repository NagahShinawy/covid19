from django.shortcuts import render
from api_scripts.covid_api_scripts import get_covid_data

data = get_covid_data()


def home(request):
    # print(request.GET)
    selected_country = request.GET.get('country')
    if data is not None:
        results = data['results']
        countries_objs = data['response']
        countries_names = [country['country'] for country in countries_objs]
        counts = len(countries_objs)
        covid_data = {
            'covid_data': True,
            'results': results,
            'countries': countries_objs,
            'counts': counts,
            'countries_names': countries_names
        }
        for country in countries_objs:
            if selected_country == country['country']:
                covid_data['selected_country'] = country
                break
    else:
        covid_data = {'covid_data': None}
    return render(request, 'covidupdtes/home.html', context=covid_data)


def single_country(request):
    pass
