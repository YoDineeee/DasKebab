from kivymd.app import MDApp
from kivymd.uix.widget import MDWidget
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty, ListProperty
from kivymd.uix.list import MDListItem
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton, MDIconButton
from kivymd.uix.relativelayout import RelativeLayout

class CustomCard(MDCard):
    _card_count = 0 
    def __init__(self, **kwargs):
        CustomCard._card_count += 1 
        super().__init__(
            padding="4dp", 
            size_hint=(1, None),
            **kwargs
        )
        layout = RelativeLayout()
        icon_btn = MDIconButton(
            icon="trash-can-outline",
            pos_hint={"top": 1, "right": 1},
            on_press=self.delete_card
        )
        label = MDLabel(
            text=f"Order Added {CustomCard._card_count}",
            adaptive_size=True,
            text_color="grey",
            pos_hint={"center_y": 0.5, "center_x": 0.5},
            bold=True
        )

        layout.add_widget(icon_btn)        
        layout.add_widget(label)
        self.add_widget(layout)

    def delete_card(self, *args):
        parent = self.parent
        parent.remove_widget(self)

class MainScreen(MDScreen):
    def add_order(self):
        stack = self.ids.stack
        stack.add_widget(CustomCard())


class FirstPageApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Moccasin"
        return MainScreen()
    

if __name__ == '__main__':
    FirstPageApp().run()


# TODO: 
# increase font_size
# fix scrolling behaviour