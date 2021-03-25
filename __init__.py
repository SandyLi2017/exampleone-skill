from mycroft import MycroftSkill, intent_file_handler


class Exampleone(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('exampleone.intent')
    def handle_exampleone(self, message):
        self.speak_dialog('exampleone')


def create_skill():
    return Exampleone()

