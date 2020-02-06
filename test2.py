from kivy.garden.mapview import MapView
from kivy.app import App
from kivy.config import Config


class MapViewApp(App):
    def build(self):
        mapview = MapView(zoom=5, lat=50.6394, lon=3.057)
        return mapview

Config.set('input', 'mouse', 'mouse,disable_multitouch')
MapViewApp().run()