screen_helper = '''          
<MainScreen>:
    md_bg_color: self.theme_cls.backgroundColor  
    MDButton:
        style: "elevated"
        pos_hint: {"center_x": .9, "center_y": 0.9}
        size: 100, 100
        MDButtonIcon:
            icon: "plus"

        MDButtonText:
            text: "Add Order"
<SecondScreen>:
    MDChip:
        pos_hint: {"center_x": .5, "center_y": .5}

        MDChipText:
            text: "Kebab"
            icon: "kebab"

'''
