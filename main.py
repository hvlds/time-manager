import urwid
from datetime import datetime

def on_clean_clicked(txt, button):
    txt.set_edit_text("")

def refresh(loop, data=None):
    header.set_text(str(datetime.now()))
    loop.set_alarm_in(1, refresh)

def on_start_clicked(header, loop, button):
    refresh(loop)

if __name__ == "__main__":
    txt = urwid.Edit((""))
    txt_boxed = urwid.LineBox(txt, "Task description")
    header = urwid.Text("Time Manager", align="center")
    start = urwid.Button("start")
    clean = urwid.Button("clean")
    buttons = urwid.Columns([
        start,
        clean,
    ])
    widget = urwid.Pile([
        header,
        txt_boxed,
        buttons,
    ])
    widget = urwid.Padding(widget, align='center', width=('relative', 85))
    widget = urwid.Filler(widget, "middle")

    urwid.connect_signal(clean, "click", on_clean_clicked, weak_args=[txt])
    loop = urwid.MainLoop(widget)
    # loop.set_alarm_in(1, refresh)
    urwid.connect_signal(start, "click", on_start_clicked, weak_args=[header,loop])
    loop.run()
