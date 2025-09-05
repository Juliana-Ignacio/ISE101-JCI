from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class WidgetDemo(App):
    def build(self):
        layoutJCI = BoxLayout(orientation="vertical", padding=10, spacing=10)

        self.label = Label(text="Enter your name below:")
        self.text_input = TextInput(hint_text="Type here")
        submit = Button(text="Submit")
        clear = Button(text="Clear")

        submit.bind(on_press=self.on_submit)
        clear.bind(on_press=self.on_clear)

        layoutJCI.add_widget(self.label)
        layoutJCI.add_widget(self.text_input)
        layoutJCI.add_widget(submit)
        layoutJCI.add_widget(clear)

        return layoutJCI

    def on_submit(self, instance):
        name = self.text_input.text.strip()
        self.label.text = f"Hello, {name}!" if name else "Please enter a name."

    def on_clear(self, instance):
        self.text_input.text = ""
        self.label.text = "Enter your name below:"

if __name__ == "__main__":
    WidgetDemo().run()
