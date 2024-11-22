from television import Television  # import statement needed to gain access to Television class


def main():
    # Television 1
    tv_1 = Television()
    tv_1.power()
    print(tv_1)             # Power = True, Channel = 0, Volume = 0

    tv_1.channel_up()
    tv_1.channel_up()
    tv_1.volume_up()
    print(tv_1)             # Power = True, Channel = 2, Volume = 1

    tv_1.channel_up()
    tv_1.channel_up()
    tv_1.channel_up()
    tv_1.volume_down()
    tv_1.volume_down()
    print(tv_1)             # Power = True, Channel = 1, Volume = 0

    tv_1.power()
    tv_1.volume_up()
    tv_1.channel_down()
    print(tv_1)             # Power = False, Channel = 1, Volume = 0

    tv_1.power()
    tv_1.volume_up()
    tv_1.volume_up()
    tv_1.volume_up()
    tv_1.channel_down()
    tv_1.channel_down()
    print(tv_1)             # Power = True, Channel = 3, Volume = 2

    # Television 2
    tv_2 = Television()
    tv_2.power()
    tv_2.channel_up()
    tv_2.volume_up()
    print(tv_2)             # Power = True, Channel = 1, Volume = 1

    # Muting effect
    tv_1.mute()
    print(tv_1)             # Power = True, Channel = 3, Volume = 0
    tv_1.volume_down()
    print(tv_1)             # Power = True, Channel = 3, Volume = 1
    tv_1.mute()
    print(tv_1)             # Power = True, Channel = 3, Volume = 0
    tv_1.volume_up()
    print(tv_1)             # Power = True, Channel = 3, Volume = 2
    tv_1.power()
    tv_1.mute()
    print(tv_1)             # Power = False, Channel = 3, Volume = 2


if __name__ == '__main__':
    main()
