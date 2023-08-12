from nicegui import ui

from nicegui_draggable import column, draggable


class draggable_input(draggable):
    def __init__(self, title) -> None:
        self.title = title
        super().__init__()

    def __repr__(self) -> str:
        return f"draggable_input({self.title})"

    def build(self) -> None:
        ui.label(self.title)
        ui.input("Value", placeholder="Enter value")
        ui.number("Number", placeholder="Enter number")
        ui.button("Button", on_click=self.on_click)

    def on_click(self) -> None:
        print(f"Clicked {self.title}")


with ui.row():
    with column() as col_1:
        draggable_input("Simplify Layouting")
        draggable_input("Provide Deployment")
    with column() as col_2:
        draggable_input("Improve Documentation")
    with column() as col_3:
        draggable_input("Invent NiceGUI")
        draggable_input("Test in own Projects")
        draggable_input("Publish as Open Source")
        draggable_input("Release Native-Mode")

ui.run()
print(col_3.get_draggable_children())
