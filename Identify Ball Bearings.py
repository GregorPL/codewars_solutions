class Bearing:
    def __init__(self, id): self.id = id
    def __repr__(self): return f"Bearing from Box {self.id}"


a, b, c, d, e = (Bearing(i) for i in range(5))


def build_weigh(deluxe):
    used = False

    def weigh(*bearings):
        nonlocal used
        if used:
            raise Exception("weigh has already been used!")
        if any(not isinstance(v, Bearing) for v in bearings):
            raise Exception("All arguments should be Bearings!")
        used = True
        return sum(10 + (bearing is deluxe) for bearing in bearings)
    return weigh


def identify_bb(bearings, weigh):
    a, b, c = bearings

    if weigh(a, b) == 20:
        return c
    if weigh(a) == 10:
        return b
    return a


print(identify_bb([a, b, c], d))
