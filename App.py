from kivymd.app import MDApp
from kivymd.uix.widget import MDWidget
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

KV = '''          
<Root>:
    md_bg_color: self.theme_cls.backgroundColor  
    MDButton:
        style: "elevated"
        pos_hint: {"center_x": .9, "center_y": 0.9}
        size: 100, 100
        MDButtonIcon:
            icon: "plus"

        MDButtonText:
            text: "Add Order"
'''
class Root(MDScreen):
    pass


class FirstPageApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Moccasin"
        Builder.load_string(KV)
        return Root()

if __name__ == '__main__':
    FirstPageApp().run()