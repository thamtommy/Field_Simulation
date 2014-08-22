from PyQt4.QtGui import *

import field_resources

class QDragLabel(QLabel):
    """this c,ass provides an image label that can be dragged and dropped"""

    #constructor

    def __init__(self,picture):
        super().__init__()
        self.setPixmap(picture.scaledToWidth(35,1))

class WheatDragLabel(QDragLabel):
    """this class provides a wheat label that can be dragged and dropped"""
    def __init__(self):
        super().__init__(QPixmap(":/wheat_seed.png"))

class PotatoDragLabel(QDragLabel):
    """this class provides a potato label that can be dragged and dropped"""
    def __init__(self):
        super().__init__(QPixmap(":/potato_seed.png"))

class CowDragLabel(QDragLabel):
    """this class provides a cow label that can be dragged and dropped"""
    def __init__(self):
        super().__init__(QPixmap(":/cow_baby.png"))

class SheepDragLabel(QDragLabel):
    """this class provides a sheep label that can be dragged and dropped"""
    def __init__(self):
        super().__init__(QPixmap(":/sheep_baby.png"))
