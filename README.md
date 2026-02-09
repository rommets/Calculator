# Python Scientific Calculator

This project implements a **graphical scientific calculator** using **Python** and **Tkinter**, supporting both basic arithmetic and advanced mathematical operations. The calculator features a clean GUI, keyboard input support, and a secure expression evaluation mechanism.

---

## Features

- **Graphical User Interface (GUI):** Built with Tkinter for a lightweight and responsive desktop application  
- **Basic Arithmetic Operations:**  
  Addition, subtraction, multiplication, division, parentheses  
- **Scientific Functions:**  
  - Square root (`√`)  
  - Power operations (`x²`, `x^y`)  
  - Trigonometric functions: `sin`, `cos`, `tan`, `cot` (degree-based)  
  - Logarithmic function (`log₁₀`)  
- **Constants Support:**  
  - π (`pi`)  
  - Euler’s number (`e`)  
- **Keyboard Bindings:**  
  Full keyboard input support for numbers, operators, and function shortcuts  
- **Safe Expression Evaluation:**  
  Uses a restricted `eval` environment to prevent unsafe code execution  
- **Error Handling:**  
  Gracefully handles invalid expressions and mathematical errors  
- **Auto Parenthesis Completion:**  
  Automatically closes unbalanced parentheses before evaluation  

---

## Academic Purpose

This project demonstrates practical concepts in:

- **Python GUI programming** using Tkinter  
- **Event-driven programming**  
- **Secure expression evaluation**  
- **Mathematical function handling**  
- **User input validation and error handling**

It is suitable as a **computer workshop**, **introductory software engineering**, or **Python programming** course project.

---

## Usage

1. Make sure Python 3 is installed on your system.
2. Clone the repository or download the source file.
3. Run the application:

```bash
python calculator.py
```

The calculator window will open immediately.

---

## Keyboard Shortcuts

| Key         | Action                |
| ----------- | --------------------- |
| `Enter`     | Evaluate expression   |
| `Backspace` | Delete last character |
| `Esc`       | Clear                 |
| `s`         | `sin(`                |
| `c`         | `cos(`                |
| `t`         | `tan(`                |
| `o`         | `cot(`                |
| `l`         | `Log(`                |

---

## Example

Expression:

```
sin(30) + √(16) + 2^3
```

Output:

```
8.5
```

---

## Implementation Highlights

* **Sanitized Expressions:**
  User-friendly symbols (`√`, `x²`, `x^y`) are internally converted to valid Python expressions.
* **Degree-Based Trigonometry:**
  All trigonometric functions operate in degrees for user convenience.
* **Minimal Dependencies:**
  Uses only Python standard libraries (`tkinter`, `math`).

---

## Future Extensions

* Add calculation history panel
* Support radians/degrees toggle
* Dark mode UI
* Scientific notation and factorial support
