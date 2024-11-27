import pytest
from television import *

class Test:
    def setup_method(self):
        self.tv = Television()

    def teardown_method(self):
        del self.tv

    def test_init(self):
        assert self.tv._Television__status == False
        assert self.tv._Television__muted == False
        assert self.tv._Television__volume == Television.MIN_VOLUME
        assert self.tv._Television__channel == Television.MIN_CHANNEL
        print(self.tv)

    def test_power(self):
        self.tv.power()
        assert self.tv._Television__status == True
        print(self.tv)
        self.tv.power()
        assert self.tv._Television__status == False
        print(self.tv)

    def test_mute(self):
        #on,vol increased once, muted
        self.tv.power()
        assert self.tv._Television__muted == False
        self.tv.volume_up()
        self.tv.mute()
        assert self.tv._Television__muted == True
        print(self.tv)

        #on and unmuted
        self.tv.mute()
        assert self.tv._Television__muted == False
        print(self.tv)

        #off and muted
        self.tv.power()
        self.tv.mute()
        assert self.tv._Television__muted == False
        print(self.tv)

        #off and unmuted
        self.tv.mute()
        assert self.tv._Television__muted == False
        print(self.tv)

    def test_channel_up(self):
        #off and increased
        self.tv.channel_up()
        assert self.tv._Television__channel == Television.MIN_CHANNEL
        print(self.tv)

        #on and increased
        self.tv.power()
        self.tv.channel_up()
        assert self.tv._Television__channel == 1
        print(self.tv)

        #on and increased past max
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()
        assert self.tv._Television__channel == Television.MIN_CHANNEL
        print(self.tv)

    def test_channel_down(self):
        #off and down
        self.tv.channel_down()
        assert self.tv._Television__channel == Television.MIN_CHANNEL
        print(self.tv)

        #on and past min
        self.tv.power()
        self.tv.channel_down()
        assert self.tv._Television__channel == Television.MAX_CHANNEL
        print(self.tv)

    def test_volume_up(self):
        #off and increased
        self.tv.volume_up()
        assert self.tv._Television__volume == Television.MIN_VOLUME
        print(self.tv)

        #on and increased once
        self.tv.power()
        self.tv.volume_up()
        assert self.tv._Television__volume == 1
        print(self.tv)

        #on and muted and then increased
        self.tv.mute()
        assert self.tv._Television__muted == True
        self.tv.volume_up()
        assert self.tv._Television__muted == False
        assert self.tv._Television__volume == 2
        print(self.tv)

        #on and increased past max
        self.tv.volume_up()
        assert self.tv._Television__volume == Television.MAX_VOLUME
        print(self.tv)

    def test_volume_down(self):
        #off and vol decreased
        self.tv.volume_down()
        assert self.tv._Television__volume == Television.MIN_VOLUME
        print(self.tv)

        #on and decreased(set on the max vol)
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        assert self.tv._Television__volume == Television.MAX_VOLUME
        print(self.tv)
        self.tv.volume_down()
        assert self.tv._Television__volume == 1
        print(self.tv)

        #on,muted,decreased(put at max val to see effects)
        self.tv.volume_up()
        self.tv.volume_up()
        print(self.tv)
        self.tv.mute()
        print(self.tv)
        self.tv.volume_down()
        assert self.tv._Television__volume == 1
        print(self.tv)

        #on and decreased past min vol
        self.tv.volume_down()
        self.tv.volume_down()
        assert self.tv._Television__volume == Television.MIN_VOLUME
        print(self.tv)