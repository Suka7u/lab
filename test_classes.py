import pytest
from classes import *


class Test:
    def setup_method(self):
        self.tv = Television()

    def teardown_method(self):
        del self.tv

    def test_init(self):
        assert self.tv.__str__() == 'Tv Status: Is On = False, Channel = 0, Volume = 0'

    def test_power(self):
        """
        Testing the power method of the Television class
        """
        assert self.tv.__str__() == 'Tv Status: Is On = False, Channel = 0, Volume = 0'
        self.tv.power()
        assert self.tv.__str__() == 'Tv Status: Is On = True, Channel = 0, Volume = 0'

    def test_channel_up(self):
        """
        Testing the channel up method of the Television class
        """
        self.tv.channel_up()
        assert self.tv.__str__() == 'Tv Status: Is On = False, Channel = 0, Volume = 0'

        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__str__() == 'Tv Status: Is On = True, Channel = 1, Volume = 0'

        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()
        assert self.tv.__str__() == 'Tv Status: Is On = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        """
        Testing the channel down method of the Television class
        """
        self.tv.channel_down()
        assert self.tv.__str__() == 'Tv Status: Is On = False, Channel = 0, Volume = 0'

        self.tv.power()
        self.tv.channel_down()
        assert self.tv.__str__() == 'Tv Status: Is On = True, Channel = 3, Volume = 0'

        self.tv.channel_down()
        self.tv.channel_down()
        self.tv.channel_down()
        assert self.tv.__str__() == 'Tv Status: Is On = True, Channel = 0, Volume = 0'

    def test_volume_up(self):
        """
        Testing the volume up method of the Television class
        """
        self.tv.volume_up()
        assert self.tv.__str__() == 'Tv Status: Is On = False, Channel = 0, Volume = 0'

        self.tv.power()
        self.tv.volume_up()
        assert self.tv.__str__() == 'Tv Status: Is On = True, Channel = 0, Volume = 1'

        self.tv.volume_up()
        self.tv.volume_up()
        assert self.tv.__str__() == 'Tv Status: Is On = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        """
        Testing the volume down method of the Television class
        """
        self.tv.volume_down()
        assert self.tv.__str__() == 'Tv Status: Is On = False, Channel = 0, Volume = 0'

        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down()
        assert self.tv.__str__() == 'Tv Status: Is On = True, Channel = 0, Volume = 1'

        self.tv.volume_down()
        self.tv.volume_down()
        assert self.tv.__str__() == 'Tv Status: Is On = True, Channel = 0, Volume = 0'


if __name__ == '__main__':
    unittest.main()
