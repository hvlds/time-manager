import urwid

def on_clean_clicked(txt, button):
    txt.set_edit_text("")

def main():
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
    loop.run()

if __name__ == "__main__":
    main()
