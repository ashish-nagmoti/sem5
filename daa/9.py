from queue import PriorityQueue
class item:
	def __init__(self,weight,value):
		self.weight = weight
		self.value = value
		self.ratio = value/weight
class Node:
	def __init__(self,level,profit,weight,bound):
		self.level = level
		self.profit = profit
		self.weight = weight
		self.bound = bound
	def __lt__(self,other):
		return self.bound > other.bound

def calculate_bound(node,n,capacity, items):
	if node.weight >= capacity:
		return 0
	profit_bound = node.profit
	total_weight = node.weight
	j = node.level+1
	while j<n and total_weight + items[j].weight <=capacity:
		total_weight += items[j].weight
		profit_bound += items[j].value
		j+=1
	if j<n:
		profit_bound += (capacity-total_weight)*items[j].ratio
	return profit_bound

def knapsack(weights,values,capacity):
	items = [ item(weights[i],values[i]) for i in range(len(weights))]
	items.sort(key = lambda x:x.ratio, reverse =True)
	pq = PriorityQueue()
	u  = Node(-1,0,0,0)
	v = Node(0,0,0,0)
	max_profit = 0
	u.bound = calculate_bound(u,len(items),capacity,items)
	pq.put(u) 
	while not pq.empty():
		u = pq.get()
		if u.bound > max_profit:
			v.level = u.level+1
			v.weight = u.weight + items[v.level].weight
			v.profit = u.profit + items[v.level].value
	
			if v.weight <= capacity and v.profit>max_profit:
				max_profit = v.profit
			v.bound = calculate_bound(v,len(items),capacity,items)
			if v.bound > max_profit:
				pq.put(Node(v.level,v.profit,v.weight,v.bound))
			v.weight = u.weight
			v.profit = u.profit
			v.bound = calculate_bound(v,len(items),capacity,items)
			if v.bound > max_profit:
				pq.put(Node(v.level,v.profit,v.weight,v.bound))
	return max_profit
if __name__ == "__main__":
	values = [40, 42, 25, 12]
	weights = [4, 7, 5, 3]
	capacity = 10
	max_profit = knapsack(weights, values, capacity)
	print(f"Maximum profit is {max_profit}")