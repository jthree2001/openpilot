from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout

from common.params import Params

class ShowParams(FloatLayout):

  def __init__(self, **kwargs):
    super(ShowParams, self).__init__(**kwargs)

    self.label_1 = Label(text="""Loading""", markup=True)
    self.add_widget(self.label_1 )

    self.params = Params()

    self.schedule = Clock.schedule_interval(self.update, 5.0 / 60.0)

  def delete(self):
    self.schedule.cancel()
    self.remove_widget(self.label_1)

  def update(self, dt):
    self.label_1.text = """Car Params: {car_params}
      IsOffroad: {offroad}
      Passive: {Passive}
      CommunityFeaturesToggle: {CommunityFeaturesToggle}
      CompletedTrainingVersion: {CompletedTrainingVersion}
      IsRHD: {IsRHD}
      IsMetric: {IsMetric}
      RecordFront: {RecordFront}
      HasAcceptedTerms: {HasAcceptedTerms}
      HasCompletedSetup: {HasCompletedSetup}
      IsUploadRawEnabled: {IsUploadRawEnabled}
      IsLdwEnabled: {IsLdwEnabled}
      LastUpdateTime: {LastUpdateTime}
      OpenpilotEnabledToggle: {OpenpilotEnabledToggle}
      LaneChangeEnabled: {LaneChangeEnabled}
      IsDriverViewEnabled: {IsDriverViewEnabled}
      DisableUpdates: {DisableUpdates}
      Offroad_ConnectivityNeeded: {Offroad_ConnectivityNeeded}
      """.format(car_params=self.params.get("CarParams"), offroad=self.params.get("IsOffroad"), 
      Passive = self.params.get("Passive"), CommunityFeaturesToggle = self.params.get("CommunityFeaturesToggle"), 
      CompletedTrainingVersion = self.params.get("CompletedTrainingVersion"), IsRHD = self.params.get("IsRHD"),
      IsMetric = self.params.get("IsMetric"), RecordFront = self.params.get("RecordFront"), 
      HasAcceptedTerms = self.params.get("HasAcceptedTerms"), HasCompletedSetup = self.params.get("HasCompletedSetup"), 
      IsUploadRawEnabled = self.params.get("IsUploadRawEnabled"), IsLdwEnabled = self.params.get("IsLdwEnabled"), 
      LastUpdateTime = self.params.get("LastUpdateTime"), OpenpilotEnabledToggle = self.params.get("OpenpilotEnabledToggle"), 
      LaneChangeEnabled = self.params.get("LaneChangeEnabled"), IsDriverViewEnabled = self.params.get("IsDriverViewEnabled"), 
      DisableUpdates = self.params.get("DisableUpdates"), Offroad_ConnectivityNeeded = self.params.get("Offroad_ConnectivityNeeded"))