import urwid
from datetime import datetime

class Display:
    def __init__(self):
        self.start_flag = True
        self.stop_counter = 0
        self.txt = urwid.Edit((""))
        self.txt_boxed = urwid.LineBox(self.txt, "Task description")
        self.header = urwid.Text("Time Manager", align="center")
        self.div = urwid.Divider(" ", 0, 1)
        self.start = urwid.Button("start")
        self.clean = urwid.Button("clean")
        self.buttons = urwid.Columns([
            self.start,
            self.clean,
        ])
        self.widget = urwid.Pile([
            self.header,
            self.div,
            self.txt_boxed,
            self.buttons,
        ])
        self.widget = urwid.Padding(self.widget, align='center', width=('relative', 85))
        self.widget = urwid.Filler(self.widget, "middle")

        # Connect signals
        urwid.connect_signal(self.clean, "click", self.on_clean_clicked)
        urwid.connect_signal(self.start, "click", self.on_start_clicked)

    def main(self):
        self.loop = urwid.MainLoop(self.widget)
        self.loop.run()

    def on_clean_clicked(self, button):
        self.txt.set_edit_text("")

    def refresh(self, loop=None, data=None):
        if self.start_flag:
            self.header.set_text(str(datetime.now()))
            self.loop.set_alarm_in(1, self.refresh)

    def stop(self, loop=None, data=None):
        self.stop_counter += 1
        if self.stop_counter >= 1:
            self.start_flag = False
            self.header.set_text("STOP WORKING!")

    def on_start_clicked(self, button, loop=None):
        if self.start_flag:
            urwid.connect_signal(button, "click", self.stop)
            urwid.disconnect_signal(button, "click", self.on_start_clicked)
            button.set_label("stop")
            self.refresh(self.loop)
        else:
            self.stop(self.loop)
