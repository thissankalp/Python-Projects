# Expense Tracker Applications: Complex Data Structures & Mapping

This module advances from simple string data management to handling rich, relational information. It showcases two progressive iterations of a Command Line Interface (CLI) Expense Tracker, introducing structured Python dictionaries, complex analytical loops, and persistent multi-attribute data serialization.

---

## 🗺️ The Expense Tracker Learning Roadmap

These two scripts are designed to demonstrate how apps evolve when transitioning from standard recording tools to complex financial reporting and data management systems.

[Expense Tracker V1]        --> Learn nested data structures (List of Dictionaries).
│
▼
[Expense Tracker V2]        --> Master dynamic grouping, data filtering, and JSON persistence.


---

## 🚀 Projects & Learning Outcomes

### 📊 1. Expense Tracker V1 (`expense_v1.py`)
**What was made:** A basic terminal ledger where users record transactions containing a category, cost, and memo description. It calculates runtime aggregates but loses all data upon program termination.

**What was learned:**
* **Composite Data Collections:** Implementing a **List of Dictionaries** (`[{}]`) data architecture to handle complex, multi-variable entities under a unified, indexable array.
* **String Formatting Precision:** Utilizing floating-point layout syntax (`f"₹{value:.2f}"`) to automatically round numbers and match monetary presentation standards.
* **Accumulator Loops:** Writing basic accumulation passes to traverse structured objects, isolate specific numeric key values (`expense['amount']`), and dynamically track calculations.

---

### 📈 2. Expense Tracker V2 (`expense_v2.py`)
**What was made:** An enterprise-grade localized ledger upgrading the initial engine with transactional persistence, algorithmic category grouping, individual metric deletions, and case-insensitive pattern filters.

**What was learned:**
* **Structured JSON Formatting:** Serializing composite nested data arrays cleanly to a local disk (`expenses.json`) using multi-space element indents to ensure the backend file matches human-readable structures.
* **Dynamic Map Generation:** Building custom frequency tables on the fly. Isolating structural object keys to systematically create tracking maps, initialize unseen fields (`summary[category] = 0`), and dynamically generate data categories.
* **Case-Insensitive String Filtering:** Employing text normalization matching (`.lower()`) to run complex structural filters without forcing rigid capitalization requirements on user search parameters.
* **Data Sequence Safety Checkers:** Designing robust conditional validation logic (`choice <= 1 or choice > len(expenses)`) to protect structured matrix entries against range violations and offset faults during runtime array adjustments.

---

## 🛠️ Usage & Setup

No external dependencies are required to execute these modules—they rely exclusively on native core Python libraries.

Execute either file version straight through your system console:
```bash
python expense_v2.py