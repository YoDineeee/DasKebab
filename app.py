from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDButton, MDButtonText, MDButtonIcon
from kivy.animation import Animation

#still need to add more buttons and stuff and to work with other screen 
#count 1,2,3 viva This app 
# "".
# KV='''
# MDButton:

# '''

class MainApp(MDApp):   
   def build(self):
        self.theme_cls.primary_palette = "Wine"
        return (
            MDScreen(
                MDButton(
                    MDButtonIcon(
                        icon="plus",
                        
                    ),
                    MDButtonText(
                    text="blahblah"
                    ),
                  
                    style="elevated",
                    pos_hint={"center_x": 0.9, "center_y": 0.9},
                    
                ),
                md_bg_color=self.theme_cls.surfaceColor,
            )
        )


MainApp().run()



