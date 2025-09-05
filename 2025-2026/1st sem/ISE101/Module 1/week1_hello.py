from kivy.app import App
from kivy.uix.label import Label

class HelloWorld(App):
    def build(self):
        nameJCI = Label(
            text="BSIS 3A - Juliana Clair Ignacio!!",
            font_size='50sp'
        )
        return nameJCI

if __name__ == "__main__":
    HelloWorld().run()