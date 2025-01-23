from kivymd.app import MDApp
from kivymd.uix.widget import MDWidget
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivymd.uix.chip import MDChip, MDChipText
from kivymd.uix.list import MDListItem
from screen_nav import screen_helper

<<<<<<< HEAD
class SecondScreen(MDScreen):
    pass
class MainScreen(MDScreen):
    pass
=======
KV = '''          
<Root>:
    md_bg_color: self.theme_cls.backgroundColor  
    MDButton:
        style: "elevated"
        pos_hint: {"center_x": .9, "center_y": 0.9}
        on_press: root.add_order()
        MDButtonIcon:
            icon: "plus"

        MDButtonText:
            id: order_btn
            text: "Add Order"
'''
class Root(MDScreen):
    def add_order(self):
        Builder.load_string(KV)
        btn = self.ids.order_btn
        btn.text = "Order added"
>>>>>>> b6853cd0cbb5be7c3f70f148fab7c46bf646c33e


class FirstPageApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Moccasin"
        Builder.load_string(screen_helper)
        return MainScreen()
    
   



class SecondPageApp(MDApp):
    def build(self):
        self.theme_cls.theme_style ="Light"
        self.theme_cls.primary_palette = "Moccasin"
        Builder.load_string(screen_helper)
        return SecondScreen()




if __name__ == '__main__':
    FirstPageApp().run()