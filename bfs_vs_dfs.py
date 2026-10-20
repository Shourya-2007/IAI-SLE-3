from collections import deque
import timeit

# ==========================================
# 1. Graph Data Setup
# ==========================================
NUM_NODES = 100
START_NODE = 0

# Creating 100-node sequential adjacency graph (0 -> 1 -> 2 -> ... -> 99)
graph = {i: [] for i in range(NUM_NODES)}
for i in range(NUM_NODES - 1):
    graph[i].append(i + 1)


# ==========================================
# 2. Search Services (BFS & DFS Components)
# ==========================================
def bfs(start_node, goal_node):
    """
    Breadth-First Search using collections.deque (FIFO queue).
    Tracks visited nodes and nodes_expanded counter.
    """
    nodes_expanded = 0
    visited = set()
    queue = deque([start_node])
    found = False

    while queue:
        current = queue.popleft()

        if current not in visited:
            visited.add(current)
            nodes_expanded += 1

            if current == goal_node:
                found = True
                break

            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return {"found": found, "nodes_expanded": nodes_expanded}


def dfs(start_node, goal_node):
    """
    Depth-First Search using a Python list as a stack (LIFO stack).
    Tracks visited nodes and nodes_expanded counter.
    """
    nodes_expanded = 0
    visited = set()
    stack = [start_node]
    found = False

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.add(current)
            nodes_expanded += 1

            if current == goal_node:
                found = True
                break

            # Reverse neighbours so left-to-right order is preserved on popping
            for neighbor in reversed(graph.get(current, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return {"found": found, "nodes_expanded": nodes_expanded}


# ==========================================
# 3. Measurement & Profiling Wrapper
# ==========================================
def profile_algorithm(algo_func, start_node, goal_node, runs=3):
    """
    Wraps search algorithm execution with timeit and calculates average runtime.
    Returns average execution time in milliseconds, last node count, and found status.
    """
    total_time_ms = 0.0
    last_result = None

    for _ in range(runs):
        start_time = timeit.default_timer()
        result = algo_func(start_node, goal_node)
        end_time = timeit.default_timer()

        execution_time_ms = (end_time - start_time) * 1000
        total_time_ms += execution_time_ms
        last_result = result

    avg_time_ms = total_time_ms / runs
    return avg_time_ms, last_result["nodes_expanded"], last_result["found"]


# ==========================================
# 4. Experiment Driver (Main Script Execution)
# ==========================================
def run_experiment():
    print("=" * 75)
    print(" GRAPH SEARCH PERFORMANCE STUDY — BFS vs DFS")
    print(" System: 100-Node Sequential Graph | Start Node = 0 | 3 Timing Runs")
    print("=" * 75)

    experiment_cases = [
        ("Best Case", 1),
        ("Average Case", 50),
        ("Worst Case", 99),
    ]

    for case_name, goal_node in experiment_cases:
        print(f"\n--- Testing Scenario: Goal Node = {goal_node} ({case_name}) ---")

        # Profile BFS
        bfs_avg_time, bfs_nodes, bfs_found = profile_algorithm(
            bfs, START_NODE, goal_node, runs=3
        )

        # Profile DFS
        dfs_avg_time, dfs_nodes, dfs_found = profile_algorithm(
            dfs, START_NODE, goal_node, runs=3
        )

        # Display Results
        print(f"{'Metric':<30} | {'BFS':<18} | {'DFS':<18}")
        print("-" * 72)
        print(f"{'Goal Found':<30} | {str(bfs_found):<18} | {str(dfs_found):<18}")
        print(f"{'Nodes Expanded':<30} | {bfs_nodes:<18} | {dfs_nodes:<18}")
        print(
            f"{'Avg Exec Time (ms)':<30} | {bfs_avg_time:<18.6f} | {dfs_avg_time:<18.6f}"
        )
        print("-" * 72)

    print("\n" + "=" * 75)
    print(" EXPERIMENT COMPLETE")
    print("=" * 75)


if __name__ == "__main__":
    run_experiment()