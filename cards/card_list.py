from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.swiper import MDSwiperItem
from kivy.utils import rgba, QueryDict


class card_list(MDApp):
    colors = QueryDict()
    colors.primary = rgba("#0c3b2e")
    colors.secondary = rgba("#bbcbc2")
    colors.warning = rgba("#ffba00")
    colors.danger = rgba("#E86767")
    colors.success = rgba("##6d9773")
    colors.white = rgba("#FFFFFF")
    colors.grey = rgba("#C4C4C4")
    colors.grey_light = rgba("#777a7a")
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        pass
    

    def my_callback(self):
        print("Button pressed")

    def card_click(self):
        print('Card clicked!')

    def on_swipe(self, swiper):
        # Handle swipe events here
        pass

if __name__ == '__main__':
    card_list().run()