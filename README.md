# 🚀 Graph Search Performance Study Engine (BFS vs DFS)

---

## 📌 Project Overview :

The **Graph Search Performance Study Engine** is an AI execution and empirical analysis framework developed for comparing two graph-traversal strategies: **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**[cite: 1, 5]. 

Designed for the course **02AML204 — Introduction to Artificial Intelligence**, this program creates a standard **100-node sequential adjacency graph setup** (Start Node: `0`) and profiles traversal performance across three distinct goal positions (`1`, `50`, and `99`)[cite: 1, 5]. Each search is profiled over three runs using Python's `timeit` module while recording the exact number of expanded nodes[cite: 1, 5]. The system design is modeled using the **C4 Software Architecture Framework** (Levels 1 through 4) to ensure clarity, modularity, and clean separation between search logic and performance profiling[cite: 1, 6].

---


## 🏛️ Architectural Design (Full C4 Model) :

The system architecture follows the 4-level C4 model, structured using standard C4 visual layouts:

### 📍 Level 1: System Context Diagram :

Defines the system boundaries and external interactions between the Student/Operator, the central Graph Search System, and the Python Execution Environment[cite: 5].

![Level 1 Context Diagram](./Screenshot%202026-10-20%20123444.png)[cite: 5]

* **Input Parameters:** 100 nodes | Start node `0` | Goal nodes (`1`, `50`, `99`) | 3 timing runs[cite: 5].
* **System Boundary:** Coordinates search execution, collects search status, nodes expanded, and measured average execution time[cite: 5].
* **Execution Environment:** Python runtime supplying `timeit` measurement module and `collections.deque` for BFS[cite: 5].

---

### 📍 Level 2: Container / Architecture View :

Organizes the system into five primary functional responsibility boundaries[cite: 6]:

![Level 2 Container Diagram](./Screenshot%202026-10-20%20123452.png)[cite: 6]

1. **1. Graph Setup:** Creates the 100-node adjacency structure and supplies the common graph[cite: 6].
2. **2. Search Services:** Houses BFS and DFS services receiving start + goal inputs and returning search status/count[cite: 6].
3. **3. Experiment Driver:** Runs selected goal cases and invokes each search algorithm[cite: 6].
4. **4. Traversal State:** Manages frontier structures (Visited set, BFS `deque`, DFS `stack`, and Node counter)[cite: 6].
5. **5. Measurement & Report:** Tracks `timeit` timing, average time, nodes expanded, and final comparison[cite: 6].

---

### 📍 Level 3: Component View :

Zooms inside the **Search Services** container to detail algorithm components[cite: 7]:

![Level 3 Component Diagram](./Screenshot%202026-10-20%20123500.png)[cite: 7]

* **BFS Component:** `bfs(start_node, goal_node)` — 1. Put start node into FIFO deque. 2. Remove the next node. 3. Check the goal. 4. Add unvisited neighbours. 5. Increase `nodes_expanded`. Shared output: `found` + `nodes_expanded`[cite: 7].
* **DFS Component:** `dfs(start_node, goal_node)` — 1. Put start node into LIFO stack. 2. Pop the next node. 3. Check the goal. 4. Push unvisited neighbours. 5. Increase `nodes_expanded`. Shared output: `found` + `nodes_expanded`[cite: 7].
* **Interface Specification:** Common interface with different traversal strategies: FIFO queue versus LIFO stack[cite: 7].

---

### 📍 Level 4: Code / Function Map :

Maps the core functions, variables, and execution dependencies[cite: 8]:

![Level 4 Code Diagram](./Screenshot%202026-10-20%20123507.png)[cite: 8]

* `bfs(start_node, goal_node)`: Uses `collections.deque`, maintains visited set + node counter[cite: 8].
* `dfs(start_node, goal_node)`: Uses Python `list` as stack, maintains visited set + node counter[cite: 8].
* `profile_algorithm(algo_func, start_node, goal_node, runs=3)`: Uses `timeit` and returns average timing[cite: 8].
* `Main Script (bfs_vs_dfs.py)`: Coordinates the experiment and calls search/profiling functions[cite: 8].
* **Graph Data:** `NUM_NODES = 100`, sequential adjacency list, `Start node = 0`[cite: 8].
* **Experiment Cases:** Best (`goal 1`), Average (`goal 50`), Worst (`goal 99`)[cite: 8].
* **Dependencies:** `timeit` for timing measurement, `collections.deque` for BFS queue[cite: 8].

---

## 📊 Benchmarking & Experiment Configuration :

| Experiment Parameter | Value / Configuration |
| :--- | :--- |
| **Total Graph Nodes** | 100 Nodes (Sequential Adjacency List)[cite: 5, 8] |
| **Start Node** | Node `0`[cite: 5, 8] |
| **Goal Nodes Tested** | `1` (Best), `50` (Average), `99` (Worst)[cite: 5, 8] |
| **Profiling Tool** | Python `timeit` module (3 runs average)[cite: 5, 8] |
| **BFS Frontier Structure** | `collections.deque` (FIFO Queue)[cite: 5, 7, 8] |
| **DFS Frontier Structure** | Python `list` (LIFO Stack)[cite: 6, 7, 8] |

---

## ⚙️ Architectural Decisions :

1. **Shared Graph Instance:** BFS and DFS use the same generated graph so the experiment compares traversal strategy rather than different input data[cite: 1].
2. **Standardized Interface:** The search functions expose a similar result structure, making them easy to benchmark through the same profiling function[cite: 1].
3. **Decoupled State & Timing:** Traversal state is kept separate conceptually from experiment timing so search logic is not mixed with measurement logic[cite: 1].
4. **Multi-Goal Testing:** Three goal positions are used to represent best, average, and worst search situations[cite: 1].

---

