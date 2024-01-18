class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3 and not hasattr(self, 'name'):
            self._name = name
        # else:
        #     raise Exception('invalid name/ must be 3 characters or longer. Can\'t change name')
    
        
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
        
    def customers(self):
        return list(set([order.customer for order in self.orders()]))
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        price_list = [order.price for order in self.orders()]
        return round((sum(price_list) / len(price_list)), 2)
    

class Customer:
    all = []
    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1<= len(name) <=15:
            self._name = name
    
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    def most_aficionado(cls, coffee):
        all_coffee_orders = [order for order in Order.all if order.coffee is coffee]
        print(all_coffee_orders)
        if all_coffee_orders:
            return max(cls.all, key= lambda customer: sum([order.price for order in all_coffee_orders if order.customer is customer]))

    
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
        
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        if isinstance(price, float) and 1.0 <= price <= 10.0 and not hasattr(self, 'price'):
            self._price = price
        # else:
        #     raise Exception('price must be between 1 and 10. Can\'t change price')

    @property
    def customer(self):
        return self._customer
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
    @property
    def coffee(self):
        return self._coffee
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee