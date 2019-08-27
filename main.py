import urwid
from datetime import datetime
from time import sleep

def on_clean_clicked(txt, button):
    txt.set_edit_text("")

def refresh(loop, data=None):
    global start_flag
    if start_flag:
        header.set_text(str(datetime.now()))
        loop.set_alarm_in(1, refresh)

def stop(loop, data=None):
    global start_flag
    global stop_counter
    stop_counter += 1
    if stop_counter >= 2:
        start_flag = False
        header.set_text("STOP WORKING!")

def on_start_clicked(loop, button):
    global start_flag
    global stop_counter
    if start_flag:
        urwid.connect_signal(button, "click", stop)
        urwid.disconnect_signal(button, "click", on_start_clicked)
        button.set_label("stop")
        refresh(loop)
    else:
        stop(loop)

if __name__ == "__main__":
    start_flag = True
    stop_counter = 0
    txt = urwid.Edit((""))
    txt_boxed = urwid.LineBox(txt, "Task description")
    header = urwid.Text("Time Manager", align="center")
    div = urwid.Divider(" ", 0, 1)
    start = urwid.Button("start")
    clean = urwid.Button("clean")
    buttons = urwid.Columns([
        start,
        clean,
    ])
    widget = urwid.Pile([
        header,
        div,
        txt_boxed,
        buttons,
    ])
    widget = urwid.Padding(widget, align='center', width=('relative', 85))
    widget = urwid.Filler(widget, "middle")
    loop = urwid.MainLoop(widget)

    # Connect signals
    urwid.connect_signal(clean, "click", on_clean_clicked, weak_args=[txt])
    urwid.connect_signal(start, "click", on_start_clicked,
                         weak_args=[loop])
    loop.run()

