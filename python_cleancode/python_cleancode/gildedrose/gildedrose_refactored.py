# -*- coding: utf-8 -*-

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class GildedRose:

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self._update_item_quality(item)

    def _update_item_quality(self, item):
        if item.name == "Sulfuras, Hand of Ragnaros":
            return

        if item.name == "Aged Brie":
            self._update_aged_brie(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            self._update_backstage_pass(item)
        else:
            self._update_regular_item(item)

        item.sell_in -= 1

        if item.sell_in < 0:
            self._update_expired_item(item)

    def _update_aged_brie(self, item):
        self._increase_quality(item)

    def _update_backstage_pass(self, item):
        self._increase_quality(item)
        if item.sell_in < 11:
            self._increase_quality(item)
        if item.sell_in < 6:
            self._increase_quality(item)
        if item.sell_in <= 0:
            item.quality = 0

    def _update_regular_item(self, item):
        self._decrease_quality(item)

    def _update_expired_item(self, item):
        if item.name == "Aged Brie":
            self._increase_quality(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            item.quality = 0
        else:
            self._decrease_quality(item)

    def _increase_quality(self, item):
        if item.quality < 50:
            item.quality += 1

    def _decrease_quality(self, item):
        if item.quality > 0:
            item.quality -= 1


if __name__ == '__main__':
    print ("OMGHAI!")
    items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
    ]

    days = 31
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items).update_quality()

