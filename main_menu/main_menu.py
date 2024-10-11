import kivy
from kivy.app import App  
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder 
from kivy.uix.widget import Widget 
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image, AsyncImage
from kivymd.app import MDApp
from kivy.uix.image import Image

Builder.load_file('main_menu.kv')

class MainPage(RelativeLayout):
    pass

class TestApp(MDApp):  
    def build(self, **kwargs):  
        return MainPage()
        
if  __name__  ==  '__main__':  
        TestApp().run() 