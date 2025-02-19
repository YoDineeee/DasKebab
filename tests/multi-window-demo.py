import os
import multiprocessing
import matplotlib.pyplot as plt
from kivy_matplotlib_widget.tools.interactive_converter import app_window,app_window_3D
import numpy as np
# from interactive_converter3D import app_window_3D
# from interactive_converter import app_window

def generate_plot(kwargs):
    """Function to generate and display the plot."""
    num = kwargs['num']
    if num == 1:
        # 1. Line Plot (1D)
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        plt.figure()
        plt.plot(x, y)
        plt.title("Line Plot")
        app_window(plt.gcf())
    elif num == 2:
        # 2. Scatter Plot (2D)
        x = np.random.rand(100)
        y = np.random.rand(100)
        plt.figure()
        plt.scatter(x, y)
        plt.title("Scatter Plot")
        app_window(plt.gcf())


if __name__ == "__main__":
    # Set the multiprocessing start method
    multiprocessing.set_start_method("spawn")

    # Place Kivy imports here to ensure they're only in the main process
    from kivy.app import App
    from kivy.uix.button import Button
    from kivy.uix.boxlayout import BoxLayout


    class PlottingApp(App):
        def build(self):
            layout = BoxLayout(orientation="vertical")

            b1 = Button(text="1 'Line Plot'")
            b1.bind(on_press=lambda x: self.generate_plot(1))
            b2 = Button(text="2 'Scatter Plot'")
            b2.bind(on_press=lambda x: self.generate_plot(2))


            for b in (b1, b2):
                layout.add_widget(b)

            return layout

        def generate_plot(self, num):
            x = [1, 2, 3, 4, 5]
            y = [i ** 2 for i in x]
            kwargs = {'data': (x, y), 'num': num}
            plot_process = multiprocessing.Process(target=generate_plot, args=(kwargs,))
            plot_process.start()
            self.plot_processes.append(plot_process)

        def on_stop(self):
            for process in self.plot_processes:
                if process.is_alive():
                    process.terminate()
            super().on_stop()

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.plot_processes = []


    PlottingApp().run()