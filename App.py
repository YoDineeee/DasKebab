from kivy.lang import Builder
from kivy.app import App
from kivy.uix.widget import Widget


class ExampleFirst(Widget):
    pass

class ExampleApp(App):
    def build(self):
        return ExampleFirst()

if __name__ == '__main__':
    ExampleApp().run()