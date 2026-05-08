# SMART-EXAM-HALL-ANTI-CHEATING

smart exam hall seat allocation and anti cheating system

# 🎓 ExamGuard — Smart Hall Allocator

An intelligent examination hall seating system that minimizes cheating opportunities using constraint-based algorithms and real-time risk visualization.

---

## 📌 Project Overview

ExamGuard automatically allocates exam seats to students ensuring no two students from the same department sit adjacent to each other. It calculates a risk score for every seat, generates a visual heatmap for invigilators, and statistically proves its superiority over random allocation using Monte Carlo simulation.

Built as part of:

- **22AIE112 — Data Structures & Algorithms**
- **22AIE115 — User Interface Design**

---

## 👥 Team

| Name      | Roll Number      |
| --------- | ---------------- |
| Jayan K S | CB.SC.U4AIE25124 |
| Rethesh S | CB.SC.U4AIE25142 |
| Royston R | CB.SC.U4AIE25147 |
| Sathya K  | CB.SC.U4AIE25154 |

**Semester:** II
**Faculties:** Ms. Sruthi S, Ms. Chandni M

---

## 🎯 Objectives

1. **Smart Automation** — Eliminate manual seating by automating the entire allocation process using algorithms
2. **Algorithmic Design** — Enforce department-based constraints so same-dept students are never seated adjacently
3. **Visual Interface** — Highlight potential cheating risk zones visually so invigilators can act fast

---

## ✨ Features

- 🔀 Fisher-Yates shuffle for unbiased student ordering
- ✅ CSP constraint check — no same-dept adjacency
- 🧠 Greedy seat allocation with real-time constraint validation
- 🔴 8-direction weighted risk scoring (cardinal = 3pts, diagonal = 2pts)
- 📊 Hall-wide weighted safety score (0–100%)
- 🗺️ Visual heatmap — GREEN / YELLOW / RED per seat
- 🔁 Monte Carlo simulation — 10 runs comparing Random vs CSP+Greedy
- 📋 Audit report with conflict breakdown
- 🧩 Configurable hall size and department list

---

## 🧠 Algorithms Used

### 1. Fisher-Yates Shuffle

Produces an unbiased random permutation of the student pool before allocation.
Every permutation has equal probability = 1/n!

- Time: `O(n)` | Space: `O(1)`

### 2. CSP Constraint Check — `isSafe()`

Checks left and above neighbours before placing a student.
Rejects placement if neighbour shares the same department.

- Time: `O(1)` | Space: `O(1)`

### 3. Greedy Allocation

For each seat (left-to-right, top-to-bottom), picks the first student from the shuffled pool that passes the CSP check. No backtracking.

- Time: `O(rows × cols × n)` | Space: `O(n)`

### 4. Random Allocation (Baseline)

Sequential fill after Fisher-Yates shuffle. No constraint checking. Used as baseline in simulation.

- Time: `O(n)` | Space: `O(n)`

### 5. 8-Direction Weighted Graph Scorer

Each seat is a graph node. Edges to all 8 neighbours, weighted by direction:

- Cardinal (↑↓←→): weight **3**
- Diagonal (↖↗↙↘): weight **2**

Risk Categories:

- 🟢 `score < 3` → LOW
- 🟡 `score 3–4` → MEDIUM
- 🔴 `score ≥ 5` → HIGH

Time: `O(1)` per seat | Space: `O(1)`

### 6. Weighted Safety Score

score = ((low × 1.0) + (med × 0.6) + (high × 0.1)) / total × 100

dept = dept_names[i % len(dept_names)]
Ensures equal department distribution across the student pool.

- Time: `O(n)` | Space: `O(n)`

### 8. Set-Based Conflict Deduplication

Uses a Python/JS Set with a sorted canonical key to prevent A↔B and B↔A being counted as two conflicts.

- Lookup: `O(1)` avg | Space: `O(k)`

### 9. Monte Carlo Simulation

Runs N=10 iterations of both allocation modes. Computes mean, min, max safety scores. Statistically proves CSP+Greedy consistently outperforms random placement.

- Time: `O(N × rows × cols × n)` | Space: `O(N)`

---

## 📁 Project Structure

examguard/
│
├── uid.html # Full frontend — UI + all algorithms (JS)
├── examguard_algorithms.py # All algorithms converted to Python
└── README.md # This file

---

## 🚀 How to Run

### Web Version (UI)

```bash
# Just open the HTML file in any browser — no server needed
open uid.html

Sample output
=======================================================
  ExamGuard — Smart Hall Allocator (Python Demo)
=======================================================

[1] Generated 40 students across 4 depts
[2] Greedy Allocation done  |  Unplaced: 0
[3] Safety Score : 77%
    LOW=22  MED=14  HIGH=4  TOTAL=40
[7] Running Monte Carlo Simulation (N=10)...
    Random  →  Mean: 60%  Min: 48%  Max: 72%
    Greedy  →  Mean: 85%  Min: 80%  Max: 88%
    Winner  : CSP+Greedy by 25%
=======================================================
```
