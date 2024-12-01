from tkinter import *
from television import Television


class Gui:
    """
    A class for setting up and giving functionality to the GUI for television_main.py
    """
    def __init__(self, window) -> None:
        """
        Method for piecing together the GUI layout.
        Consists of a display showing the current status of the television,
        buttons for power and mute, a label for channel and volume and associated
        increase and decrease buttons respectively.
        """
        self.tvl = Television()

        self.window = window

        self.frame_one = Frame(self.window)
        self.screen_label = Label(self.frame_one, text="Power: Off\n"
                                                       "Mute: Off\n"
                                                       "Current channel: 0\n"
                                                       "Current volume: 0")
        self.screen_label.pack()
        self.frame_one.pack()

        self.frame_two = Frame(self.window)
        self.button_power = Button(self.frame_two, text='Pwr', command=self.power)
        self.button_mute = Button(self.frame_two, text='Mute', command=self.mute)
        self.button_power.pack(side='right')
        self.button_mute.pack(side='left')
        self.frame_two.pack()

        self.frame_three = Frame(self.window)
        self.channel_label = Label(self.frame_three, text='Channel')
        self.channel_up = Button(self.frame_three, text='->', command = self.channel_up)
        self.channel_down = Button(self.frame_three, text='<-', command=self.channel_down)
        self.channel_label.pack()
        self.channel_up.pack(side='right')
        self.channel_down.pack(side='left')
        self.frame_three.pack()

        self.frame_four = Frame(self.window)
        self.volume_label = Label(self.frame_four, text='Volume')
        self.volume_up = Button(self.frame_four, text='->', command=self.volume_up)
        self.volume_down = Button(self.frame_four, text='<-', command=self.volume_down)
        self.volume_label.pack()
        self.volume_up.pack(side='right')
        self.volume_down.pack(side='left')
        self.frame_four.pack()
    def submit(self) -> None:
        """
        Method for changing the screen_label after any status change.
        """
        power_status = ""
        mute_status = ""
        if self.tvl.get_power():
            power_status = "On"
        else:
            power_status = "Off"
        if self.tvl.get_mute():
            mute_status = "On"
        else:
            mute_status = "Off"
        self.screen_label.config(text=f"Power: {power_status}\n"
                                      f"Mute: {mute_status}\n"
                                      f"Current channel: {self.tvl.get_channel()}\n"
                                      f"Current volume: {self.tvl.get_volume()}")
    def power(self) -> None:
        """
        Method for the functionality of button_power.
        Updates the screen_label.
        """
        self.tvl.power()
        self.submit()
    def mute(self) -> None:
        """
        Method for the functionality of button_mute.
        Updates the screen_label.
        """
        self.tvl.mute()
        self.submit()
    def channel_up(self) -> None:
        """
        Method for the functionality of channel_up.
        Updates the screen_label.
        """
        self.tvl.channel_up()
        self.submit()
    def channel_down(self) -> None:
        """
        Method for the functionality of channel_down.
        Updates the screen_label.
        """
        self.tvl.channel_down()
        self.submit()
    def volume_up(self) -> None:
        """
        Method for the functionality of volume_up.
        Updates the screen_label.
        """
        self.tvl.volume_up()
        self.submit()
    def volume_down(self) -> None:
        """
        Method for the functionality of volume_down.
        Updates the screen_label.
        """
        self.tvl.volume_down()
        self.submit()