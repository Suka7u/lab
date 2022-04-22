class Television:
    """
    A class representing a television
    """
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Function to initialize the TV channel, volume, and status
        """
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__status = False

    def power(self) -> None:
        """
        Function to turn the TV on and off
        """
        if self.__status == False:
            self.__status = True
        elif self.__status:
            self.__status = False
        else:
            pass

    def channel_up(self) -> None:
        """
        Function to turn the channel up
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1
        else:
            pass

    def channel_down(self) -> None:
        """
        Function to turn the channel down
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1
        else:
            pass

    def volume_up(self) -> None:
        """
        Function to turn the volume up
        """
        if self.__status and self.__volume < Television.MAX_VOLUME:
            self.__volume += 1
        else:
            pass

    def volume_down(self) -> None:
        """
        Function to turn the volume down
        """
        if self.__status and self.__volume > Television.MIN_VOLUME:
            self.__volume -= 1
        else:
            pass

    def __str__(self) -> str:
        """
        :return: TV status, Channel, Volume
        """
        return f'Tv Status: Is On = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
