"""
This is the main application for runnnimg `vagn`.
"""

from interface import MPDClient

import sys

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.adapters.simplelistadapter import SimpleListAdapter
from kivy.properties import ListProperty

class MusicWidget(BoxLayout):
    pass

def song_converter(r_id, song):
    return {
        'text': song,
        'id': r_id,
        'height': 32,
    }

class VagnApp(App):
    
    songs = ListProperty([])

    def build(self):
        widget = MusicWidget()

        widget.song_list.adapter = SimpleListAdapter(
            data=self.songs,
            template='SongListTemplate',
            args_converter=song_converter
        )
        return widget
    
    def add_song(self, name):
        self.songs.append(name)

    def remove_song(self, id_):
        del self.songs[id_]

    def move_song(self, id_):
        if id_ > 0:
            self.songs[id_ - 1], self.songs[id_] = \
                self.songs[id_], self.songs[id_ - 1]

    def exit(self):
        sys.exit(0)
        

if __name__ == '__main__':
    VagnApp().run()
