


def hashmap_left_join(hashmap1,hashmap2):
    keys = hashmap1.keys()
    indecies = []
    left_join_table=[]
    for key in keys:
        indecies.append(hashmap1._get_hash(key))

    for idx in indecies:
        if hashmap2.map[idx] !=None:

            left_join_table.append([hashmap1.map[idx][0][0],hashmap1.map[idx][0][1],hashmap2.map[idx][0][1]])

        else:
             left_join_table.append([hashmap1.map[idx][0][0],hashmap1.map[idx][0][1],"Null"])
    return left_join_table


if __name__ == "__main__":
    from hahtable import HashTable
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
    for i in hashmap_left_join(hashmap1,hashmap2):
        print(i)
