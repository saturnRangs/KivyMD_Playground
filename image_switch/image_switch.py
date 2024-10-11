from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.image import Image


#Example of using the KivyMD library to switch between images.
#Layout can be found in the image_switch.kv file

class image_switch(MDApp):
    def build(self):
        self.current_image = 0
        self.images = [
            "assets/picture_1.png",
            "assets/picture_2.png",
            "assets/picture_3.png",
            "assets/picture_4.png",
            "assets/picture_5.png",
        ]

        self.current_text = 0

        self.texts = [
            "This is a photo of a Spiral Galaxy",
            "This is the Death Star",
            "This object is unknown",
            "Stars!",
            "This is the Hubble Space Telescope"
        ]

        self.image_widget = Image(allow_stretch=True, keep_ratio=True)
        self.update_image()
        

    def on_start(self):
        # Set the initial theme and background color
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Purple'


    def switch_forward(self, *args):
        self.current_image = (self.current_image + 1) % len(self.images)
        self.current_text = (self.current_text + 1) % len(self.texts)
        self.update_image()

    def switch_backward(self, *args):
        self.current_image = (self.current_image - 1) % len(self.images)
        self.current_text = (self.current_text - 1) % len(self.texts)
        self.update_image()

    def update_image(self):
        self.root.ids.image_widget.source = self.images[self.current_image]
        self.root.ids.text_label.text = self.texts[self.current_image]
        self.root.ids.text_step.text = f"Picture {self.current_text + 1}"


if __name__ == '__main__':
    image_switch().run()