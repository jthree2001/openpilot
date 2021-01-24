class Colors():
  presets = [{
    "background": "#222629",
    "text": "#FFFFFF",
    "alert": "#86C232",
    "secondary_alert": "#61892F",
    "lane_highlight": "#6B6E70",
    "path_highlight": "#474B4F"
  },{
    "background": "#65CCB8",
    "text": "#182628",
    "alert": "#F2F2F2",
    "secondary_alert": "#57BA98",
    "lane_highlight": "#57BA98",
    "path_highlight": "#3B945E"
  }]

  active_color = {}

  def __init__(self, color_set=0):
    # TODO(Michael): I don't know, something incredible I guess
    self.active_color = self.presets[color_set]
    print("Selected color preset", color_set)
  
  def hex_to_rgb(self, value):
    value = value.lstrip('#')
    lv = len(value)
    # NOTE(Michael): this returns an array of the rgb colors
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

  def to_rgb(self):
    temp_dict = {}
    for key, value in self.active_color.items():
      temp_dict[key] = self.hex_to_rgb(value)
    return temp_dict