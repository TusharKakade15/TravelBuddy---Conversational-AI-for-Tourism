import wikipedia 

def wikipedia_info(city):
    try:
        return wikipedia.summary(city, sentences=4)  
    except KeyError or ValueError:
        return "Didn't find any information about {}".format(city)
    
# print(wikipedia_info("kochi"))