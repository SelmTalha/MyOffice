from kivy.app import App
from kivy.uix.button import Button

class calisma(App):
    def build(self):
        return Button(text ="Merhaba Selim")

if __name__ == "__main__":
    calisma().run()