#1. FISHER-YATES SHUFFLE ALGORITHM
import random

def fisher_yates_shuffle(array):
    """
    Fisher-Yates Shuffle Algorithm
    Time: O(n), Space: O(1)
    """
    n = len(array)
    
    # Iterate backwards from last to second element
    for i in range(n - 1, 0, -1):
        # Pick random index from 0 to i
        j = random.randint(0, i)
        
        # Swap elements
        array[i], array[j] = array[j], array[i]
#2. CONSTRAINT SATISFACTION ALGORITHM
def is_safe(hall, row, col, student):
    """
    Check if placing student violates constraints
    Time: O(1), Space: O(1)
    """
    # Define directions to check (left and top only)
    directions = [(0, -1), (-1, 0)]
    
    # Check each neighbor
    for delta_row, delta_col in directions:
        neighbor_row = row + delta_row
        neighbor_col = col + delta_col
        
        # Check if within bounds
        if neighbor_row >= 0 and neighbor_col >= 0:
            neighbor = hall[neighbor_row][neighbor_col]
            
            # If neighbor exists and same department
            if neighbor and neighbor["dept"] == student["dept"]:
                return False  # Constraint violated
    
    return True  # Safe to place
#3. GREEDY ALLOCATION ALGORITHM
def greedy_allocation(hall, students, rows, cols):
    """
    Greedy seat allocation algorithm
    Time: O(n²), Space: O(n)
    """
    # Shuffle students first for fairness
    fisher_yates_shuffle(students)
    
    # Process each seat row-by-row, left-to-right
    for row in range(rows):
        for col in range(cols):
            
            # Try each student in current list
            for i in range(len(students)):
                student = students[i]
                
                # Check if placement is safe
                if is_safe(hall, row, col, student):
                    # Greedy choice: place first valid student
                    hall[row][col] = student
                    
                    # Remove placed student from list
                    students.pop(i)
                    break  # Move to next seat (no backtracking)
    
    return hall
#4. GRAPH ADJACENCY SEARCH ALGORITHM
def get_risk_neighbors(hall, row, col, rows, cols):
    """
    Find all same-department neighbors (8 directions)
    Time: O(1), Space: O(1)
    """
    # Define all 8 directions (4 direct + 4 diagonal)
    directions = [
        {"delta": (0, 1),   "type": "direct"},    # right
        {"delta": (1, 0),   "type": "direct"},    # down
        {"delta": (0, -1),  "type": "direct"},    # left
        {"delta": (-1, 0),  "type": "direct"},    # up
        {"delta": (1, 1),   "type": "diagonal"},  # down-right
        {"delta": (1, -1),  "type": "diagonal"},  # down-left
        {"delta": (-1, 1),  "type": "diagonal"},  # up-right
        {"delta": (-1, -1), "type": "diagonal"}   # up-left
    ]
    
    current_student = hall[row][col]
    
    # If seat empty, no risk neighbors
    if not current_student:
        return []
    
    risk_neighbors = []
    
    # Check each of 8 directions
    for direction in directions:
        delta_row, delta_col = direction["delta"]
        neighbor_row = row + delta_row
        neighbor_col = col + delta_col
        
        # Check if within bounds
        if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
            neighbor_student = hall[neighbor_row][neighbor_col]
            
            # If neighbor exists and same department
            if neighbor_student and neighbor_student["dept"] == current_student["dept"]:
                risk_neighbors.append({
                    "row": neighbor_row,
                    "col": neighbor_col,
                    "type": direction["type"],
                    "dept": neighbor_student["dept"]
                })
    
    return risk_neighbors
#5. WEIGHTED SCORING ALGORITHM
def get_risk_score(hall, row, col, rows, cols):
    """
    Calculate weighted risk score for a seat
    Time: O(1), Space: O(1)
    """
    # Get all same-department neighbors
    risk_neighbors = get_risk_neighbors(hall, row, col, rows, cols)
    
    # If no risk neighbors, score is 0
    if not risk_neighbors:
        return 0
    
    total_score = 0
    
    # Apply weighted scoring
    for neighbor in risk_neighbors:
        if neighbor["type"] == "direct":
            total_score += 3  # Direct neighbor weight
        elif neighbor["type"] == "diagonal":
            total_score += 2  # Diagonal neighbor weight
    
    return total_score


def get_risk_category(score):
    """
    Categorize risk level based on score
    """
    if score < 3:
        return "LOW"      # Green
    elif 3 <= score <= 4:
        return "MEDIUM"   # Yellow
    else:
        return "HIGH"     # Red (score
    
import random

# ── 1. Fisher-Yates Shuffle ──────────────────────────────────────────
array = [1, 2, 3, 4, 5]
fisher_yates_shuffle(array)
print(array)  # shuffled in-place

# ── 2. is_safe ───────────────────────────────────────────────────────
rows, cols = 3, 3
hall = [[None]*cols for _ in range(rows)]

student_a = {"name": "Alice", "dept": "CS"}
student_b = {"name": "Bob",   "dept": "Math"}

hall[0][0] = student_a
print(is_safe(hall, 0, 1, student_a))  # False — same dept, adjacent
print(is_safe(hall, 0, 1, student_b))  # True  — different dept

# ── 3. Greedy Allocation ─────────────────────────────────────────────
rows, cols = 3, 3
hall = [[None]*cols for _ in range(rows)]

students = [
    {"name": "Alice", "dept": "CS"},
    {"name": "Bob",   "dept": "Math"},
    {"name": "Carol", "dept": "CS"},
    {"name": "Dave",  "dept": "EE"},
    {"name": "Eve",   "dept": "Math"},
]

result = greedy_allocation(hall, students, rows, cols)
for row in result:
    print([s["name"] if s else "---" for s in row])

# ── 4. get_risk_neighbors ────────────────────────────────────────────
rows, cols = 3, 3
hall = [[None]*cols for _ in range(rows)]

hall[1][1] = {"name": "Alice", "dept": "CS"}
hall[0][1] = {"name": "Carol", "dept": "CS"}   # direct neighbor (up)
hall[1][2] = {"name": "Dave",  "dept": "EE"}   # different dept
hall[0][0] = {"name": "Eve",   "dept": "CS"}   # diagonal neighbor

neighbors = get_risk_neighbors(hall, 1, 1, rows, cols)
print(neighbors)

# ── 5. get_risk_score & get_risk_category ────────────────────────────
score = get_risk_score(hall, 1, 1, rows, cols)
print(score)                    # 3 (direct=3) + 2 (diagonal=2) = 5
print(get_risk_category(score)) # "HIGH"