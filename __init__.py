import names
from ovos_workshop.intents import IntentBuilder
from ovos_workshop.skills import OVOSSkill

__author__ = 'jarbas'


class NamesSkill(OVOSSkill):

    def initialize(self):
        name_intent = IntentBuilder("SuggestNameIntent").require(
            "name").build()
        self.register_intent(name_intent, self.handle_name_intent)

        last_name_intent = IntentBuilder("SuggestLastNameIntent").require(
            "lastname").build()
        self.register_intent(last_name_intent, self.handle_last_name_intent)

        female_name_intent = IntentBuilder("SuggestFemaleNameIntent").require(
            "femalename").build()
        self.register_intent(female_name_intent,
                             self.handle_female_name_intent)

        male_name_intent = IntentBuilder("SuggestMaleNameIntent").require(
            "malename").build()
        self.register_intent(male_name_intent, self.handle_male_name_intent)

    def handle_name_intent(self, message):
        name = names.get_full_name()
        self.speak(name)

    def handle_last_name_intent(self, message):
        name = names.get_last_name()
        self.speak(name)

    def handle_female_name_intent(self, message):
        name = names.get_first_name("female")
        self.speak(name)

    def handle_male_name_intent(self, message):
        name = names.get_first_name("male")
        self.speak(name)
