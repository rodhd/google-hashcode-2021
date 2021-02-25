class Car:
    def __init__(self, street, position, path):
        self.street = street
        self.position = position
        self.path = path

    def tick(self, streets):
        pass


class Street:
    def __init__(self, start, end, name, length):
        self.start = start
        self.end = end
        self.name = name
        self.length = length

    def tick(self):
        pass


class Intersection:
    def __init__(self, int_id, inbound, outbound):
        self.int_id = int_id
        self.inbound = inbound
        self.outbound = outbound

    def tick(self):
        pass
