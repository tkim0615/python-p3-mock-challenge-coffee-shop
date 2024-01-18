#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    c1 = Customer('s')
    c2 = Customer('Henry')
    c3 = Customer('Ada')
    c4 = Customer('michael')

    cf1 = Coffee('espresso')
    cf2 = Coffee('cold brew')
    cf3 = Coffee('flat white')
    cf4 = Coffee('cappuccino')
    
    order1 = Order(c1, cf1, 3.99)
    order2 = Order(c1, cf2, 2.99)
    order3 = Order(c1, cf1, 2.50)

    order4= Order(c1, cf2, 5.29)
    order5= Order(c2, cf1, 1.95)

    order6= Order(c2, cf2, 9.00)
    order7= Order(c3, cf1, 9.8)













    ipdb.set_trace()
