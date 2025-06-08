from utilityx.pythonx.user_interface.view import View

class Terminal(View):

    def __init__(self):
        pass

    def ask_input_with_hint_message(self, hint_message:str):
        return input(hint_message)