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
            dispatcher.utter_message(" Du hast mir deine personality nicht genannt 😥")
        elif personality_type == "INTJ":
            dispatcher.utter_message('So so du bist also {}. Das ist supi.'.format(personality_type))
        elif personality_type == "INTP":
            dispatcher.utter_message("Du bist also INTP. Neugierig wa? 😏")
        elif personality_type == "ENTJ":
            dispatcher.utter_message("Du bist ENTJ")
        elif personality_type == "ENTP":
            dispatcher.utter_message("Du bist ENTP")
        elif personality_type == "INFJ":
            dispatcher.utter_message("Du bist INFJ. Soso das klingt krass mystisch! 🧙‍♂️")
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
            dispatcher.utter_message("Du bist ESFJ. Du kleiner social butterfly du. 🥰")
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
        
        listStile = ["Romantik", "Gotik", "Renaissance",
                     "Rokoko", "Klassizismus", "Realismus",
                     "Impressionismus","Naturalismus", "Symbolismus",
                     "Jugendstil","Expressionismus","Kubismus", "Dadaismus",
                     "Bauhaus", "Surrealismus",
                     "Pop-Art",
                     "Graffiti"]

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
        
        
        #dispatcher.utter_message("Dein gewählter Emoji ist ein {}".format(formen_choice))
        #dispatcher.utter_message("Meine Idee für dich wäre: \n 'Ein Fuchs, welcher in einem frostigen Wald eine magische Glaskugel findet'")

        return []

