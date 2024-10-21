class Item:
    """
    Represents an item with a name, sell-in value, and quality.
    
    Attributes:
        name (str): The name of the item.
        sell_in (int): The number of days to sell the item.
        quality (int): The quality of the item.
    """
    def __init__(self, name, sell_in, quality):
        """
        Initializes the Item with a name, sell-in value, and quality.

        Args:
            name (str): The name of the item.
            sell_in (int): The number of days left to sell.
            quality (int): The quality of the item.
        """
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        """
        Returns a string representation of the Item.

        Returns:
            str: A formatted string with name, sell_in, and quality.
        """
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


from abc import ABC, abstractmethod

class UpdateStrategy(ABC):
    """
    Abstract base class that defines the interface for item update strategies.
    
    Attributes:
        item (Item): The item to apply the update strategy on.
    """
    def __init__(self, item):
        """
        Initializes the UpdateStrategy with an item.

        Args:
            item (Item): The item to be updated.
        """
        self.item = item

    @abstractmethod
    def update(self):
        """
        Abstract method to be implemented by subclasses for updating the item.
        """
        pass


class RegularStrategy(UpdateStrategy):
    """
    Strategy for updating regular items (non-special items).
    """
    def update(self):
        """
        Updates the quality and sell-in for regular items.
        Decreases quality by 1 each day, and twice as fast after the sell-in period.
        """
        self._decrease_quality()
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            self._decrease_quality()

    def _decrease_quality(self):
        """
        Decreases the quality of the item if it's greater than 0.
        """
        if self.item.quality > 0:
            self.item.quality -= 1


class BrieStrategy(UpdateStrategy):
    """
    Strategy for updating "Aged Brie" items.
    """
    def update(self):
        """
        Updates the quality and sell-in for Aged Brie.
        Increases quality each day, and faster after the sell-in period.
        """
        self._increase_quality()
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            self._increase_quality()

    def _increase_quality(self):
        """
        Increases the quality of the item if it's less than 50.
        """
        if self.item.quality < 50:
            self.item.quality += 1


class BackstagePassStrategy(UpdateStrategy):
    """
    Strategy for updating "Backstage passes" items.
    """
    def update(self):
        """
        Updates the quality and sell-in for Backstage passes.
        Increases quality as sell-in approaches, but drops to 0 after the event.
        """
        self._increase_quality()
        if self.item.sell_in < 11:
            self._increase_quality()
        if self.item.sell_in < 6:
            self._increase_quality()
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            self.item.quality = 0

    def _increase_quality(self):
        """
        Increases the quality of the item if it's less than 50.
        """
        if self.item.quality < 50:
            self.item.quality += 1


class SulfurasStrategy(UpdateStrategy):
    """
    Strategy for updating "Sulfuras" items, which never change.
    """
    def update(self):
        """
        No updates are made for Sulfuras items as they do not degrade or improve.
        """
        pass


class GildedRose:
    """
    The main class for managing and updating a collection of items in the Gilded Rose.
    
    Attributes:
        items (list): A list of Item objects.
    """
    def __init__(self, items):
        """
        Initializes GildedRose with a list of items.

        Args:
            items (list): A list of Item objects.
        """
        self.items = items

    def update_quality(self):
        """
        Updates the quality and sell-in values of all items in the store.
        Uses appropriate strategy based on the item type.
        """
        for item in self.items:
            strategy = self._get_strategy(item)
            strategy.update()

    def _get_strategy(self, item):
        """
        Determines the appropriate strategy for a given item.

        Args:
            item (Item): The item for which the strategy is determined.

        Returns:
            UpdateStrategy: The appropriate strategy for the item.
        """
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

