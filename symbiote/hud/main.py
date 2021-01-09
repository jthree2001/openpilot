from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector

from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class RootWidget(FloatLayout):
  def __init__(self, **kwargs):
    # make sure we aren't overriding any important functionality
    super(RootWidget, self).__init__(**kwargs)

    # let's add a Widget to this layout
    self.add_widget(
      Button(
        text="Hello World",
        size_hint=(.5, .5),
        pos_hint={'center_x': .5, 'center_y': .5}))

    def update(self, dt):
      print("need update camera here I suppose")


class HeadsUpDisplayApp(App):
    def build(self):
      self.root = RootWidget()

      #NOTE(Michael): this will force the UI to update every x interval, not sure what is optimal yet but will need to revist
      # Clock.schedule_interval(root.update, 1.0 / 60.0)

      return self.root




if __name__ == '__main__':
    HeadsUpDisplayApp().run()
