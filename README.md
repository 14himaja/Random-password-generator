# Random Password Generator

## Table of Contents

1. [Project Description](#project-description)  
2. [Features](#features)  
3. [Technologies / Tools Used](#technologies--tools-used)  
4. [Design & Implementation Approaches](#design--implementation-approaches)  
5. [How to Run / Usage](#how-to-run--usage)  
6. [Project Structure](#project-structure)  
7. [output](#output)


---

## Project Description

A Python script to generate random passwords. The script allows users to specify details / constraints, validates inputs, then produces a password satisfying those constraints (e.g., length, combination of uppercase, lowercase, digits, special characters).

---

## Features

- Interactive input (through console) to accept parameters like length, character types etc.  
- Checks / validation of input values (e.g. positive integers, minimum length)  
- Random generation combining different character sets  
- Ensures password has variety (uppercase, lowercase, digits, symbols) if requested  
- (Possibly) error handling for invalid combinations  

---

## Technologies / Tools Used

- **Python** (version whatever you used)  
- Python standard library modules such as `random` and/or `secrets`, `string` etc.  
- No external dependencies (lightweight, simple)  

---

## Design & Implementation Approaches

- **Modular input & validation**: The code likely splits logic between reading user input, verifying constraints, and generating password. This separation ensures clarity and easier maintenance.

- **Use of built-in character sets** (`string.ascii_letters`, `string.digits`, `string.punctuation`) to define allowed characters: makes code concise and reduces errors.

- **Random selection & mixing / shuffling**: After collecting chosen character types, the code shuffles or randomly picks to ensure password is unpredictable.

- **Guarding edge cases**: e.g. if user does not request any special characters, or if length is less than number of mandatory types, handling that gracefully.

---

## How to Run / Usage

```bash
# Clone repo
git clone https://github.com/14himaja/OIBSIP_python_programming_3.git
cd OIBSIP_python_programming_3

# (Optional) setup virtual environment
python3 -m venv venv
source venv/bin/activate    # on Linux / Mac
venv\Scripts\activate       # on Windows

# Run
python password_generator.py

```
## Project Structure
```

OIBSIP_python_programming_3/
├── password_generator.py     # Main script: handles input, validation, and generation
├── README.md                 # Documentation
└── (other supporting files if any)
```
## output
[password_generator.webm](https://github.com/user-attachments/assets/f9f29fcc-3192-45e8-a326-3b886b0cc386)


```

