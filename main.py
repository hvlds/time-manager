import urwid

def main():
    txt = urwid.Edit((""))
    txt = urwid.LineBox(txt, "Task description")
    header = urwid.Text("Time Manager", align="center")
    buttons = urwid.Columns([
        urwid.Button("save"),
        urwid.Button("clean"),
    ])
    widget = urwid.Pile([
        header,
        txt,
        buttons,
    ])
    widget = urwid.Padding(widget, align='center', width=('relative', 85))
    widget = urwid.Filler(widget, "middle")
    loop = urwid.MainLoop(widget)
    loop.run()

if __name__ == "__main__":
    main()
