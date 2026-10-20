---

### 2. `AI_contribution_log.md`

```markdown
# 🤖 AI Contribution Log :

## 📝 Overview :
This document logs all interactions, architectural guidance, profiling advice, and content formatting conducted in collaboration with **Gemini AI** during the completion of the **SLE-3 Architectural Design (Full C4 Model)** assignment for course **02AML204 — Introduction to Artificial Intelligence**[cite: 1].

---

## Breakdown of Contributions :

### 1. AI Tools Used :

* **Primary AI Assistant:** Gemini AI[cite: 1]
* **Diagramming Platform:** Draw.io / Diagrams.net

---

### 2. What AI Helped With :

#### A. Programming & Logic Guidance :
* **Node-Counting Integration:** Assisted with node-counting logic and tracking `nodes_expanded` across traversal iterations[cite: 1, 7].
* **Profiling Guidance:** Provided guidance on profiling and timing setup using Python's `timeit` module across 3 timing runs[cite: 1, 8].

#### B. Architectural Modeling (C4 Framework) :
* **4-Level C4 Modeling:** Guided the creation of the complete C4 model across System Context, Container Architecture, Component View, and Code/Function Map[cite: 1, 5, 6, 7, 8].
* **Responsibility Boundaries:** Assisted in defining five responsibility-based containers (Graph Setup, Search Services, Experiment Driver, Traversal State, Measurement & Report)[cite: 1, 6].

#### C. Documentation & Support :
* **Architectural Decisions:** Assisted in documenting architectural choices (e.g., separating traversal state from measurement logic)[cite: 1].
* **Documentation Formatting:** Provided documentation support and generated Markdown repository files (`README.md` and `AI_contribution_log.md`)[cite: 1].

---

### 3. What I Did Myself (Human Contribution) :

* **Experiment Configuration:** Configured the 100-node sequential graph experiment parameters (Start Node: `0`, Goal Nodes: `1`, `50`, `99`)[cite: 1, 5].
* **Program Execution:** Ran the Python search experiment, collected timing metrics and node counts across 3 runs per goal position[cite: 1, 5].
* **C4 Diagram Construction:** Manually built, connected, and styled all 4 levels of C4 diagrams in Draw.io matching the supplied program implementation[cite: 1, 5, 6, 7, 8].
* **Outputs Verification:** Checked execution outputs, verified algorithm results, and wrote the final architectural analysis report[cite: 1].

---

## Interaction Summary Log :

| Phase | Assistance Requested | AI Output / Resolution |
| :--- | :--- | :--- |
| **Phase 1: Setup & Logic** | Guidance on node-counting logic and `timeit` execution | Provided code structure for `profile_algorithm()` and node tracking[cite: 1, 8]. |
| **Phase 2: Architectural Design** | Structuring system into 4 C4 model levels | Mapped responsibilities into 5 containers and context boundaries[cite: 1, 5, 6]. |
| **Phase 3: Component & Code View** | Modeling BFS/DFS interfaces and function maps | Detailed component operations and code function dependencies[cite: 1, 7, 8]. |
| **Phase 4: Documentation** | Formatting repository documentation and logs | Generated complete Markdown files for repository submission[cite: 1]. |

---

## 📜 Verification Statement :
I confirm that AI assistance (Gemini) was used ethically for programming guidance, profiling advice, node-counting logic, and documentation support[cite: 1]. All experiment configurations, program executions, timing checks, diagram modeling, and analysis were completed and verified by me[cite: 1].
