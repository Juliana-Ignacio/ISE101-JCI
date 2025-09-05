from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout 
from kivy.core.window import Window

Window.size = (300, 500)

class Calculator(BoxLayout):
    def _init_(self, **kwargs):
        super()._init_(orientation='vertical', **kwargs)

class CalculatorApp(App):
    def build(self):
        return Calculator()

if __name__ == '__main__':
    CalculatorApp().run()
