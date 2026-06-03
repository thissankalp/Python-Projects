# API Integration & Data Handling Portfolio

Welcome to my Python learning journey! This repository contains three progressive projects designed to master interacting with external REST APIs, parsing JSON payloads, managing state, and implementing local data persistence.

---

## 🗺️ The Learning Roadmap

The scripts are designed to be read and executed in order. Each version introduces a foundational programming concept that builds directly upon the last.

---

## 🚀 Projects & Learning Outcomes

### 🔍 1. GitHub Account Finder (`github_finder.py`)
**What was made:** A profile lookup utility that connects to the live GitHub REST API. Users type in any public username, and the script fetches and formats their profile information.

**What was learned:**
* **Dynamic URL Formatting:** Moving away from hardcoded data to inject real-time user input (`f"https://api.github.com/users/{username}"`) directly into API endpoints.
* **HTTP Status Code Validation:** Utilizing `response.status_code == 200` to verify if an account exists before attempting to read data, preventing application crashes on invalid inputs (`404 Not Found`).
* **External API Schema Adaptability:** Working with completely different JSON structures, keys, and timestamp data types (`created_at`).

---

### 📍 2. Weather App V1 (`weather_v1.py`)
**What was made:** A lightweight command-line script that displays the current weather for a fixed list of Indian cities (Vadodara, Mumbai, Delhi, Bangalore) using the Open-Meteo API.

**What was learned:**
* **Mapping with Tuples:** Using a Python dictionary to map string keys (City Names) to tuple values (`Latitude`, `Longitude`).
* **Basic `requests.get()`:** Crafting a clean URL string and executing a standard HTTP GET request.
* **Accessing Nested JSON:** Traversing multi-layered API dictionary responses to pull out specific fields like `temperature` and `windspeed`.
* **Value Mapping:** Translating raw API data (WMO numeric weather codes) into human-readable strings using `.get()` with fallback values.

---

### 🏆 3. Weather App V2 (`weather_v2.py`)
**What was made:** An advanced, interactive CLI application featuring an infinite operational loop, data validation, automated text-to-coordinate geocoding, and a persistent search history tracking menu.

**What was learned:**
* **API Chaining:** Passing data seamlessly between independent servers. The script sends a text input to the *Geocoding API*, extracts the precise latitude/longitude from the first matching array index `[0]`, and passes those coordinates into the *Forecast API*.
* **List Indexing Deep Dive:** Understanding why `[0]` is crucial when working with search APIs that return an array/list of matching locations rather than a single dictionary.
* **File I/O and Serialization:** Reading from and writing to local storage using Python's `json` library (`json.load()` and `json.dump()`).
* **Persistent Global State:** Managing a memory list (`cities`) that populates from a physical file (`cities.json`) at startup and automatically appends unique, title-cased entries across restarts.
* **Robust UX Defensiveness:** Implementing `try-except` blocks to handle malformed user choices safely and preventing application loops from breaking on invalid menu options.

---

## 🛠️ Installation & Setup

1. Make sure you have Python 3.x installed.
2. Install the required `requests` library:
   ```bash
   pip install requests