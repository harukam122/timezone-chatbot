# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

#TODO: REPLACE wITH API CALL TO ACTUALLY RETRIEVE THE DATA
timezones = {
    "London": "UTC+1:00",
    "Sofia": "UTC+3:00",
    "Lisbon": "UTC+1:00",
    "Mumbai": "UTC+5:30"
}

class ActionShowTimeZone(Action):

    def name(self) -> Text:
        return "action_show_timezone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = tracker.get_slot("city")
        timezone = timezones.get(city)

        if timezone is None:
            output = "Could not find the timezone of {}".format(city)
        else:
            output = "Time zone of {} is {}".format(city, timezone)

        dispatcher.utter_message(text=output)

        return []
