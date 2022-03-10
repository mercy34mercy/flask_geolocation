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

            keys = 0
            for n in place_detail['result']['photos']:
                
                print(n['photo_reference'])
                photoreference_array['photo'].append(n['photo_reference'])
                if(keys == 2):
                    break
                keys+=1
                
                

            add_data=({
                "name": i['name'],
                "url" : place_detail['result']['url'],
                "website" : place_detail['result']['website'],
            })

            jsonify['data'].append(add_data)
            jsonify['photos'].append(photoreference_array)
            
            print("adddata",add_data)
            if(key == 10):
                return jsonify
        except:
            print('近くにカフェがありません')
            return '近くにカフェがありません'
        pass
        
    return jsonify