class Television:
    """
    A class to set up a television and it's details like volume, power status, and channel
    """
    MIN_VOLUME :int = 0  #Default Minimum volume set at 0
    MAX_VOLUME :int = 2  #Default Maximim Volume set at 2
    MIN_CHANNEL :int = 0 #Default Minimum channel set at 0
    MAX_CHANNEL :int = 3 #Default Maximum channel set at 3

    def __init__(self) -> None:
        """
        Function to set up default instance Variables
        :return: Nothing
        """
        self.__status :bool = False
        self.__muted :bool = False
        self.__volume :int = Television.MIN_VOLUME
        self.__channel :int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Funtion to turn tv on and off by switching the status variable
        :return: Nothing
        """
        if self.__status == False:
            self.__status :bool = True
        elif self.__status == True:
            self.__status :bool = False

    def mute(self) -> None:
        """
        Function sees if the tv is on and if it is, it'll mute/unmutes the tv
        :return: Nothing
        """
        if self.__status == True:
            if self.__muted == False:
                self.__muted = True
            else:
                self.__muted = False

    def channel_up(self) -> None:
        """
        Function sees if tv is on and if it is it'll change the channel up one
        :return: Nothing
        """
        if self.__status == True:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Function sees if tv is on and if it is it'll change the channel down one
        :return: Nothing
        """
        if self.__status == True:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Function sees if tv is on and if it is it'll change the volume up one
        :return: Nothing
        """
        if self.__status == True:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            else:
                self.__volume = Television.MAX_VOLUME
    def volume_down(self) -> None:
        """
        Function sees if tv is on and if it is it'll change the volume down one
        :return: Nothing
        """
        if self.__status == True:
            self.__muted = False
            if self.__volume == Television.MIN_VOLUME:
                pass
            else:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Function gives the format of strings when they are called to be printed
        :return: TV status and values of volume and channels
        """
        if self.__muted == False:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}"