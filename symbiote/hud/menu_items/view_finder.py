from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.graphics.texture import Texture

from common.transformations.camera import get_view_frame_from_road_frame as camera

import cv2

class ViewFinder(Image):
  def __init__(self, **kwargs):
    super(ViewFinder, self).__init__(**kwargs)

    # NOTE(Michael): Example of picture data, not needed as we are grabbing this form our helper class
    # img = cv2.imread('0.png', cv2.IMREAD_UNCHANGED)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # img = cv2.flip(img, 0)

    img = camera(0, 0, 0, 1.22)

    
    self.w, self.h = img.shape
    buf1 = cv2.flip(img, 0)
    buf = buf1.tostring()
    image_texture = Texture.create(size=(self.w, self.h), colorfmt='bgr')
    image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
    self.w_img = Image(size=(self.w, self.h), texture=image_texture)
    self.texture = image_texture

    # ret, frame = cv2.VideoCapture(2).read()
    # if ret:
    #   # convert it to texture
    #   buf1 = cv2.flip(frame, 0)
    #   buf = buf1.tostring()
    #   image_texture = Texture.create(
    #       size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
    #   image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
    #   # display image from the texture
    #   self.texture = image_texture
  
  def update(self):
    img = camera(0, 0, 0, 1.22)
    self.texture.blit_buffer(img.flatten(), colorfmt='rgb', bufferfmt='ubyte')
    self.w_img = Image(size=(self.w, self.h), texture=self.texture)