# 🧠 Quizzes

A collection of educational **quizzes and mental math trainers** written in MicroPython for the **NumWorks** calculator.

While most scripts in this collection are quick, simple drills, the **English Irregular Verbs Quiz** is the flagship project — complete, structured, and designed so anyone can reuse it as a template for their own calculator quizzes.

---

## 📂 Scripts Included

```
Quizzes/
├── english_irregular_verbs_quiz.py  # Flagship: 157 English irregular verbs, 3 tiers & 4 modes
├── german_quiz.py                   # Minimal 10-word prototype (basis for the English quiz)
├── date_quiz.py                     # Day-of-the-week quiz (0–2100), powered by Time-Tools
└── mental_math/
    ├── square_quiz.py               # Squares of 0–15
    ├── square_root_quiz.py          # Square roots of 15–100
    ├── cube_quiz.py                 # Cubes of 10–100
    └── cube_root_quiz.py            # Cube roots of 10–100
```

---

## 🌟 Flagship Project: `english_irregular_verbs_quiz.py` *(Created May 18, 2023)*

A comprehensive, well-structured trainer covering **157 English irregular verbs**, originally adapted from the `german_quiz.py` layout.

- **3 Cumulative Difficulty Levels**:
  - **Easy** *(26 verbs)* : Past simple and past participle match the base infinitive.
  - **Medium** *(+76 verbs = 102 total)* : Past simple and past participle are identical, but differ from the infinitive.
  - **Hard** *(+55 verbs = all 157)* : All three forms are different.
- **4 Question Modes**:
  1. Find the base **infinitive** given one of the other forms.
  2. **Translate** an English infinitive into French.
  3. **Conjugate** all forms given the infinitive.
  4. Give the **past simple** from a given infinitive.
- **Educational Feedback**: Displays the French translation alongside the infinitive, preterite, and past participle after every answer.
- **Reusable Template**: Cleanly structured so anyone looking to build a custom vocabulary or study quiz on a NumWorks calculator can fork and extend the word bank directly.

---

## 📜 Other Quizzes

### `german_quiz.py` *(Created June 04, 2023)*
- An early vocabulary quiz prototype containing only **10 German words**. Served as the structural mockup adapted for the English irregular verbs quiz.

### `date_quiz.py` *(Created January 10, 2024)*
- Guess the exact day of the week for any random date between **year 0 and 2100**.
- Powered by the Zeller's congruence date logic developed in **[Time-Tools (`zeller.py` / `date.py`)](https://github.com/maelangallais/Time-Tools)**.

### Mental Math Drills (`mental_math/`)
Simple, quick-fire console drills for mental arithmetic practice:
- **`square_quiz.py`** *(Created May 05, 2023)* : Squares of numbers from `0` to `15`.
- **`square_root_quiz.py`** *(Created May 05, 2023)* : Square roots of values from `15` to `100`.
- **`cube_quiz.py`** *(Created September 12, 2023)* : Cubes of numbers from `10` to `100`.
- **`cube_root_quiz.py`** *(Created September 12, 2023)* : Cube roots of values from `10` to `100`.

---

## 🖥️ Requirements & Platform

- MicroPython for **NumWorks** calculators (`random`, `math`, `time`).
