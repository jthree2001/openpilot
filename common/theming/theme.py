from common.theming.colors import Colors
import json
from common.params import Params

class Theme():

  colors = None
  def __init__(self, theme_colors = None):
    # TODO(Michael): I don't know, something incredible I guess
    if theme_colors:
      self.colors = theme_colors
    else:
      self.colors = Colors()
    

  def to_hash(self):
    temp_dic = {} 
    temp_dic["colors"] = self.colors.active_color
        
    return json.dumps(temp_dic)

  def to_rgb_hash(self):
    temp_dic = {}
    temp_dic["colors"] = self.colors.to_rgb()

    return json.dumps(temp_dic)

  def save(self):
    params = Params()
    params.put("Theming", self.to_rgb_hash())