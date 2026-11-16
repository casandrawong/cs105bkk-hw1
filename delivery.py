"""HW1: a Bangkok food-delivery order. Practises Sessions 1-3: aliasing and defaults, comprehensions,
classes with a guarded property, __repr__ and __eq__, inheritance with super(), composition and duck typing."""


class MenuItem:
    """A dish on a restaurant's menu. The price is a whole number of baht."""

    def __init__(self, name: str, price: int):
        """Store the name and the price. The price goes through the setter, so it is checked."""
        self.name = name
        self.price = price
    @property
    def price(self) -> int:
        """Provided: the price in baht."""
        return self._price

    @price.setter
    def price(self, value: int) -> None:
        """Set the price. Raise ValueError if it is 0 or less, and keep the old price."""
        if value <= 0:
            raise ValueError(f"Price must be more than 0 baht, got {value}")
        self._price = value

    def __repr__(self) -> str:
        """Return the developer view, for example MenuItem('Pad Thai', 60)."""
        return f"{type(self).__name__}('{self.name}', {self.price})"
    

    def __eq__(self, other: object) -> bool:
        """Two menu items are equal when their names and prices are equal."""
        if not isinstance(other, MenuItem):
            return NotImplemented
        if self.name == other.name and self.price == other.price:
            return True
        else:
            return False

    def cost(self, quantity: int) -> int:
        """Provided: what quantity of this dish costs, in baht."""
        return self.price * quantity


class PromoItem(MenuItem):
    """A dish on a "buy 2, get 1 free" promotion: every third one is free."""

    def cost(self, quantity: int) -> int:
        """Return what quantity costs when every third one is free."""
        free_items = quantity // 3
        paid_items = quantity - free_items
        return super().cost(paid_items)


class Order:
    """One customer's delivery order: a list of (menu item, quantity) lines."""

    delivery_fee = 30  # Provided: baht added to every order with food in it
    free_delivery_from = 300  # Provided: food worth this much or more is delivered free

    def __init__(self, customer, lines=None):
        """Store the customer and a new list of lines. Never share a list with the caller or another order."""
        self.customer = customer
        if lines is None:
            self.lines = []
        else:
            self.lines = lines.copy()

    def add(self, item: MenuItem, quantity: int = 1) -> None:
        """Add one line. Raise ValueError if quantity is less than 1."""
        if quantity < 1:
            raise ValueError(f"Quantity must be at least 1, got {quantity}")
        self.lines.append((item, quantity))

    def total(self) -> int:
        """Return the food cost plus the delivery fee; free delivery from free_delivery_from; 0 if empty."""
        food_cost = 0
        for item, quantity in self.lines:
            food_cost += item.cost(quantity)

        if len(self.lines) == 0:
            return 0
        if food_cost >= self.free_delivery_from:
            return food_cost
        else:
            return food_cost + self.delivery_fee

    def summary(self) -> list[str]:
        """Return one text line per order line, for example "2 x Pad Thai"."""
        return [f"{quantity} x {item.name}" for item, quantity in self.lines]
def cheapest(options):
    """Return the option with the smallest total(). First one wins a tie; None for an empty list.

    An option can be anything with a total() method, not only an Order.
    """
    if len(options) == 0:
        return None
    cheapest_option = options[0]
    for option in options:
        if option.total() < cheapest_option.total():
            cheapest_option = option
    return cheapest_option
    
