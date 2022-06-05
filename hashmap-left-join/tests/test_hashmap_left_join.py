from hashmap_left_join.hashmap_left_join import hashmap_left_join
from hashmap_left_join.hahtable import HashTable
hashmap1 = HashTable()
hashmap2 = HashTable()
hashmap1.__setitem__("diligent","employed")
hashmap1.__setitem__("fond","enamored")
hashmap1.__setitem__("guide","usher")
hashmap1.__setitem__("outfit","garb")
hashmap1.__setitem__("wrath","anger")
hashmap2.__setitem__("diligent","idle")
hashmap2.__setitem__("fond","averse")
hashmap2.__setitem__("guide","follow")
hashmap2.__setitem__("flow","jam")
hashmap2.__setitem__("wrath","delight")


def test_one():
    actual=hashmap_left_join(hashmap1,hashmap2)
    excepted=[['wrath', 'anger', 'delight'],
['outfit', 'garb', 'Null'],
['diligent', 'employed', 'idle'],
['guide', 'usher', 'follow'],
['fond', 'enamored', 'averse']]
