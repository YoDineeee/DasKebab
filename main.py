from kivymd.app import MDApp
from kivymd.uix.widget import MDWidget
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty, ListProperty
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton, MDIconButton
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.boxlayout import MDBoxLayout

class OrderCard(MDCard):
    _card_count = 0
    
    def __init__(self, **kwargs):
        OrderCard._card_count += 1
        super().__init__(
            padding="8dp",
            size_hint=(1, None),
            height="100dp",
            **kwargs
        )
        
        layout = MDRelativeLayout()
        
        label = MDLabel(
            text=f"Order Added {OrderCard._card_count}",
            adaptive_size=True,
            text_color="grey",
            pos_hint={"center_y": 0.5, "center_x": 0.5},
            bold=True
        )
        layout.add_widget(label)
        
        buttons_layout = MDBoxLayout(
            orientation='horizontal',
            size_hint=(None, None),
            width="96dp",
            height="48dp",
            pos_hint={"top": 1, "right": 1},
            spacing="4dp"
        )
        
        edit_btn = MDIconButton(
            icon="square-edit-outline",
            on_press=self.edit_card,
            size=("24dp", "24dp")
        )
        delete_btn = MDIconButton(
            icon="trash-can-outline",
            on_press=self.delete_card,
            size=("24dp", "24dp")
        )
        
        buttons_layout.add_widget(edit_btn)
        buttons_layout.add_widget(delete_btn)
        layout.add_widget(buttons_layout)
        
        self.add_widget(layout)

    def delete_card(self, *args):
        parent = self.parent
        parent.remove_widget(self)

    def edit_card(self, *args):
        print("Entered menu")

class MainScreen(MDScreen):
    def add_order(self):
        stack = self.ids.stack
        stack.add_widget(OrderCard(size_hint_y=None))

class FirstPageApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Moccasin"
        return MainScreen()
    
if __name__ == '__main__':
    FirstPageApp().run()

