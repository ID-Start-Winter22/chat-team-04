# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from sys import displayhook
from typing import Any, Text, Dict, List
from pyparsing import nestedExpr
import random 



from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionStoreUserName(Action):

    ### Diese Action ruft den Slot username aus den entities ab 

     def name(self):
         return "action_store_name"
         
     def run(self, dispatcher, tracker, domain):
        username = tracker.get_slot("username")
        print("Sender ID: ", tracker.sender_id)

        return []


class ActionUserName(Action):

    ### Diese Action ruft den Slot username auf 
    ### (noch nicht funktionierend: lowercase in uppercase zum speichern im slot verändern)


     def name(self):
         return "action_get_name"

     def run(self, dispatcher, tracker, domain):
        username = tracker.get_slot("username")
        username = username[0].upper() + username[1:]
        if not username :
            dispatcher.utter_message(" Du hast mir Deinen Namen nicht gesagt.")
        else:
            dispatcher.utter_message(' Du bist {}'.format(username))

        return []

class ActionStorePersonality(Action):

    ### Diese Action ruft den gespeicherten Slot personality_type ab und kürzt ihn auf 4 Zeichen 
    ### Außerdem fängt sie den Fehler ab, wenn der Slot nicht belegt ist. 

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


    ### Diese Action ruft den gespeicherten Slot personality_type auf
    ### und gibt je nach Slot Value verschiedene responses zurück 


     def name(self):
         return "action_yourTypeIs"
         
     def run(self, dispatcher, tracker, domain):
        username = tracker.get_slot("username")
        personality_type = tracker.get_slot("personality_type")
        personality_type = personality_type[:4]

        if not personality_type :
            dispatcher.utter_message(" Du hast mir deine personality nicht genannt :(")
        elif personality_type == "INTJ":
            dispatcher.utter_message('So so du bist also {}. Das ist supi.'.format(personality_type))
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

        

        dispatcher.utter_message('Ich kenne dich jetzt schon ein bisschen besser Matrose {}! Aber um dir die perfekte Idee zu liefern, muss ich dir noch drei Fragen stellen! An welche Farbe denkst du, wenn du das Wort Kreativität hörst?'.format(username))
        
        return []

class ActionStoreColor(Action):

    ### Diese Action speichert die gewählte Farbe des Nutzers 

     def name(self):
         return "action_store_color"
         
     def run(self, dispatcher, tracker, domain):
        color = tracker.get_slot("color")
        print("Sender ID: ", tracker.sender_id)

        return []

class ActionThisIsYourColorAndStyle(Action):

     ### Diese Action fragt die gewählte Farbe des Nutzers aus dem Slot ab und gibt custom Responses dazu zurück. 
     ### Danach fragt sie den präferierten Kunststil des Users ab. 
     ### Dafür werden für die Buttontitel als Variable 3 random Stile aus einer Liste von Kunsstilen übergeben.


     def name(self):
         return "action_this_is_your_color_and_question_two"

     def run(self, dispatcher, tracker, domain):
        color  = tracker.get_slot("color")
        color = color.lower()
        if color.lower() == "pink":
            dispatcher.utter_message('Deine ausgewählte Farbe ist {}! Das ist zufälligerweise auch meine Lieblingsfarbe... glaubt man kaum oder ;)?'.format(color))
        else:
            dispatcher.utter_message('Deine ausgewählte Farbe ist {}! Gute Wahl! .. Obwohl ich selber wohl pink wählen würde..'.format(color))
        
        listStile = ["Romantik", "Gotik", "Renaissance","Manierismus","Barock", \
                     "Rokoko","Klassizismus","Romantik","Realismus","PräRaffaelismus",
                     "Impressionismus","Naturalismus","Post-Impressionismus","Symbolismus",
                     "Jugendstil","Expressionismus","Kubismus","Futurismus","Dadaismus",
                     "Präzisionismus","Art Deco","Bauhaus","Surrealismus","Neue Sachlichkeit",
                     "Abstrakter Expressionismus","Pop-Art","Hyperrealismus",
                     "Neo-expressionismus","Graffiti","Suprematismus"]

        myList = random.sample(listStile, 3)
        styleOne, styleTwo, styleThree = myList

        art_style = tracker.get_slot("art_style")

        buttons = []

        buttons.append({"title": str(styleOne), "payload": str(styleOne)})
    
        buttons.append({"title": str(styleTwo), "payload": str(styleTwo)})

        buttons.append({"title": str(styleThree), "payload": str(styleThree)})

        dispatcher.utter_message(text= "Welchen Stil würdest du wählen?", buttons=buttons)

        print("Sender ID: ", tracker.sender_id)

        return []  

class ActionStoreStyle(Action):

    ### Diese Action ruft den Slot art_style auf in dem der gewählte Kunststil des Users gespeichert ist. 

     def name(self):
         return "action_store_Style"
         
     def run(self, dispatcher, tracker, domain):
        art_style = tracker.get_slot("art_style")
        print("Sender ID: ", tracker.sender_id)
        
        return []

class ActionForm(Action):

    ### Diese Action ruft den Slot mit dem gewählten Kunsstil des Nutzers auf und 
    ### gibt ihn in einer Response zurück 

     def name(self):
        return "action_this_is_your_style_and_question_three"

     def run(self,dispatcher, tracker, domain):
        art_style = tracker.get_slot("art_style")
        dispatcher.utter_message("Dein gewählter Stil ist {} hmm..außergewöhnlich...".format(art_style))

        # dispatcher.utter_message("Welchen Emoji würdest du zum texten nutzen?") # dialog ändern

        # buttons = []

        # buttons.append({"title": "blatt" , "payload": "Blatt"})
        # buttons.append({"title": "kreis", "payload": "Kreis"})
        # buttons.append({"title": "dreieck", "payload": "Dreieck"})
        # buttons.append({"title": "herz", "payload": "Herz"})

        # dispatcher.utter_message(buttons=buttons)

        return []

class ActionStoreForm(Action):

    ### Diese Action ruft den Slot mit der vom Nutzer gewählten Form aus und gibt ihn in einer Response zurück

     def name(self):
        return "action_store_formen"

     def run(self,dispatcher, tracker, domain):
        formen_choice = tracker.get_slot("formen_choice")
        print("Sender ID: ", tracker.sender_id)
        
        
        dispatcher.utter_message("Dein gewählter Emoji ist ein {}".format(formen_choice))

        return []
