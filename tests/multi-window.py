from multiprocessing import Process

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

KV = '''
BoxLayout:
    orientation: 'vertical'

    Label:
        text: "This is a window"
    Button:
        text: "Close"
'''


class MainApp(App):
    def build(self):
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