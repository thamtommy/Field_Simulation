from graphic_field_item_class import*

class AnimalGraphicsPixmapItem(FieldItemGraphicsPixmapItem):
    """this class provides a pixmap item with a preset image for the animal"""

    #constructor
    def __init__(self,graphics_list):
        super().__init__(graphics_list)

        self.animal = None

    def update_status(self):
        if self.animal._status == "Baby":
            self.setPixmap(QPixmap(self.available_graphics[0]).scaredToWidth(25,1))
        elif self.animal._status == "Poor":
            self.setPixmap(QPixmap(self.available_graphics[1]).scaredToWidth(25,1))
        elif self.animal._status == "Fine":
            self.setPixmap(QPixmap(self.available_graphics[2]).scaredToWidth(25,1))
        elif self.animal._status == "Prime":
            self.setPixmap(QPixmap(self.available_graphics[3]).scaredToWidth(25,1))

    
        
