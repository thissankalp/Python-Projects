# To-Do List Applications: Memory vs. File Persistence

This module marks the transition from fetching data from external web APIs to creating and manipulating local databases. It showcases two progressive iterations of a Command Line Interface (CLI) To-Do List application, shifting from volatile in-memory storage to persistent text-file logging.

---

## 🗺️ The To-Do App Learning Roadmap

These two scripts are designed to demonstrate how applications evolve when you add data durability layer constraints.

[To-Do List V1]            --> Master runtime memory management (Lists & Indexing).
│
▼
[To-Do List V2]            --> Transition to physical file storage (File I/O & Buffering).


---

## 🚀 Projects & Learning Outcomes

### 📝 1. To-Do List V1 (`todo_v1.py`)
**What was made:** A classic console-based task manager where users can dynamically add, view, and delete tasks. It relies entirely on a native Python list to keep track of items while the script is executing.

**What was learned:**
* **Volatile Memory Handling:** Understanding that global lists (`tasks = []`) live purely in RAM. Closing the terminal or terminating the program completely wipes the data.
* **Synchronizing User Indexes to Memory Indices:** Navigating the user-experience offset where a user types `1` to select the first task, but the program must translate that into a `0` index value (`index = user_choice - 1`) to accurately pop it from the array.
* **Array Component Removal:** Utilizing the `.pop()` method to safely extract and return an item from a specific position inside a list without breaking the remaining sequence.

---

### 💾 2. To-Do List V2 (`todo_v2.py`)
**What was made:** An advanced task manager that replaces the volatile memory array with a physical document file (`tasks.txt`). Tasks persist permanently, remaining safe and fully retrievable even if you turn off your computer.

**What was learned:**
* **File Appending (`"a"`) vs Writing (`"w"`):** Mastering different file modes. Using mode `"a"` to silently append new lines without wiping the document, and utilizing mode `"w"` to completely overwrite old content when structural updates occur (like deleting a specific line).
* **Line-by-Line File Processing:** Utilizing `.readlines()` to instantly ingest an entire text file and parse each string row into an indexable Python list element.
* **Data Sanitization (`.strip()`):** Dealing with invisible formatting anomalies like trailing newline characters (`\n`) introduced by file saves, and removing them using string stripping methods to ensure clean terminal output.
* **Defensive File Exception Mapping:** Shielding the viewer interface inside a `try-except FileNotFoundError` block, making sure the code handles situations gracefully if a user tries to view tasks before the tracking file has actually been generated on disk.

---

## 🛠️ Usage & Setup

No external libraries or pip installations are required to run these files—they rely purely on Python's robust native built-in functions.

Simply run either version directly through your workspace terminal terminal:
```bash
python todo_v2.py