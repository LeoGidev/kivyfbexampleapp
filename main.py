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
            halign='left',
            markup=True,
            font_size=18,
        ))

        # Post content
        self.add_widget(Label(
            text=text,
            size_hint_y=None,
            height=80,
            halign='left',
            valign='top',
            text_size=(self.width, None),
            font_size=16,
        ))

        # Post image
        self.add_widget(Image(
            source=image_src,
            size_hint_y=None,
            height=150,
        ))

        # Like and Comment buttons
        buttons_layout = BoxLayout(size_hint_y=None, height=40)
        buttons_layout.add_widget(Button(text="Like"))
        buttons_layout.add_widget(Button(text="Comment"))
        self.add_widget(buttons_layout)


class MainApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')

        # App Header
        header = BoxLayout(size_hint_y=None, height=60, padding=10, spacing=10)
        header.add_widget(Label(
            text="[b]My Social App[/b]",
            font_size=24,
            markup=True,
            halign='center'
        ))
        root.add_widget(header)

        # Scrollable feed
        scroll_view = ScrollView()
        feed = GridLayout(cols=1, size_hint_y=None, spacing=10)
        feed.bind(minimum_height=feed.setter('height'))

        # Add example posts
        for i in range(5):
            feed.add_widget(Post(
                username=f"User {i + 1}",
                text=f"Here is a sample post content for User {i + 1}.",
                image_src="path_to_sample_image.jpg"  # Replace with an actual image path
            ))

        scroll_view.add_widget(feed)
        root.add_widget(scroll_view)

        return root


if __name__ == '__main__':
    MainApp().run()
