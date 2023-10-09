# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.forms import FormValidationAction 
from . import textgeneration
from . import weather
from . import wiki
from . import places
from . import travel_forum
from rasa_sdk.events import SlotSet
import requests
import math



class ActionGetWeather(Action):
    """RETURN TODAY'S WEATHER"""
    
    def name(self):
        return "action_get_weather"
    
    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city = tracker.get_slot('location')
        # loca = tracker.latest_message.get('entities', [{'entity': 'location', 'value': None}])[-1]['value']
        # if city is None:
        #     # If the location slot is not set, extract the location from the entities
        #     loca = tracker.latest_message.get('entities', [{'entity': 'location', 'value': None}])[-1]['value']
        # else:
        #     loca = city

        msg=weather.weather_gen(city)
        dispatcher.utter_message(msg)
        # return [SlotSet("location", loca)]
        return [SlotSet("location", None)]


class ActionWiki(Action):
    """RETURN WIKIPEDIA'S SUMMARY"""
    
    def name(self):
        return "action_wiki"
    
    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city = tracker.get_slot('location')
        # loca = tracker.latest_message.get('entities', [{'entity': 'location', 'value': None}])[-1]['value']
        if city is None:
            # If the location slot is not set, extract the location from the entities
            loca = tracker.latest_message.get('entities', [{'entity': 'location', 'value': None}])[-1]['value']
        else:
            loca = city

        msg=wiki.wikipedia_info(city)
        dispatcher.utter_message(msg)
        # return [SlotSet("location", loca)]
        return [SlotSet("location", None)]


# class UserAddForm(FormValidationAction):
#     def name(self) -> Text:
#         return "user_add_form"
    
#     def run(self, dispatcher: CollectingDispatcher, 
#             tracker: Tracker, 
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         add=tracker.get_slot('user_address')

    

class ActionPlace(Action):
    """RETURN TOURIST PLACES"""
    
    def name(self):
        return "action_place"
    
    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # inter = tracker.get_slot('user_interest')
        add=tracker.get_slot('user_address')
        intr=tracker.get_slot('user_interest')
        # if intr is None:
        #     # If the user_interest slot is not set, extract the user_interest from the entities
        #     loci = tracker.latest_message.get('entities', [{'entity': 'user_interest', 'value': None}])[-1]['value']
        # else:
        #     loci = intr
        # if add is None:
        #     # If the user_interest slot is not set, extract the user_interest from the entities
        #     loca = tracker.latest_message.get('entities', [{'entity': 'user_address', 'value': None}])[-1]['value']
        # else:
        #     loca = add
        
        msg=places.user_pl(add,intr)
        dispatcher.utter_message(msg)
        return [SlotSet("user_address", None), SlotSet("user_interest", None)]
        # return [SlotSet("location", loca)]
        # return [SlotSet("user_interest", None)]



class ActionOutOfScope(Action):
    #GENERATES TEXT
    def name(self):
        return "action_out_of_scope"
    
    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        input = tracker.latest_message['text']
        answer = travel_forum.chatbot(input)
        if len(answer) == 0:
            msg = "Sorry, I can't handle that request"
        else:
            msg = answer
            
        dispatcher.utter_message(msg)

# class ActionTextGeneration(Action):
#     #GENERATES TEXT
#     def name(self):
#         return "action_generate_text"
    
#     def run(self, dispatcher: CollectingDispatcher, 
#             tracker: Tracker, 
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         input = tracker.latest_message['text']
#         answer = textgeneration.textGenerator(input)
#         if len(answer) == 0:
#             msg = "Sorry, I can't handle that request"
#         else:
#             msg = answer
            
#         dispatcher.utter_message(msg)
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
