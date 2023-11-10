from nicegui import ui

from nicegui_draggable import column, draggable


class DraggableElement(draggable):
    def __init__(self, title, drag_enabled=True) -> None:
        self.title = title
        super().__init__(drag_enabled=drag_enabled)
        self.classes("bg-white shadow-md rounded-md p-4 m-2")

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
        DraggableElement("Simplify Layouting")
        DraggableElement("Provide Deployment")
    with column() as col_2:
        DraggableElement("Improve Documentation")
    with column() as col_3:
        DraggableElement("Invent NiceGUI", drag_enabled=False)
        DraggableElement("Test in own Projects", drag_enabled=False)
        DraggableElement("Publish as Open Source", drag_enabled=False)


if __name__ in {"__main__", "__mp_main__"}:
    ui.run()
