# 🌳 Depth First Search (DFS) Using Recursion in Python

This repository demonstrates the implementation of **Depth First Search (DFS)** using **recursion** in Python. It includes a simple graph example, source code, explanation, dry run, recursion call stack, and time & space complexity.

---

## 📖 What is DFS?

Depth First Search (DFS) is a graph traversal algorithm that explores one branch completely before moving to another branch. It uses **recursion** (or a stack) to traverse all the nodes of a graph or tree.

---

## 📊 Example Graph

```text
        0
      /   \
     1     2
    / \     \
   3   4     5
```

### DFS Traversal

```text
0 → 1 → 3 → 4 → 2 → 5
```

---

## 📂 Project Structure

```
DFS-Using-Recursion/
│── dfs.py          # Python implementation
│── README.md       # Documentation
```

---

## 💻 Python Code

```python
graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5],
    3: [],
    4: [],
    5: []
}

visited = set()

def dfs(node):
    visited.add(node)
    print(node, end=" ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(neighbour)

print("DFS Traversal:")
dfs(0)
```

---

## 📤 Output

```text
DFS Traversal:
0 1 3 4 2 5
```

---

## ⏱️ Time Complexity

- **Time Complexity:** `O(V + E)`

Where:
- **V** = Number of vertices
- **E** = Number of edges

---

## 💾 Space Complexity

- **Space Complexity:** `O(V)`

---

## 📚 Applications of DFS

- Graph Traversal
- Tree Traversal
- Path Finding
- Cycle Detection
- Topological Sorting
- Connected Components

---

## 🛠️ Technologies Used

- Python 3
- Recursion
- Graph (Adjacency List)

---

## 👨‍💻 Author

**Palak Bharat Paryani**
