from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.tools.patterns.MVC.Model import Model
from kivy.lang import Builder




class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Moccasin"
        
        Builder.load_string()
    
        return 

if __name__ == '__main__':
    MainApp().run()