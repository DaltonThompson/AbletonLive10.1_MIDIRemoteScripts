# uncompyle6 version 3.4.1
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  2 2019, 14:32:10) 
# [GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)]
# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Axiom_AIR_25_49_61/SpecialMixerComponent.py
# Compiled at: 2019-04-09 19:23:44
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.MixerComponent import MixerComponent
from .DisplayingChanStripComponent import DisplayingChanStripComponent

class SpecialMixerComponent(MixerComponent):
    u""" Special mixer class that uses displaying channel strips """

    def __init__(self, name_display, value_display, num_tracks, num_returns=0):
        MixerComponent.__init__(self, num_tracks, num_returns=0)
        self._name_display = name_display
        self._value_display = value_display
        for index in range(num_tracks):
            self._channel_strips[index].set_name_display(self._name_display)
            self._channel_strips[index].set_value_display(self._value_display)

        for index in range(num_returns):
            self._return_strips[index].set_name_display(self._name_display)
            self._return_strips[index].set_value_display(self._value_display)

        self._selected_strip.set_name_display(self._name_display)
        self._selected_strip.set_value_display(self._value_display)

    def disconnect(self):
        MixerComponent.disconnect(self)
        self._name_display = None
        self._value_display = None
        return

    def tracks_to_use(self):
        return self.song().visible_tracks + self.song().return_tracks

    def _create_strip(self):
        return DisplayingChanStripComponent()