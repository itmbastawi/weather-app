from django.shortcuts import render
import requests
import json
# Create your views here.
def index(request):
    headers =  {
              'User-Agent': 'Request-Promise',
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip'
        }
    lat = 51.5
    lon = -0.25
    url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={}&lon={}'.format(lat,lon)
    api = requests.get(url,headers=headers)
    if api.status_code == 200:
        data = json.loads(api.text)
        units = data['properties']['meta']['units']
        last_updated = data['properties']['meta']['updated_at']
        days = data['properties']['timeseries']
        content = {'units':units,'last_updated':last_updated,
                    'days':days}
    else:
        content = {'units':None,'last_updated':None,
                    'days':None}
    return render(request,'weather/index.html',content)