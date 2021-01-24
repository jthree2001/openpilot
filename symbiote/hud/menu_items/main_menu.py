from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label

from kivy.uix.textinput import TextInput


from symbiote.hud.menu_items.show_params import ShowParams
from symbiote.hud.menu_items.view_finder import ViewFinder
from symbiote.hud.menu_items.show_messages import ShowMessages


class MainMenu(Button):
  def __init__(self, **kwargs):
    super(MainMenu, self).__init__(**kwargs)

    self.text="Main Menu"
    self.drop_list = None
    self.drop_list = DropDown()

    btn = Button(text="Show Params", size_hint_y=None, height=50) 
    btn.bind(on_release=lambda btn: self.parent.add_widget(ShowParams()))
    self.drop_list.add_widget(btn)

    btn = Button(text="Show Messages", size_hint_y=None, height=50)
    btn.bind(on_release=lambda btn: ShowMessages())
    self.drop_list.add_widget(btn)

    btn = Button(text="Show Viewfinders", size_hint_y=None, height=50)
    btn.bind(on_release=lambda btn: self.parent.add_widget(ViewFinder()))
    self.drop_list.add_widget(btn)

    btn = Button(text="Clear screen", size_hint_y=None, height=50)
    btn.bind(on_release=lambda btn: self.parent.clear_widgets())
    self.drop_list.add_widget(btn)

    self.bind(on_release=self.drop_list.open)
    self.drop_list.bind(on_select=lambda instance, x: setattr(self, 'text', x))


