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
        increase and decrease buttons respectively. Finally, a volume bar and submit button for the volume.
        """
        self.tvl = Television()

        self.window = window

        """
        FIXME: The use of the PhotoImage function from Tkinter allows the use
        of images in Tkinter GUIs through labels using 'image=', however a bug 
        occurs in which images show as blank, has happened after updating python.
        As such the code has been omitted.
        This may be fixed before submission but if not, this is here for explanation of
        how it would be done. Note, works best with png files, subset and zoom args used
        for resizing the image.
        """

        self.frame_one = Frame(self.window)
        self.screen_label = Label(self.frame_one, text="Power: Off\n"
                                                       "Mute: Off\n"
                                                       "Current channel: N/A\n"
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
        self.channel_up_button = Button(self.frame_three, text='->', command = self.channel_up)
        self.channel_down_button = Button(self.frame_three, text='<-', command=self.channel_down)
        self.channel_up_x2_button = Button(self.frame_three, text='->>', command=self.channel_up_x2)
        self.channel_down_x2_button = Button(self.frame_three, text='<<-', command=self.channel_down_x2)
        self.channel_label.pack()
        self.channel_up_button.pack(side='right')
        self.channel_down_button.pack(side='left')
        self.channel_up_x2_button.pack(side='right')
        self.channel_down_x2_button.pack(side='left')
        self.frame_three.pack()

        self.frame_four = Frame(self.window)
        self.volume_label = Label(self.frame_four, text='Volume')
        self.volume_up = Button(self.frame_four, text='->', command=self.volume_up)
        self.volume_down = Button(self.frame_four, text='<-', command=self.volume_down)
        self.volume_label.pack()
        self.volume_up.pack(side='right')
        self.volume_down.pack(side='left')
        self.frame_four.pack()

        self.frame_five = Frame(self.window)
        self.bar_label = Label(self.frame_five, text="Volume bar")
        self.bar_label.pack()
        self.frame_five.pack()

        self.frame_six = Frame(self.window)
        self.volume_scale = Scale(self.frame_six, from_=0, to=0, orient=HORIZONTAL)
        self.volume_scale.pack()
        self.frame_six.pack()

        self.frame_seven = Frame(self.window)
        self.scale_confirm = Button(self.frame_seven, text="Set volume to current scale?", command=self.volume_set)
        self.scale_confirm.pack()
        self.frame_seven.pack()

    def submit(self) -> None:
        """
        Method for changing the screen_label after any status change.
        """
        power_status = ""
        mute_status = "Off"
        current_channel = ""
        if self.tvl.get_power():
            power_status = "On"
            if self.tvl.get_mute():
                self.volume_scale.config(from_=0, to=0)
                mute_status = "On"
            else:
                self.volume_scale.config(from_=0, to=2)
                mute_status = "Off"
        else:
            power_status = "Off"
            self.volume_scale.config(from_=0, to=0)

        if not self.tvl.get_power():
            current_channel = "N/A"
        elif self.tvl.get_channel() == 0:
            current_channel = "Cartoons"
        elif self.tvl.get_channel() == 1:
            current_channel = "News"
        elif self.tvl.get_channel() == 2:
            current_channel = "Nature documentary"
        else:
            current_channel = "Popular movies"

        self.screen_label.config(text=f"Power: {power_status}\n"
                                      f"Mute: {mute_status}\n"
                                      f"Current channel: {current_channel}\n"
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
    def channel_up_x2(self) -> None:
        """
        Method for increasing the channel 2x.
        Updates the screen_label.
        """
        self.tvl.channel_up()
        self.tvl.channel_up()
        self.submit()
    def channel_down(self) -> None:
        """
        Method for the functionality of channel_down.
        Updates the screen_label.
        """
        self.tvl.channel_down()
        self.submit()
    def channel_down_x2(self) -> None:
        """
        Method for increasing the channel 2x.
        Updates the screen_label.
        """
        self.tvl.channel_down()
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
    def volume_set(self) -> None:
        """
        Method for volume slider functionality.
        Updates the screen_label.
        """
        self.tvl.set_volume(self.volume_scale.get())
        self.submit()