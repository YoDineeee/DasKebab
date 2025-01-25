KV = '''          
<FirstPage>:
    md_bg_color: self.theme_cls.backgroundColor  
    MDButton:
        style: "elevated"
        pos_hint: {"center_x": .9, "center_y": 0.9}
        on_press: root.add_order()
        MDButtonIcon:
            icon: "plus"

        MDButtonText:
            id: order_btn
            text: "Add Order"
 <SecondPage>:
    MDSegmentedButton:
         MDSegmentedButtonItem:
            text: "Menu"
            text:"Fast Food"
            text:"The snacks"
            text:"Drinks"





'''