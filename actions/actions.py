# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
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
            dispatcher.utter_message(' So so, du bist also {}'.format(personality_type))

        return []

# class yourTypeIs(Action):
#      def name(self):
#          return "action_yourTypeIs"
         
#      def run(self, dispatcher, tracker, domain):
#         personality_type = tracker.get_slot("personality_type")
#         if not personality_type :
#             dispatcher.utter_message(" Du hast mir deine personality nicht genannt :(")
#         else:
#             dispatcher.utter_message(' Du bist {}'.format(personality_type))
#         return []
       