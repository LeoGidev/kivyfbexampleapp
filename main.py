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
        self.background_color = (1, 1, 1, 1)  # Fondo blanco para cada post

        # Username label
        self.add_widget(Label(
            text=f"[b]{username}[/b]",
            size_hint_y=None,
            height=40,
            halign='left',
            markup=True,
            font_size=18,
            color=(0.23, 0.35, 0.60, 1),  # Azul oscuro estilo Facebook
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
            color=(0.15, 0.15, 0.15, 1),  # Gris oscuro para texto
        ))

        # Post image
        self.add_widget(Image(
            source=image_src,
            size_hint_y=None,
            height=150,
        ))

        # Like and Comment buttons
        buttons_layout = BoxLayout(size_hint_y=None, height=40, spacing=10, padding=5)
        buttons_layout.add_widget(Button(
            text="Like",
            background_color=(0.23, 0.35, 0.60, 1),  # Azul oscuro
            color=(1, 1, 1, 1),  # Texto blanco
        ))
        buttons_layout.add_widget(Button(
            text="Comment",
            background_color=(0.23, 0.35, 0.60, 1),  # Azul oscuro
            color=(1, 1, 1, 1),  # Texto blanco
        ))
        self.add_widget(buttons_layout)


class MainApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')

        # App Header
        header = BoxLayout(size_hint_y=None, height=60, padding=10, spacing=10, background_color=(0.23, 0.35, 0.60, 1))
        header.add_widget(Label(
            text="[b]My Social App[/b]",
            font_size=24,
            markup=True,
            halign='center',
            color=(1, 1, 1, 1),  # Blanco para texto
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
                image_src="C:\\Users\\Westnet\\Desktop\\imagenes elementos\\115x115x80.PNG"
            ))

        scroll_view.add_widget(feed)
        root.add_widget(scroll_view)

        return root


if __name__ == '__main__':
    MainApp().run()