class ActionPrompt(Action):

    ### Die Action generiert einen Inspirationsprompt angepasst an die individuellen Entity-Slots


    def name(self):
        return "action_getPrompt"

    def run(self, dispatcher, tracker, domain):
        username = tracker.get_slot("username")
        personality_type = tracker.get_slot("personality_type")
        color = tracker.get_slot("color")
        art_style = tracker.get_slot("art_style")
        formen_choice = tracker.get_slot("formen_choice")
        
        chosenPromptPersonality = ""
        chosenPromptColor = ""
        chosenPromptForm = ""
        chosenPromptStyle = ""

        dispatcher.utter_message("Dein gewählter Emoji ist ein {}".format(formen_choice))

        # test entities (rausnehmen)
        # personality_type = "INTJ"
        # color = "grün"
        # art_style = "Barock"
        # formen_choice = "Herz"

        # Listen für jede Kategorie und Unterkategorien als Wahl des Users = Prompts für Satz  => in jeweilige Schleife für Übersicht
    

        
        # PERSONALITIES 

        if personality_type == "INFJ":
            """Funktion die Satzteil für passende Userantwort random auswählt"""

            randomZahl = random.randint(0,4) # hier nummer der prompts in liste einfügen - 1

            listePers = ["über den Sinn des Lebens philosophiert.", "entspannt.", "in die Sterne schaut.", "über Liebe nachdenkt.", "einen Comic liest."]

            # so für jede personality benennen 
            chosenPromptPersonality = listePers[randomZahl]

        elif personality_type == "INTP":

            randomZahl = random.randint(0,3) 
            listePers = ["mit genmutiertem Mais experimentiert.", "die Antarktis erforscht.", "einen Chatbot entwickelt.", "sich selbst feiert."]
            chosenPromptPersonality = listePers[randomZahl]

        elif personality_type == "ESFJ":

            randomZahl = random.randint(0,3) 
            listePers = ["Mensch-ärgere-dich-nicht spielt.", "Menschen beobachtet.", "sich unterhält.", "sich freut."]
            chosenPromptPersonality = listePers[randomZahl]

        # COLOR  

        if color == "Grün" or color == "Hellgrün" or color == "Dunkelgrün" or color == "Limette" or color == "Tannengrün" or color== "Grasgrün" or color=="Pastellgrün":

            randomZahl = random.randint(0,3) 

            listeColor = ["auf dem Moos", "hinter einem Baum", "neben einer Kuhweide", "unter einem Schmetterlingsschwarm"]

            chosenPromptColor = listeColor[randomZahl]

        elif color == "rot" or color == "hellrot" or color == "dunkelrot" or color == "pastellrot":

            randomZahl = random.randint(0,3) 

            listeColor = ["auf einem Dach", "am Meer bei Sonnenuntergang", "neben einem Papagei", "an einer Backsteinwand"]

            chosenPromptColor = listeColor[randomZahl]


        elif color == "gelb" or color=="Hellgelb" or color=="Pastellgelb":

            randomZahl = random.randint(0,3) 

            listeColor = ["in einer Blumenwiese", "unter der Mittagssonne", "inmitten von Sonnenblumen", "am Kamin"]

            chosenPromptColor = listeColor[randomZahl]

        elif color == "blau" or color == "hellblau" or color == "dunkelblau" or color == "pastellblau":

            randomZahl = random.randint(0,3) 

            listeColor = ["am tobenden Meer", "an der Küste", "an einem verwilderten Teich", "unter klarem Sternenhimmel"]

            chosenPromptColor = listeColor[randomZahl]

        elif color == "rosa" or color == "fuchsia" or color == "altrosa" or color == "pastellrosa":

            randomZahl = random.randint(0,3) 

            listeColor = ["in einem zugemüllten Garten", "in einem insolventen Blumengeschäft", "umgeben von verwelkten Rosen", "auf einer Hüpfburg"]

            chosenPromptColor = listeColor[randomZahl]

        elif color == "pink" or color == "pastellpink":

            randomZahl = random.randint(0,3) 

            listeColor = ["bei Barbie und Ken", "auf einer Tulpenwiese", "in einem Smarties Pool", "umgeben von einem knalligen Sonnenuntergang"]

            chosenPromptColor = listeColor[randomZahl]

        elif color == "lila" or color == "violett" or color == "purpur":

            randomZahl = random.randint(0,3) 

            listeColor = ["auf einem verlassenen Flughafen", "umgeben von bösen Schmetterlingen", "auf Höhe des Matterhorns", "auf einem Trampolin"]

            chosenPromptColor = listeColor[randomZahl]

        elif color == "schwarz":

            randomZahl = random.randint(0,3) 

            listeColor = ["in einem dunklen Wald", "Unter einem Wolkenlosen Sternenhimmel", "in einem dunklen Gang", "in einer Trauerweide"]

            chosenPromptColor = listeColor[randomZahl]   

        elif color == "weiß":

            randomZahl = random.randint(0,3) 

            listeColor = ["auf einem schneebedeckten Berg", "in einer verschneiten Straße", "in einem Mondkrater", "am Gipfelkreuz eines Berges"]

            chosenPromptColor = listeColor[randomZahl] 

        


        # FORMEN CHOICE 

        if formen_choice == "Herz":

            randomZahl = random.randint(0,3) 

            listeForm = ["Eine weiße Taube, die", "Ein verliebter Frosch, der", "Ein gerade geschlüpftes Küken, das", "Ein schöner Schwan, der"]

            chosenPromptForm = listeForm[randomZahl]

        elif formen_choice == "Blatt":

            randomZahl = random.randint(0,3) 

            listeForm = ["Ein süßer Fuchs, der", "Ein wilder Wolf, der", "Eine kleine Kuh, die", "Ein riesiger Schwarm Gänse, die"]

            chosenPromptForm = listeForm[randomZahl]

        elif formen_choice == "Kreis":

            randomZahl = random.randint(0,3) 

            listeForm = ["Ein exotischer Planet, der", "Eine lebende Uhr, die", "Ein untergegangenes Boot, das", "Ein meditierender Mönch, der"]

            chosenPromptForm = listeForm[randomZahl]

        elif formen_choice == "Dreieck":

            randomZahl = random.randint(0,4) 

            listeForm = ["Ein fliegendes Schiff, das", "Eine schnelle Libelle, die", "Ein lebender Tortilla Chip, der", "Ein kaputtes Verkehrsschild, das", "Ein wabbeliger Kugelfisch, der"]

            chosenPromptForm = listeForm[randomZahl]
        

        # ART STYLE 

             
         
        if art_style == "Romantik":

            randomZahl = random.randint(0,3) 

            listeStyle = ["altertümlich", "unterbewusst", "präzise", "verträumt"]

            chosenPromptStyle = listeStyle[randomZahl]

        elif art_style == "Gotik":

            randomZahl = random.randint(0,3) 

            listeStyle = ["ängstlich", "verkünstelt", "aufwendig", "dunkel"]

            chosenPromptStyle = listeStyle[randomZahl]

        elif art_style == "Renaissance":

            randomZahl = random.randint(0,3) 

            listeStyle = ["befreit", "lebhaft", "verspielt", "traditionell"]

            chosenPromptStyle = listeStyle[randomZahl]

        elif art_style == "Rokoko":

            randomZahl = random.randint(0,3) 

            listeStyle = ["verspielt", "exotisch", "ungewöhnlich", "schön"]

            chosenPromptStyle = listeStyle[randomZahl]

        elif art_style == "Klassizismus":

            randomZahl = random.randint(0,3) 

            listeStyle = ["gerade", "genau", "explizit", "gerne"]

            chosenPromptStyle = listeStyle[randomZahl]


        elif art_style == "Realismus":

            randomZahl = random.randint(0,3) 

            listeStyle = ["echt", "unsichtbar", "nur", "ungeschönt"]

            chosenPromptStyle = listeStyle[randomZahl]
        


        elif art_style == "Impressionismus":

            randomZahl = random.randint(0,3) 

            listeStyle = ["realistisch", "alltäglich", "gefühlvoll", "melancholisch"]

            chosenPromptStyle = listeStyle[randomZahl]


        elif art_style == "Naturalismus":

            randomZahl = random.randint(0,3) 

            listeStyle = ["friedlich", "im Einklang mit der Natur", "angenehm", "natürlich"]

            chosenPromptStyle = listeStyle[randomZahl]


        elif art_style == "Symbolismus":

            randomZahl = random.randint(0,3) 

            listeStyle = ["wütend", "anti-materialistisch", "sinnbildlich", "traumähnlich"]

            chosenPromptStyle = listeStyle[randomZahl]


        elif art_style == "Jugendstil":

            randomZahl = random.randint(0,3) 

            listeStyle = ["natursüchtig", "schöpferisch", "harmonisch", "idyllisch"]

            chosenPromptStyle = listeStyle[randomZahl]


        elif art_style == "Expressionismus":

            randomZahl = random.randint(0,3) 

            listeStyle = ["chaotisch", "laut", "ängstlich", "rebellisch"]

            chosenPromptStyle = listeStyle[randomZahl]


        elif art_style == "Kubismus":

            randomZahl = random.randint(0,3) 

            listeStyle = ["blass", "wenig", "verteilt", "unverfälscht"]

            chosenPromptStyle = listeStyle[randomZahl]

        elif art_style == "Dadaismus":

            randomZahl = random.randint(0,3) 

            listeStyle = ["belustigt", "veräppelnd", "unvernünftig", "chaotisch"]

            chosenPromptStyle = listeStyle[randomZahl]


        elif art_style == "Bauhaus":

            randomZahl = random.randint(0,3) 

            listeStyle = ["flach", "revolutionär", "nur", "anders als normal"]

            chosenPromptStyle = listeStyle[randomZahl]



        elif art_style == "Surrealismus":

            randomZahl = random.randint(0,3) 

            listeStyle = ["verträumt", "unterbewusst", "automatisch", "fremdgesteuert"]

            chosenPromptStyle = listeStyle[randomZahl]


        elif art_style == "Pop-Art":

            randomZahl = random.randint(0,3) 

            listeStyle = ["popkulturell", "leuchtend", "comic-haft", "bunt"]

            chosenPromptStyle = listeStyle[randomZahl]



        elif art_style == "Graffiti":

            randomZahl = random.randint(0,3) 

            listeStyle = ["wild", "revolutionär", "rebellisch", "bunt"]

            chosenPromptStyle = listeStyle[randomZahl]




        # zusammensetzen des gesamten prompts 
        wholePrompt = "Deine personalisierte Idee ist: \n" + chosenPromptForm + " " + chosenPromptColor + " " + chosenPromptStyle + " " + chosenPromptPersonality

        dispatcher.utter_message(wholePrompt)

        return []

