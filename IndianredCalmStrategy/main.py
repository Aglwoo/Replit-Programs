import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
import matplotlib.pyplot as plt
import numpy as np



class BouncingBallApp(App):

    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # Input fields
        self.layout.add_widget(Label(text='Launch angle (degrees):'))
        self.angle_input = TextInput(multiline=False)
        self.layout.add_widget(self.angle_input)

        self.layout.add_widget(Label(text='Launch speed:'))
        self.speed_input = TextInput(multiline=False)
        self.layout.add_widget(self.speed_input)

        self.layout.add_widget(Label(text='Strength of gravity:'))
        self.gravity_input = TextInput(multiline=False)
        self.layout.add_widget(self.gravity_input)

        self.layout.add_widget(Label(text='Launch height:'))
        self.height_input = TextInput(multiline=False)
        self.layout.add_widget(self.height_input)

        self.layout.add_widget(Label(text='Coefficient of restitution:'))
        self.coeff_input = TextInput(multiline=False)
        self.layout.add_widget(self.coeff_input)

        self.layout.add_widget(Label(text='Number of bounces:'))
        self.bounces_input = TextInput(multiline=False)
        self.layout.add_widget(self.bounces_input)

        # Button
        self.plot_button = Button(text='Plot Trajectory')
        self.plot_button.bind(on_press=self.plot_trajectory)
        self.layout.add_widget(self.plot_button)

        # Image for displaying the plot
        self.image = Image()
        self.layout.add_widget(self.image)

        return self.layout

    def plot_trajectory(self, instance):
        # Get inputs
        an_launch_deg = float(self.angle_input.text)
        an_launch = np.radians(an_launch_deg)
        u = float(self.speed_input.text)
        g = float(self.gravity_input.text)
        h = float(self.height_input.text)
        C = float(self.coeff_input.text)
        N = float(self.bounces_input.text)

        # Constants
        n = 0
        inc = 0.01
        total_time = 100/inc

        # Initial speed
        x_speed = [u * np.cos(an_launch)]
        y_speed = [u * np.sin(an_launch)]

        # Initial position
        x = [0.0]
        y = [h]

        # Calculations
        for i in range(int(total_time)):
            if n >= N:
                break

            x_now = x[-1] + x_speed[-1]*inc + 0.5*(-g)*inc**2
            y_now = y[-1] + y_speed[-1]*inc + 0.5*(-g)*inc**2

            y_speed.append(y_speed[-1] -g*inc)

            if y_now < 0:
                y_now = 0
                y_speed[-1] = y_speed[-1] * -C
                n += 1

            x.append(x_now)
            y.append(y_now)

        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set(xlabel='x/m', ylabel='y/m', title='Bouncing Ball')
        ax.grid()
        fig.savefig("trajectory.png")
        plt.close(fig)

        # Display the plot in the Kivy Image widget
        self.image.source = 'trajectory.png'
        self.image.reload()

if __name__ == '__main__':
    BouncingBallApp().run()
