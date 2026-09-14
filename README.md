# OS-task1

## 🧵 Operating Systems — Thread-Based Implementations

This repository contains two Python implementations demonstrating fundamental Operating Systems and multithreading concepts:

1. **Producer-Consumer Problem using Python Threads**
2. **Matrix Multiplication using Python Threads with Animation**

The programs demonstrate thread creation, concurrent execution, shared resources, synchronization, circular buffers, thread coordination, and parallel computation.

---

## 📌 Overview

The assignment includes the following concepts:

- Thread creation and execution
- Concurrent task execution
- Shared-memory access
- Synchronization
- Circular buffer implementation
- Producer-consumer coordination
- Thread completion using `join()`
- Matrix multiplication
- Result verification
- Visualization of computation using animation

---

## 📂 Files in This Repository

| File | Description |
|------|-------------|
| `producer_consumer.py` | Implementation of the Producer-Consumer problem using Python threads |
| `matrix_multiplication.py` | Thread-based multiplication of two 100 × 100 matrices |
| `matrix_multiplication.gif` | Animation of the matrix multiplication result |
| `README.md` | Project documentation |

> If your actual filename contains spaces or numbering, update the names in this table and in the run commands below.

---

# 1️⃣ Producer-Consumer Problem Using Threads

## 📖 Description

The Producer-Consumer problem is a classic synchronization problem in Operating Systems.

A **Producer thread** creates items and places them into a shared buffer. A **Consumer thread** removes items from the same buffer.

This implementation uses a fixed-size circular buffer with a capacity of 5. The producer adds 10 items, and the consumer removes the same 10 items.

The producer and consumer use a condition variable to coordinate their actions and safely access the shared buffer.

## ⚙️ How It Works

- The buffer has a fixed capacity of 5.
- The producer inserts items at the next available position.
- The consumer removes items from the next occupied position.
- The insertion and removal positions move in a circular manner.
- The producer waits when the buffer is full.
- The consumer waits when the buffer is empty.
- The condition variable protects access to the shared buffer.
- The waiting thread is notified after the buffer state changes.

The circular movement of the positions can be represented as:

```text
next_position = (current_position + 1) % buffer_size
```

## 🧠 Concepts Demonstrated

- Python threads
- Producer-consumer synchronization
- Shared resources
- Fixed-size circular buffer
- Locks
- Condition variables
- Waiting and notification
- Concurrent execution

## ▶️ How to Run

Install Python 3 and run:

```bash
python producer_consumer.py
```

## 🖥️ Sample Output

```text
Producer added item 1
Producer added item 2
Consumer took item 1
Producer added item 3
Consumer took item 2
Producer added item 4
Consumer took item 3
...
All items were produced and consumed.
```

The exact order of the output may change because the producer and consumer execute concurrently.

---

# 2️⃣ Matrix Multiplication Using Python Threads

## 📖 Description

The second program performs multiplication of two randomly generated **100 × 100 matrices** using Python threads.

For every cell in the result matrix, a separate thread is created. Each thread calculates one element of the result matrix by multiplying one row of Matrix A with one column of Matrix B.

After the threaded multiplication is completed, the result is verified using NumPy's matrix multiplication operation.

## ⚙️ How It Works

The matrix multiplication process is:

```text
Matrix A (100 × 100) × Matrix B (100 × 100)
                    ↓
             Matrix C (100 × 100)
```

The result matrix contains:

```text
100 × 100 = 10,000 cells
```

For each result cell `C[row][column]`, the program calculates:

```text
C[row][column] =
A[row] × B[column]
+ A[row] × B[column][1]
+ ...
+ A[row] × B[column][2]
```

Each thread performs the calculation for one result cell.

## 🔹 Thread Execution

- A thread is created for each column within the current row.
- The thread calculates one cell of the result matrix.
- The `start()` method begins thread execution.
- The `join()` method makes the main program wait until the thread finishes.
- The program processes all rows and columns.
- The completed result is compared with NumPy's expected result.

## ✅ Result Verification

The program uses NumPy to calculate an expected result:

```python
expected = matA @ matB
```

The threaded result is compared with this expected result using:

```python
np.array_equal(result, expected)
```

If both results are equal, the program displays:

```text
Result verified successfully.
```

## 🎬 Matrix Multiplication Animation

The animation displays three panels:

- **Matrix A** — the first input matrix.
- **Matrix B** — the second input matrix.
- **Result Matrix C** — the result of the multiplication.

The animation gradually reveals the values in the result matrix. The highlighted row, column, and cell show the current part of the matrix being displayed.

The completed animation is saved as:

```text
matrix_multiplication.gif
```

### 🎥 Animation

![Matrix Multiplication Animation](matrix_multiplication.gif)

## ▶️ Installation

Install the required Python libraries:

```bash
pip install numpy matplotlib pillow
```

## ▶️ How to Run

```bash
python matrix_multiplication.py
```

The program calculates and verifies the matrix multiplication result. A Matplotlib window then displays the animation, and the GIF is saved in the project folder.

## 🖥️ Sample Output

```text
Starting threaded matrix multiplication...
Threaded multiplication completed.
Result verified successfully.
Matrix size: 100 x 100
Total multiplication operations: 10000
Saving animation as GIF...
GIF saved successfully!
```

---

# 🔄 Difference Between the Two Implementations

| Feature | Producer-Consumer | Matrix Multiplication |
|--------|-------------------|-----------------------|
| Main purpose | Thread communication and synchronization | Parallel division of a calculation |
| Shared data | Fixed-size circular buffer | Result matrix |
| Number of items or tasks | 10 items | 10,000 result cells |
| Thread roles | Producer and Consumer | Matrix calculation threads |
| Synchronization concept | Condition variable and waiting | `join()` for thread completion |
| Main output | Items added and removed | Verified matrix and animation |
| Main Operating Systems concept | Shared-resource coordination | Concurrent task execution |

---

# 🛠️ Technologies Used

- Python 3
- Python `threading` module
- NumPy
- Matplotlib
- Pillow
- Matplotlib Animation

---

# 📋 Requirements

- Python 3.9 or above
- NumPy
- Matplotlib
- Pillow

Install the dependencies using:

```bash
pip install numpy matplotlib pillow
```

The Producer-Consumer program uses only Python's built-in `threading` module.

---

# 🎯 Learning Outcomes

After completing these programs, the following concepts are demonstrated:

- Creating and running threads.
- Sharing data between multiple threads.
- Protecting shared resources.
- Implementing a circular buffer.
- Coordinating producer and consumer threads.
- Dividing matrix multiplication into smaller tasks.
- Waiting for threads to finish.
- Verifying computational results.
- Creating an animation to visualize program execution.

---

# ▶️ Complete Execution

Run the Producer-Consumer program:

```bash
python producer_consumer.py
```

Run the threaded matrix multiplication program:

```bash
python matrix_multiplication.py
```

The first program displays producer and consumer activity in the terminal. The second program calculates the matrix result, verifies it, displays the animation, and saves the GIF file.

---

## 👩‍💻 Author

**Disha**

*Operating Systems — Thread-Based Programming Assignment*
