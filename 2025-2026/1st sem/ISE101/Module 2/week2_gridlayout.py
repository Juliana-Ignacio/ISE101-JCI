from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class CombinedDemo(App):
    def build(self):
        layoutJCI = BoxLayout(orientation="vertical", spacing=10, padding=10)

        grid = GridLayout(cols=3, spacing=10, size_hint_y=0.7)
        for i in range(1, 10):
            grid.add_widget(Button(text=f"Button {i}"))

        layoutJCI.add_widget(grid)

        for i in range(1, 4):
            layoutJCI.add_widget(Button(text=f"Button {i}"))

        return layoutJCI

if __name__ == "__main__":
    CombinedDemo().run()