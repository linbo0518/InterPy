from collections import defaultdict
from collections import Counter
from collections import deque
from collections import namedtuple
from enum import Enum

if __name__ == '__main__':

    colours = (
        ('Yasoob', 'Yellow'),
        ('Ali', 'Blue'),
        ('Arham', 'Green'),
        ('Ali', 'Black'),
        ('Yasoob', 'Red'),
        ('Ahmed', 'Silver'),
    )

    # defaultdict
    favourite_colours = defaultdict(list)
    for name, colour in colours:
        favourite_colours[name].append(colour)
    print(favourite_colours)

    # counter
    favs = Counter(name for name, colour in colours)
    print(favs)

    # deque
    d = deque()
    d.append('1')
    d.append('2')
    d.append('3')
    print(len(d))
    print(d[0])
    print(d[-1])

    d = deque(range(5))
    print(len(d))
    d.popleft()
    d.pop()
    print(d)

    d = deque([1, 2, 3, 4, 5])
    d.extendleft([0])
    d.extend([6, 7, 8])
    print(d)

    # namedtuple
    Animal = namedtuple('Animal', 'name age type')
    perry = Animal(name="perry", age=31, type="cat")
    print(perry)
    try:
        perry.age = 42
    except Exception as e:
        print(e)
    print(perry[0])
    print(perry._asdict())

    # enum.Enum
    class Species(Enum):
        cat = 1
        dog = 2
        horse = 3
        aardvark = 4
        butterfly = 5
        owl = 6
        platypus = 7
        dragon = 8
        unicorn = 9
        kitten = 1
        puppy = 2

    Animal = namedtuple('Animal', 'name age type')
    perry = Animal(name="Perry", age=31, type=Species.cat)
    drogon = Animal(name="Drogon", age=4, type=Species.dragon)
    tom = Animal(name="Tom", age=75, type=Species.cat)
    charlie = Animal(name="Charlie", age=2, type=Species.kitten)

    print(charlie.type == tom.type)
    print(charlie.type)

    print(Species(1))
    print(Species['cat'])
    print(Species.cat)
