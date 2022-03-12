from audioop import add
from cgitb import text
from unicodedata import name
from Mapapi.createClient import createClient

def parsejson(place_results):
    
    jsonify = ({
        "data":[],
        "photos":[]
        })

    photoreference_array = ({
        "photo":[]
        })

    client = createClient()
    key = 0
    for i in place_results['results']:
        key+=1
        try:
            place_detail = client.place(place_id=i['place_id'])
            for n in place_detail['result']['photos']:
                photoreference_array['photo'].append(n['photo_reference'])
                break
                
                

            add_data=({
                "name": i['name'],
                "url" : place_detail['result']['url'],
                "website" : place_detail['result']['website'],
            })

            jsonify['data'].append(add_data)
            jsonify['photos'].append(photoreference_array)
            if(key == 10):
                return jsonify
        except:
            return '近くにカフェがありません'
        pass
        
    return jsonify