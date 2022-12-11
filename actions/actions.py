# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from sys import displayhook
from typing import Any, Text, Dict, List
from pyparsing import nestedExpr

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionStoreUserName(Action):

     def name(self):
         return "action_store_name"
         
     def run(self, dispatcher, tracker, domain):
        username = tracker.get_slot("username")
        print("Sender ID: ", tracker.sender_id)

        return []


class ActionUserName(Action):

     def name(self):
         return "action_get_name"

     def run(self, dispatcher, tracker, domain):
        username = tracker.get_slot("username")
        if not username :
            dispatcher.utter_message(" Du hast mir Deinen Namen nicht gesagt.")
        else:
            dispatcher.utter_message(' Du bist {}'.format(username))

        return []

class ActionStorePersonality(Action):

     def name(self):
         return "action_store_personality"
         
     def run(self, dispatcher, tracker, domain):
        personality_type = tracker.get_slot("personality_type")
        personality_type = personality_type[:4]
        print("Sender ID: ", tracker.sender_id)

        if not personality_type :
            dispatcher.utter_message(" Du hast mir deine personality nicht genannt :(")
        else:
            pass 

        return []

class yourTypeIs(Action):
     def name(self):
         return "action_yourTypeIs"
         
     def run(self, dispatcher, tracker, domain):
        personality_type = tracker.get_slot("personality_type")
        personality_type = personality_type[:4]

        if not personality_type :
            dispatcher.utter_message(" Du hast mir deine personality nicht genannt :(")
        elif personality_type == "INTJ":
            dispatcher.utter_message('So so Du bist {}. Das ist toll'.format(personality_type))
        elif personality_type == "INTP":
            dispatcher.utter_message("Du bist INTP")
        elif personality_type == "ENTJ":
            dispatcher.utter_message("Du bist ENTJ")
        elif personality_type == "ENTP":
            dispatcher.utter_message("Du bist ENTP")
        elif personality_type == "INFJ":
            dispatcher.utter_message("Du bist INFJ")
        elif personality_type == "INFP":
            dispatcher.utter_message("Du bist INFP")
        elif personality_type == "ENFJ":
            dispatcher.utter_message("Du bist ENFJ")
        elif personality_type == "ENFP":
            dispatcher.utter_message("Du bist ENFP")
        elif personality_type == "ISTJ":
            dispatcher.utter_message("Du bist ISTJ")
        elif personality_type == "ISFJ":
            dispatcher.utter_message("Du bist ISFJ")
        elif personality_type == "ESTJ":
            dispatcher.utter_message("Du bist ESTJ")
        elif personality_type == "ESFJ":
            dispatcher.utter_message("Du bist ESFJ")
        elif personality_type == "ISTP":
            dispatcher.utter_message("Du bist ISTP")
        elif personality_type == "ISFP":
            dispatcher.utter_message("Du bist ISFP")
        elif personality_type == "ESTP":
            dispatcher.utter_message("Du bist ESTP")
        elif personality_type == "ESFP":
            dispatcher.utter_message("Du bist ESFP")

        return []
       