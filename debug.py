

from Mapapi.parsejson import parsejson

from Mapapi.process import process


def index():
    loc = {
	"lat": 35.6619707,
	"lng": 139.703795
}

    place_result = process(loc)
    json_data= parsejson(place_result)
    return json_data

index()