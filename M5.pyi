def begin():
    ...


def update():
    ...


class Widgets:

    @staticmethod
    def fillScreen(color: int):
        ...

    class FONTS:
        DejaVu18 = None

    class Label():

        def __init__(self, text: str, x: int, y: int, scale: float, color: int, bg_color: int, font):
            ...

        def setText(self, text: str):
            ...
