class fk:
    def __init__(self,value,weight):
        self.value = value
        self.weight = weight
        self.ratio = value/weight
def frac_sack(items,capacity):
    total_weight = 0.0
    total_value =0.0
    items.sort(key = lambda item:item.ratio, reverse=True)
    for item in items:
        if total_weight + item.weight <= capacity:
            total_weight += item.weight
            total_value += item.value
        else:
            rem =  capacity - total_weight
            total_value += (item.ratio * rem)
            break
    return total_value

n = int(input("total no of items"))
c = int(input("total no of capacity"))
items=[]
print("taking items")
for i in range(0,n):
    value = int(input("enter value"))
    weight = int(input("enter weght"))
    item = fk(value,weight)
    items.append(item)
print("Max profit:",frac_sack(items,c))
