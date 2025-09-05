from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class CalculatorApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.display = Label(text="0", font_size=48, halign="right", valign="center")
        self.display.bind(size=self.display.setter('text_size'))
        root.add_widget(self.display)

        buttons = ['7','8','9','/', '4','5','6','*', '1','2','3','-', 'CLEAR','0','=','+']
        grid = GridLayout(cols=4, spacing=10)

        for b in buttons:
            btn = Button(text=b, font_size=32)
            btn.bind(on_press=self.on_press)
            grid.add_widget(btn)

        root.add_widget(grid)
        return root

    def on_press(self, button):
        text = button.text

        if text == 'CLEAR':
            self.display.text = '0'  # clear numbers, reset display
        elif text.isdigit():         # only allow digits to be typed
            self.display.text = text if self.display.text == '0' else self.display.text + text
        else:
            # ignore operators and '='
            pass

if __name__ == "__main__":
    CalculatorApp().run()
