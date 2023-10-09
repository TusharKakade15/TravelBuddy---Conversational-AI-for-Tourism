# import requests

# # Replace YOUR_OPENTRIPMAP_API_KEY and YOUR_OPENSTREETMAP_EMAIL with your actual API key and email address
# OPENTRIPMAP_API_KEY = 'API KEY'
# OPENSTREETMAP_EMAIL = '@gmail.com'

# # Prompt the user to enter their location or favorite places
# location = input("Enter your location or favorite places: ")

# # Call the OpenTripMap API to search for tourist places near the location
# response = requests.get(f'https://api.opentripmap.com/0.1/en/places/geoname?name={location}&apikey={OPENTRIPMAP_API_KEY}')
# response_json = response.json()

# # Get the latitude and longitude of the location
# lat = response_json['features'][0]['geometry']['coordinates'][1]
# lng = response_json['features'][0]['geometry']['coordinates'][0]

# # Define the types of places to search for
# place_types = ['beach', 'hill']

# # Call the OpenTripMap API to search for places of the specified types near the location
# response = requests.get(f'https://api.opentripmap.com/0.1/en/places/radius?radius=50000&lon={lng}&lat={lat}&kinds={",".join(place_types)}&apikey={OPENTRIPMAP_API_KEY}')
# response_json = response.json()

# # Prompt the user to enter their favorite places
# favorite_places = input("Enter your favorite places (comma-separated): ").split(',')

# # Call the OpenStreetMap API to search for the user's favorite places
# favorite_places_result = []
# for favorite in favorite_places:
#     response = requests.get(f'https://nominatim.openstreetmap.org/search?q={favorite}&format=json&email={OPENSTREETMAP_EMAIL}')
#     response_json = response.json()
#     if len(response_json) > 0:
#         favorite_places_result.append(response_json[0])

# # Print the name and address of each place
# for place in response_json['features']:
#     print(place['properties']['name'])
#     print(place['properties']['address'])

# # Print the name and address of each favorite place
# for place in favorite_places_result:
#     print(place['display_name'])



# import requests
# import json
# from geopy.distance import distance

# # Get user's location from input
# user_location = input("Enter your location (e.g. 'Los Angeles, CA'): ")

# # Set up the API endpoint and parameters
# endpoint = "https://nominatim.openstreetmap.org/search"
# params = {
#     "q": user_location,
#     "format": "json",
#     "addressdetails": 1,
#     "limit": 1,
# }

# # Get the latitude and longitude of the user's location using the OpenStreetMap Nominatim API
# response = requests.get(endpoint, params=params)
# location_data = response.json()[0]["address"]
# user_lat = float(location_data.get("lat", 0))
# user_lon = float(location_data.get("lon", 0))

# # Set up the API endpoint and parameters for OpenTripMap
# endpoint = "https://api.opentripmap.com/0.1/en/places/radius"
# params = {
#     "radius": 10000,  # radius in meters
#     "lon": user_lon,
#     "lat": user_lat,
#     "kinds": "sightseeing,natural",
#     "limit": 10,  # number of results to return
#     "format": "json",
#     "apikey": "API KEY",
# }

# # Get the nearby tourist places using the OpenTripMap API
# response = requests.get(endpoint, params=params)
# places = response.json()

# # Print the nearby tourist places and their ratings
# print("Nearby tourist places:\n")
# for place in places:
#     name = place.get("name", "Unknown")
#     rating = place.get("rate", "Unknown")
#     lat = float(place.get("point", {}).get("lat", 0))
#     lon = float(place.get("point", {}).get("lon", 0))
#     if lat and lon:
#         dist = round(distance((user_lat, user_lon), (lat, lon)).km, 2)
#         print(f"{name} (Rating: {rating}, Distance: {dist} km)")



# Import pandas package
import pandas as pd
import numpy as np
import requests
from geopy.distance import geodesic
import colorama
from colorama import Fore, Style
import pyshorteners
	
