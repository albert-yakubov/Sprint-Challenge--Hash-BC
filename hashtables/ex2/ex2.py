#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    #route = [None] * length
    
    # reset the route
    route = []

    """
    YOUR CODE HERE
    """
    
    # get the ticket 
    for i in tickets:
        hash_table_insert(hashtable, i.source, i.destination)
    
    # grab the destination that was just inserted
    destination = hash_table_retrieve(hashtable, 'None')
    # then append the destination to the route
    while destination != None:
        route.append(destination)
        destination = hash_table_retrieve(hashtable, destination)
        
        return route 
        
    
