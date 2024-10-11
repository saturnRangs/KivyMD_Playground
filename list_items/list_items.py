from kivy.lang import Builder
from kivymd.app import MDApp

#Example of using the KivyMD library to display entities in a list
#Layout can be found in the list_items.kv file

class CustomApp(MDApp):
    def build(self):
        return Builder.load_file('list_items.kv')
    
    def on_start(self):
        # Set the initial theme and background color
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Red'

if __name__ == '__main__':
    CustomApp().run()