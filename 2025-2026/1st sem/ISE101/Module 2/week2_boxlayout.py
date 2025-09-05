from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class BoxLayoutDemo(App):
 def build(self):
    layoutJCI = BoxLayout(orientation="vertical", spacing=10, padding=10)
    layoutJCI.add_widget(Button(text="Button 1"))
    layoutJCI.add_widget(Button(text="Button 2"))
    layoutJCI.add_widget(Button(text="Button 3"))
    return layoutJCI

if __name__ == "__main__":
 BoxLayoutDemo().run()