---

# 🧹 Student Data Cleaning Project

This project demonstrates **basic data cleaning using Python and Pandas**.
It loads a simple CSV dataset (`students.csv`), removes missing values, fills missing data, and exports a cleaned version.

---

## 📂 Files in this Repository

* **students.csv** → Sample dataset with some missing values.
* **simple data cleaning program.py** → Python script that cleans the dataset.
* **students\_cleaned.csv** → Output file after cleaning (generated when you run the script).
* **README.md** → Documentation with steps.
* **students datacleaning.png** →screenshot of code output

---

## 🐍 Requirements

Make sure you have **Python 3** and **pandas** installed:

```bash
pip install pandas
```

---

## ⚡ What the Script Does

* Drops rows where **Name** is missing.
* Fills missing **Age** with the average of existing ages.
* Fills missing **Marks** with `0`.
* Saves the cleaned dataset as `students_cleaned.csv`.

---

✨ Happy coding and keep your data clean!

---
