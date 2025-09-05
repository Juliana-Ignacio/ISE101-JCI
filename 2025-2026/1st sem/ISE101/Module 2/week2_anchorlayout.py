from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button

class AnchorLayoutDemo(App):
 def build(self):
    layoutJCI = AnchorLayout(anchor_x="left", anchor_y="top")
    layoutJCI.add_widget(Button(text="I’m in the corner!"))
    return layoutJCI

if __name__ == "__main__":
 AnchorLayoutDemo().run()