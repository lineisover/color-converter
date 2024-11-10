import struct

from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton

from pyforms import conf
import settings
conf+=settings


class App(BaseWidget):
    def __init__(self):
        super().__init__('Color Converter')
        
        self.setGeometry(100, 100, 500, 300)
        
        self._red_channel = ControlText('Red', default='0')
        self._green_channel = ControlText('Green', default='0')
        self._blue_channel = ControlText('Blue', default='0')
        self._alpha_channel = ControlText('Alpha', default='0')
        
        self._red_channel.changed_event = self._limit_rgba
        self._green_channel.changed_event = self._limit_rgba
        self._blue_channel.changed_event = self._limit_rgba
        self._alpha_channel.changed_event = self._limit_rgba
        
        self._rgba_to_dec = ControlButton('RGBA to Decimal')
        
        self._dec = ControlText('Decimal', default='0')
        
        self._dec.changed_event = self._limit_dec
        
        self._dec_to_rgba = ControlButton('Decimal to RGBA')
        
        self._rgba_to_dec.value = self.__rgba_to_decAction
        self._dec_to_rgba.value = self.__dec_to_rgbaAction
        
        self.formset = [('_red_channel', '_green_channel', '_blue_channel', '_alpha_channel'),
                        '_rgba_to_dec',
                        '_dec',
                        '_dec_to_rgba']
    
    def _limit_rgba(self):
        for channel in [self._red_channel, self._green_channel, self._blue_channel, self._alpha_channel]:
            try:
                value = int(channel.value)
                if value < 0:
                    channel.value = str(0)
                elif value > 255:
                    channel.value = str(255)
            except ValueError:
                channel.value = str(0)
                
    def _limit_dec(self):
        try:
            value = int(self._dec.value)
            if value < -2147483648:
                self._dec.value = str(-2147483648)
            elif value > 2147483647:
                self._dec.value = str(2147483647)
        except ValueError:
            self._dec.value = str(0)

        
        
    def __rgba_to_decAction(self):
        packed_color = struct.pack('BBBB',
                                   int(self._blue_channel.value),
                                   int(self._green_channel.value),
                                   int(self._red_channel.value),
                                   int(self._alpha_channel.value))
        self._dec.value = str(struct.unpack('i', packed_color)[0])
        
    def __dec_to_rgbaAction(self):
        b, g, r, a = struct.pack('i', int(self._dec.value))
        self._red_channel.value = str(r)
        self._green_channel.value = str(g)
        self._blue_channel.value = str(b)
        self._alpha_channel.value = str(a)


        
