import math
#o(n!) and o(1)
# Function to calculate the cost of the solution
def calculate_cost(path, graph):
    cost = 0
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i + 1]]
    cost += graph[path[-1]][path[0]]  # Return to starting city
    return cost

# Function to solve TSP using Branch and Bound
def tsp(graph, n):
    
    # Preprocessing: Calculate first and second minimum distances for each city
    def find_minimums(graph, n):
        first_min = [math.inf] * n
        second_min = [math.inf] * n

        for i in range(n):
            for j in range(n):
                if i != j:
                    if graph[i][j] < first_min[i]:
                        second_min[i] = first_min[i]
                        first_min[i] = graph[i][j]
                    elif graph[i][j] < second_min[i]:
                        second_min[i] = graph[i][j]

        return first_min, second_min

    # Initialize necessary variables
    current_bound = 0
    current_path = [-1] * (n + 1)
    visited = [False] * n

    # Calculate the initial lower bound for the root node
    first_min, second_min = find_minimums(graph, n)
    for i in range(n):
        current_bound += (first_min[i] + second_min[i])
    current_bound = math.ceil(current_bound / 2)

    visited[0] = True
    current_path[0] = 0  # Starting from the first city

    min_cost = math.inf
    final_path = []

    # Helper function to solve the problem using recursion
    def branch_and_bound(current_bound, current_weight, level, current_path, visited):
        nonlocal min_cost, final_path
        
        # If all cities are visited, check the total cost including the return to the start
        if level == n:
            total_cost = current_weight + graph[current_path[level - 1]][current_path[0]]
            if total_cost < min_cost:
                final_path = current_path[:level]  # Copy only valid part of path
                final_path.append(current_path[0])  # Add starting city at end of path
                min_cost = total_cost
            return

        # Explore nodes based on the branch and bound principle
        for i in range(n):
            if graph[current_path[level - 1]][i] != math.inf and not visited[i]:
                temp_bound = current_bound
                temp_weight = current_weight
                current_weight += graph[current_path[level - 1]][i]

                # Calculate the new bound if necessary
                if level == 1:
                    current_bound -= ((first_min[current_path[level - 1]] + first_min[i]) / 2)
                else:
                    current_bound -= ((second_min[current_path[level - 1]] + first_min[i]) / 2)

                # If the new bound is promising, proceed further
                if current_bound + current_weight < min_cost:
                    current_path[level] = i
                    visited[i] = True

                    # Recursively call for the next level
                    branch_and_bound(current_bound, current_weight, level + 1, current_path, visited)

                # Reset the weight and bound to their original state
                current_weight -= graph[current_path[level - 1]][i]
                current_bound = temp_bound
                visited[i] = False

    # Start the Branch and Bound process
    branch_and_bound(current_bound, 0, 1, current_path, visited)

    return min_cost, final_path

# Example usage
if __name__ == "__main__":
    # Graph representing the cost of traveling between cities
    graph = [
        [math.inf, 10, 15, 20],
        [10, math.inf, 35, 25],
        [15, 35, math.inf, 30],
        [20, 25, 30, math.inf]
    ]

    n = len(graph)
    min_cost, final_path = tsp(graph, n)

    print("Minimum cost:", min_cost)
    print("Path:", final_path)