from http import client

from Mapapi.createClient import createClient


def process(loc):
    client = createClient()
    place_results = client.places_nearby(
        location=loc, radius=5, keyword='カフェ', language='ja')
    
    return place_results

