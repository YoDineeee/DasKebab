from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.card import Card
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.properties import NumericProperty
from multiprocessing import Process


class OrderCard(BoxLayout):
    _card_count = NumericProperty(0)
    
    def __init__(self, **kwargs):
        OrderCard._card_count += 1
        super().__init__(size_hint=(1, None), height=100, padding=8, **kwargs)
        
        layout = RelativeLayout()
        
        label = Label(
            text=f"Order Added {OrderCard._card_count}",
            color=(0.5, 0.5, 0.5, 1),
            size_hint=(None, None),
            pos_hint={"center_y": 0.5, "center_x": 0.5},
            bold=True
        )
        layout.add_widget(label)
        
        buttons_layout = BoxLayout(
            orientation='horizontal',
            size_hint=(None, None),
            width=96,
            height=48,
            pos_hint={"top": 1, "right": 1},
            spacing=4
        )
        
        edit_btn = Button(
            text="Edit",
            size_hint=(None, None),
            size=(48, 48),
            on_press=self.edit_card
        )
        delete_btn = Button(
            text="Delete",
            size_hint=(None, None),
            size=(48, 48),
            on_press=self.delete_card
        )
        
        buttons_layout.add_widget(edit_btn)
        buttons_layout.add_widget(delete_btn)
        layout.add_widget(buttons_layout)
        
        self.add_widget(layout)

    def delete_card(self, *args):
        parent = self.parent
        if parent:
            parent.remove_widget(self)

    def edit_card(self, *args):
        print("Entered menu")


class MainScreen(Screen):
    def add_order(self):
        stack = self.ids.stack
        stack.add_widget(OrderCard(size_hint_y=None))


class MainNOMDApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        return sm


def run_app():
    MainNOMDApp().run()


if __name__ == '__main__':
    processes = [Process(target=run_app) for _ in range(2)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
