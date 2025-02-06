from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDButton
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout
from multiprocessing import Process

# Define the Kivy layout using KV language
KV = '''
BoxLayout:
    orientation: 'vertical'
    MDLabel:
        text: "This is a window"
    MDButton:
        text: "Close"
        on_release: app.stop()
'''

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Moccasin"
        return Builder.load_string(KV)

def run_app():
    MainApp().run()

if __name__ == '__main__':
    # Launch two separate processes
    processes = [Process(target=run_app) for _ in range(2)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()