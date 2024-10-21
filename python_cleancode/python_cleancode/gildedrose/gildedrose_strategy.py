# -*- coding: utf-8 -*-

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

from abc import ABC, abstractmethod

class UpdateStrategy(ABC):

    def __init__(self, item):
        self.item = item

    @abstractmethod
    def update(self):
        pass

class RegularStrategy(UpdateStrategy):

    def update(self):
        self._decrease_quality()
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            self._decrease_quality()

    def _decrease_quality(self):
        if self.item.quality > 0:
            self.item.quality -= 1

class BrieStrategy(UpdateStrategy):

    def update(self):
        self._increase_quality()
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            self._increase_quality()

    def _increase_quality(self):
        if self.item.quality < 50:
            self.item.quality += 1

class BackstagePassStrategy(UpdateStrategy):

    def update(self):
        self._increase_quality()
        if self.item.sell_in < 11:
            self._increase_quality()
        if self.item.sell_in < 6:
            self._increase_quality()
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            self.item.quality = 0

    def _increase_quality(self):
        if self.item.quality < 50:
            self.item.quality += 1

class SulfurasStrategy(UpdateStrategy):

    def update(self):
        pass

class GildedRose:

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            strategy = self._get_strategy(item)
            strategy.update()

    def _get_strategy(self, item):
        strategy_map = {
            "Aged Brie": BrieStrategy,
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassStrategy,
            "Sulfuras, Hand of Ragnaros": SulfurasStrategy
        }
        return strategy_map.get(item.name, RegularStrategy)(item)


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

