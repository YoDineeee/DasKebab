from kivymd.app import MDApp
from kivymd.uix.widget import MDWidget
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.lang import Builder
from screen_thing import KV


class FirstPage(MDScreen):
    def add_order(self):
        btn = self.ids.order_btn
        btn.text = "Order added"


#this will be changed and  it is finished 
    # def switch_screen(self):
    #    MDSwapTransition()

       
    
class SecondPage(MDScreen):
    pass





class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Moccasin"
        Builder.load_string(KV)
        return  FirstPage()
    

 

if __name__ == '__main__':
    MainApp().run()