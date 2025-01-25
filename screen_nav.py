screen_helper = '''          
<MainScreen>:
    md_bg_color: self.theme_cls.backgroundColor  
    BoxLayout:
        padding: [0, 0, 10,0]
        # spacing: 20
        ScrollView:
            do_scroll_x: False
            do_scroll_y: True
            BoxLayout:
                spacing: 15
                orientation: 'vertical'
                padding: 20
                MDCard:
                    padding: "4dp"
                    size_hint: 1, None
                    MDRelativeLayout:

                        MDIconButton:
                            icon: "dots-vertical"
                            pos_hint: {"top": 1, "right": 1}

                        MDLabel:
                            text: "HELLO"
                            adaptive_size: True
                            color: "grey"
                            pos: "12dp", "12dp"
                            bold: True
                MDCard:
                    padding: "4dp"
                    size_hint: 1, None
                    MDRelativeLayout:

                        MDIconButton:
                            icon: "dots-vertical"
                            pos_hint: {"top": 1, "right": 1}

                        MDLabel:
                            text: "HELLO"
                            adaptive_size: True
                            color: "grey"
                            pos: "12dp", "12dp"
                            bold: True
                MDCard:
                    padding: "4dp"
                    size_hint: 1, None
                    MDRelativeLayout:

                        MDIconButton:
                            icon: "dots-vertical"
                            pos_hint: {"top": 1, "right": 1}

                        MDLabel:
                            text: "HELLO"
                            adaptive_size: True
                            color: "grey"
                            pos: "12dp", "12dp"
                            bold: True
                MDCard:
                    padding: "4dp"
                    size_hint: 1, None
                    MDRelativeLayout:

                        MDIconButton:
                            icon: "dots-vertical"
                            pos_hint: {"top": 1, "right": 1}

                        MDLabel:
                            text: "HELLO"
                            adaptive_size: True
                            color: "grey"
                            pos: "12dp", "12dp"
                            bold: True
                MDCard:
                    padding: "4dp"
                    size_hint: 1, None
                    MDRelativeLayout:

                        MDIconButton:
                            icon: "dots-vertical"
                            pos_hint: {"top": 1, "right": 1}

                        MDLabel:
                            text: "HELLO"
                            adaptive_size: True
                            color: "grey"
                            pos: "12dp", "12dp"
                            bold: True                                                                                                                   
        MDButton:
            style: "elevated"
            pos_hint: {"center_y": 0.9}
            size: 100, 60
            on_press: root.add_order()
            MDButtonIcon:
                icon: "plus"

            MDButtonText:
                id: order_btn
                text: "Add Order"
                # font_size: "50sp"

<SecondScreen>:
    md_bg_color: self.theme_cls.backgroundColor  
    MDChip:
        pos_hint: {"center_x": .5, "center_y": .5}
        MDChipText:
            text: "Kebab"
            icon: "kebab"

'''
