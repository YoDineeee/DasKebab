from kivymd.app import MDApp
from kivymd.uix.widget import MDWidget
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty, ListProperty
from kivymd.uix.list import MDListItem
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton, MDIconButton
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.boxlayout import MDBoxLayout

class OrderCard(MDCard):
    # temporary order counting solution
    _card_count = 0
    
    def __init__(self, **kwargs):
        OrderCard._card_count += 1
        super().__init__(
            padding="4dp",
            size_hint=(1, None),
            **kwargs
        )
        
        # Main layout
        layout = MDRelativeLayout()
        
        # Label in the center
        label = MDLabel(
            text=f"Order Added {OrderCard._card_count}",
            adaptive_size=True,
            text_color="grey",
            pos_hint={"center_y": 0.5, "center_x": 0.5},
            bold=True
        )
        layout.add_widget(label)
        
        # Buttons layout in top right corner
        buttons_layout = MDBoxLayout(
            orientation='horizontal',
            size_hint=(None, None),
            size=(100, 48),
            pos_hint={"top": 1, "right": 1}
        )
        
        edit_btn = MDIconButton(
            icon="square-edit-outline",
            on_press=self.edit_card
        )
        delete_btn = MDIconButton(
            icon="trash-can-outline",
            on_press=self.delete_card
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
        stack.add_widget(OrderCard())

class FirstPageApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Moccasin"
        return MainScreen()
    
if __name__ == '__main__':
    FirstPageApp().run()


# TODO: 
# increase font_size for order button
# fix scrolling behaviour
# fix boxlayout icon positioning