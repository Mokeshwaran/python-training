from collections import ChainMap


class Gadget:
    """
    This class will contain a dictionary of Gadgets for
    further operations. Like an inventory.
    """
    gadgets = {}
    p_id = 0

    def __init__(self, title='title', specs='specs', color='color'):
        self.title = title
        self.specs = specs
        self.color = color

    def get(self):
        """
        This get method is used to retrieve the ChainMap object of the
        Gadget class.

        :return: ChainMap object of Gadgets.
        """
        self.p_id += 1
        self.gadgets[self.p_id] = [self.title, self.specs, self.color]
        return self.gadgets


class Games:
    """
    This class will contain a dictionary of Games for
    further operations. Also like an inventory.
    """
    games = {}
    p_id = 0

    def __init__(self, title='title', edition='edn', version='vrn'):
        self.title = title
        self.edition = edition
        self.version = version

    def get(self):
        """
        This get method will be used to retrieve the chain map object of the
        Games class.
        :return: ChainMap object of Games.
        """
        self.p_id += 1
        self.games[self.p_id] = [self.title, self.edition, self.version]
        return self.games


class Cart(Gadget, Games):
    """
    This class will contain a combined dictionary of Gadgets and Games by using
    ChainMap collection. Cart class is like the mixture of many classes.
    """
    def __init__(self, gadget, games):
        super().__init__()
        self.gadget = gadget
        self.games = games

    def get(self):
        """
        This get method will be used to retrieve the combined chain map object of the
        Cart class.
        :return: ChainMap object of Games.
        """
        games = Games()
        gadgets = Gadget()
        cart_items = ChainMap(gadgets.gadgets, games.games)
        return cart_items


gadgets = Gadget("Gadget Title", "Specs", "Blue")
games = Games("Game Title", "Some Edition", "Some Version")
cart = Cart(gadgets, games)
print(games.get())
print(gadgets.get())
print(cart.get())

essentials = {2: 'Water bottle', 3: 'Biscuits'}
cart_two = cart.get().new_child(essentials)  # new_child() will add new dict to the beginning of the ChainMap.
print(cart_two)