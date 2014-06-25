"""
This is the main application for runnnimg `vagn`.
"""

from interface import MPDClient

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MusicWidget(BoxLayout):

    def add_song(self, name):
        self.songs.item_strings = []

class VagnApp(App):
    pass

if __name__ == '__main__':
    VagnApp().run()
