from kivymd.app import MDApp
from kivymd.uix.widget import MDWidget
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivymd.uix.chip import MDChip, MDChipText
from kivymd.uix.list import MDListItem
# from screen_nav import screen_helper

class CustomerScreen(MDScreen):
    pass

class MainScreen(MDScreen):
    def add_order(self):
        # Builder.load_string(screen_helper)        
        btn = self.ids.order_btn


class FirstPageApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Moccasin"
        return MainScreen()
    
class SecondPageApp(MDApp):
    def build(self):
        self.theme_cls.theme_style ="Light"
        self.theme_cls.primary_palette = "Moccasin"
        # Builder.load_string(screen_helper)
        return CustomerScreen()


if __name__ == '__main__':
    FirstPageApp().run()

# TODO: 
# increase font_size
# fix scrolling behaviour