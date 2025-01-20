from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDButton, MDButtonText, MDButtonIcon
from kivy.animation import Animation



class MainApp(MDApp):  
   def build(self):
        self.theme_cls.primary_palette = "Green"
        return (
            MDScreen(
                MDButton(
                    MDButtonIcon(
                        icon="plus",
                    ),
                   
                    style="elevated",
                    pos_hint={"center_x": 0.9, "center_y": 0.9},
                ),
                md_bg_color=self.theme_cls.surfaceColor,
            )
        )


MainApp().run()