def user_pl(city,intr):
    if city==None:
        city= "smt indira gandhi college of engineering"

    # Define a dictionary containing data
    # data = {'City':['Bangalore', 'Mumbai', 'Chennai', 'Delhi']}
    user_interests=""
    # city = input("what's you'r location: ")
    # inter=input("tell you'r interest: ").lower() #.split()
    # print(inter)
    inter=""
    if intr!= None:
        inter=intr.lower()
    
    if inter in ["temple","templ","mandir","hindu temple","budhh temple","buddhist temple","temples","hindu temples","buddhist temples","gurudwara","temples"]:
        user_interests+="hindu_temples,buddhist_temples,other_temples,egyptian_temples,"
    if inter in ["church","jesus","catholic","christian","christianity","churchs","churches","church's","churche"]:
        user_interests += "churches,cathedrals,"
    if inter in ["mosque", "islamic mosque", "mosques","masjid","jama masjid","mosq","majjid"]:
        user_interests += "mosques,"
    if inter in ["religion","religious","spiritual","religis","god","religious place"]:
        user_interests += "religion,"
    if inter in ["island","islands","desert island"]:
        user_interests+= "islands,"
    if inter in ["spring","springs","hot springs","hot spring"]:
        user_interests+= "natural_springs,"
    if inter in ["caves","cave","mountain","mountains","volcanoes","volcano",]:
        user_interests+= "geological_formations,"
    if inter in ["lakes","lake","rivers","river","canals","canal","pond","ponds"]:
        user_interests+= "water,"
    if inter in ["water fall","waterfall","water","waterfalls"]:
        user_interests+= "waterfalls,"
    if inter in ["beaches","beach","chaupati","chowpatty","beachs","beach's"]:
        user_interests+= "beaches,"
    if inter in ["wildlife","wild","wildlife reserve","national parks","national park","aquatic"]:
        user_interests+= "nature_reserves,"
    if inter in ["nature","natural"]:
        user_interests+= "natural,"
    if inter in ["museums","museum","science","planetariums","art","gallaries","gallary","zoo","zoos","scientific"]:
        user_interests+= "museums,"
    if inter in ["aquariums","aquarium's","aquatic","aqua","aquarium"]:
        user_interests+= "aquariums,"
    if inter in ["theater","theaters","movie","movies","entertainment","entertainments","theatre","theatres"]:
        user_interests+= "theatres_and_entertainments,"
    if inter in ["parks","park","fountain"]:
        user_interests+= "urban_environment,"
    if inter in ["cultural","culture","cultures"]:
        user_interests+= "cultural,"
    if inter in ["fort","forts","killa","gad","castle","castles","fortifications","fortification"]:
        user_interests+= "fortifications,"
    if inter in ["historic","history","battlefields","archaeology","archaeological"]:
        user_interests+= "historic,"
    if inter in ["monuments","historical monument","historical monuments","monument","milestone","milestones","memorials","memorial"]:
        user_interests+= "monuments_and_memorials,"
    if inter in ["historic architecture","historic architectures"]:
        user_interests+= "historic_architecture"
    if inter in ["bridge","bridges","architecture","architectures"]:
        user_interests+= "architecture,"
    if inter in ["tourist","tour","interesting","family","friendly","family-friendly","anythig","na","n/a"]:
        user_interests+= "interesting_places,"
    if len(user_interests)==0:
        user_interests+= "interesting_places,"
    # rad=input("radius (in Km): ")
    # radius=str(int(rad)*1000)
    # user_interests = [museums,foods,sport,religion,natural,cultural,architecture,historic,beaches,rivers,canals,waterfalls,national_parks,caves,mountain_peaks,islands,churches,mosques,hindu_temples]
    # inter="cultural,religion"
    # Convert the dictionary into DataFrame
    # df = pd.DataFrame(data)
        
    # Observe the result
    # df
    from geopy.exc import GeocoderTimedOut
    from geopy.geocoders import Nominatim

    # declare an empty list to store
    # latitude and longitude of values
    # of city column
    longitude = []
    latitude = []

    # function to find the coordinate
    # of a given city
    def findGeocode(city):
        
        # try and catch is used to overcome
        # the exception thrown by geolocator
        # using geocodertimedout
        try:
            
            # Specify the user_agent as your
            # app name it should not be none
            geolocator = Nominatim(user_agent="your_app_name")
            
            return geolocator.geocode(city)
        
        except GeocoderTimedOut:
            
            return findGeocode(city)	

    # each value from city column
    # will be fetched and sent to
    # function find_geocode
    # for i in (df["City"]):
        
    if findGeocode(city) != None:
            
        loc = findGeocode(city)
            
            # coordinates returned from
            # function is stored into
            # two separate list
        latitude.append(loc.latitude)
        longitude.append(loc.longitude)
        
        
        # if coordinate for a city not
        # found, insert "NaN" indicating
        # missing value
    else:
            latitude.append(np.nan)
            longitude.append(np.nan)
            # get_nearby_places(longi, lati, city,radius,rad,user_interests)
    # now add this column to dataframe  return def get_nearby_places(lon, lat,city,r,rkm,interest)
    # print("longitude= ",longitude)
    # print("latitude= ",latitude)


    def get_nearby_places(lon, lat,city,interest,intr):
                # url = f"https://api.opentripmap.com/0.1/en/places/radius?radius={r}&lon={lon}&lat={lat}&kinds={interest}&format=json&apikey=API KEY"

        url = f"https://api.opentripmap.com/0.1/en/places/radius?radius=5000&lon={lon}&lat={lat}&kinds={interest}&format=json&apikey=API KEY"
        response = requests.get(url)
        if response.status_code == 200:
            result = response.json()
            result_sorted = sorted(result, key=lambda x: x["rate"], reverse=True)
            data = result_sorted[:5]
            # s = pyshorteners.Shortener(api_key='API KEY')
            s = pyshorteners.Shortener()
            if len(data) > 0:
                nearby_places = []
                for place in data:
                    place_lat = place['point']['lat']
                    place_lon = place['point']['lon']
                    distance = geodesic((lat, lon), (place_lat, place_lon)).km
                    place_name = place['name']
                    rating = place['rate']
                    google_maps_url = f"https://www.google.com/maps/search/?api=1&query={place_lat},{place_lon}"
                    # place_info = (f"{Fore.BLUE}{place_name}{Style.RESET_ALL}\nDistance from {city}: {distance:.2f} km\nRating: {rating}\n{Fore.GREEN}Directions: {google_maps_url}{Style.RESET_ALL}")
                    # nearby_places.append(place_info)
                    # short_url = s.bitly.short(google_maps_url)
                    short_url = s.tinyurl.short(google_maps_url)
                    
                    nearby_places.append(f"{place_name} \n{short_url} \nDistance from {city}: {distance:.2f} km \nRating: {rating}")
                    # nearby_places.append(f"{place_name}\nDistance from {city}: {distance:.2f} km\nRating: {rating}")
                # nearby_places = [f"{place['name']}\nRating: {place['rate']}" for place in data]
                out= (f"Here are some nearby places:\n" + "\n".join(nearby_places))
                return out
                # print (out)
            else:
                return(f"No {intr} found near {city}.")
        else:
            return("Error connecting to OpenTripMap API.")
        # print(interest)
    # print(user_interests)
    # Example usage:
    longi=longitude[0]
    lati=latitude[0]
    # print("longitude=",longi)
    # print("latitude= ", lati)
    return get_nearby_places(longi, lati, city,user_interests,intr)
print(user_pl(" ulhasnagar","temples"))