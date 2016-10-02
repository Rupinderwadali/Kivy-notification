from os.path import dirname
from os.path import join
from os.path import realpath

import datetime
import time
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
#from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
#from kivy.graphics import Color, Triangle, Ellipse
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from plyer import notification
from plyer.utils import platform
from plyer.compat import PY2
from time import strftime
from kivy.clock import Clock as KivyClock

class AlarmBox(Widget):
     def do_notify(self, text, text1):
                compare = 1
                while (compare):
                    now = datetime.datetime.now().replace(second= 00, microsecond= 000000)
                    user = now.replace(hour=int(text), minute=int(text1), second=00, microsecond=000000)
                    if now == user:        
                         title = self.ids.notification_title.text
                         message = self.ids.notification_text.text
                         if PY2:
                             title = title.decode('utf8')
                             message = message.decode('utf8')
                         kwargs = {'title': title, 'message': message}
                         kwargs['app_name'] = "Plyer Notification Example"
                         if platform == "win":
                             kwargs['app_icon'] = join(dirname(realpath(__file__)),
                                          'plyer-icon.ico')
                             kwargs['timeout'] = 4
                         else:
                             kwargs['app_icon'] = join(dirname(realpath(__file__)),
                                          'plyer-icon.png')
                         notification.notify(**kwargs)
                compare = 0    
class Circles(Widget):
    pass

class SetAlarmApp(App):
    def build(self):
        top = AlarmBox()
 
        return top
 
if __name__ == '__main__':
    SetAlarmApp().run()
