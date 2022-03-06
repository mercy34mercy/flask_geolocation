import googlemaps
# import pprint

api_key="AIzaSyA-XS7P52yc7vUcY5JseKJViysWO-jEjMk"
client=googlemaps.Client(api_key)
#基準になる位置情報を検索
#geocode_resultにもらってきた座標を入れる
geocode_result=client.geocode('大阪府　鳳駅')
#緯度経度を取り出す小路
loc=geocode_result[0]['geometry']['location']
#半径１００km以内から取得
# print(geocode_result)
place_results = client.places_nearby(location=loc, radius=5, keyword='カフェ',language='ja')
# print(place_results['results'][0]['photos'])
for i in place_results['results']: 
    # place_detail = client.place(place_id=i['place_id']) 
    try: 
        print(i['name'],i['photos']) 
        # print(place_detail['result']['website']) 
    except: 
        print('近くにカフェがありません') 
        pass
# cafe_name=place_results['results']
# print(cafe_name)
# pprint.pprint(place_results)
# print(place_results)
