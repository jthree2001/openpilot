from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout

import cereal.messaging as Messaging

class ShowMessages(FloatLayout):

  def __init__(self, **kwargs):
    super(ShowMessages, self).__init__(**kwargs)

    # self.label_1 = Label(text="""Loading""", markup=True)
    # self.add_widget(self.label_1 )
    print("loading...")

    self.data_array = ["frame", "frontFrame", "wideFrame", "thumbnail"]
    self.sm = Messaging.SubMaster(self.data_array)

    self.schedule = Clock.schedule_interval(self.update, 20.0 / 60.0)

  def delete(self):
    self.schedule.cancel()
    self.remove_widget(self.label_1)

  def update(self, dt):
    self.sm.update

    for i in self.data_array:
      print('{key}, {value}'.format(key=i, value=self.sm[i]))
      

    # car_messages = ["carState", "model", "radarState", "sensorEvents", "carParams", "modelV2"]

    # camera_messages = ["frame", "frontFrame", "wideFrame", "thumbnail"]

    # driver_state_messages = ["dMonitoringState", "driverState", "frontFrame"]

    # device_state = ["thermal", "health", "model", "liveLocationKalman", "logMessage", "androidLog", "cameraOdometry"]

    # path_messages = ["plan","pathPlan"]

    # other = ["uiLayoutState", "cameraOdometry", "liveCalibration" ]
