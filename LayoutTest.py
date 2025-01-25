from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

KV = """
<Order>:
    size_hint_y: None
    height: '80dp'

<OrdersBoxLayout>:
    orders: orders
    ScrollView:
        do_scroll_x: False
        do_scroll_y: True
        StackLayout:
            size_hint_y: None
            height: self.minimum_height
            size_hint_x: None
            width: '300dp'
            id: orders
    Widget:
    BoxLayout:
        size_hint_x: None
        width: '150dp'
        orientation: 'vertical'
        Button:
            size_hint_y: None
            height: '40dp'
            text: 'Add order'
            on_release:
                root.add_order()
        Widget:

OrdersBoxLayout:
"""

class Order(Button):
    pass

class OrdersBoxLayout(BoxLayout):
    _card_count = 0

    def add_order(self):
        self._card_count += 1
        self.orders.add_widget(Order(text=f"Order {self._card_count}"))


class MyApp(App):
    def build(self):
        return Builder.load_string(KV)

MyApp().run()