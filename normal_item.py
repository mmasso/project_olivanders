class Normal_item():

    def __init__(self, name, sell_in=1, quality=1):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self.quality_speed = -1
        self.sell_in_speed = -1

    def __repr__(self):
        return "name:%s, sell_in:%s, quality:%s" % (self.name, self.sell_in, self.quality)

    # def checksellinspeed i quality speed()

    def update_quality(self):
        self.quality -= 1

    def update_sell_in(self):
        self.sell_in -= 1

    # funciones para casos test

    def get_quality(self):
        return self.quality

    def get_sell_in(self):
        return self.sell_in

    # def general para cambiar todo el item

    def update_item(self):
        pass
