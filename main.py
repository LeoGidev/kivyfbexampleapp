from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class Post(BoxLayout):
    def __init__(self, username, text, image_src, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.padding = 10
        self.spacing = 10
        self.size_hint_y = None
        self.height = 300

        # Username label
        self.add_widget(Label(
            text=f"[b]{username}[/b]",
            size_hint_y=None,
            height=40,