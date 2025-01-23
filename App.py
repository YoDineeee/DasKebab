from kivymd.app import MDApp
from kivymd.uix.widget import MDWidget

class ExampleFirst(MDWidget):
    pass

class ExampleApp(MDApp):
    def build(self):
        return ExampleFirst()

if __name__ == '__main__':
    ExampleApp().run()