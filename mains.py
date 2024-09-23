from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
API_URL = 'https://disease.sh/v3/covid-19'

@app.route('/global', methods=['GET'])
def get_global_stats():
    response = requests.get(f'{API_URL}/all')
    data = response.json()
    return jsonify({
        'cases': data['cases'],
        'deaths': data['deaths'],
        'recovered': data['recovered'],
        'new_cases': data['todayCases'],
        'new_deaths': data['todayDeaths'],
        'new_recovered': data['todayRecovered']
    })

# Endpoint to get COVID-19 stats by country
@app.route('/country/<country>', methods=['GET'])
def get_country_stats(country):
    response = requests.get(f'{API_URL}/countries/{country}')
    if response.status_code == 404:
        return jsonify({'error': 'Country not found'}), 404
    data = response.json()
    return jsonify({
        'country': data['country'],
        'cases': data['cases'],
        'deaths': data['deaths'],
        'recovered': data['recovered'],
        'new_cases': data['todayCases'],
        'new_deaths': data['todayDeaths'],
        'new_recovered': data['todayRecovered']
    })

@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to COVID-19 Tracker API!',
        'endpoints': {
            'global': '/global',
            'country': '/country/<country>',
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
