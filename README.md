# Password Tool

Small interactive tool to generate, validate, and save passwords.

Files:
- [password_tool.py](password_tool.py) — main script.

Requirements
- Python 3.6+ (most recent Windows installations include a compatible Python).

Quick start
1. Open a terminal in the project folder.

```bash
python password_tool.py
```

Menu options
- Option 1: Generate a single password (choose length and which character categories to include: lowercase, uppercase, digits, symbols). The tool shows strength and can save the password to a TXT file.
- Option 2: Generate multiple passwords at once (choose count, length and categories). Strength for each password is displayed and you can save them to a TXT file.
- Option 3: Validate an existing password you type (returns `Weak`, `Medium` or `Strong`).
- Option 4: Save the last generated passwords from this session to a TXT file.
- Option 5: Exit.

Example flows
- Generate a single password:
  - Choose option 1
  - Enter length (default 12)
  - Choose whether to include lowercase, uppercase, digits and symbols
  - The script prints the generated password and its strength
  - You may save it to a TXT file

- Generate 10 passwords:
  - Choose option 2
  - Enter `10` when asked for how many passwords to generate
  - Set length and character categories
  - The script shows each password and its strength; you can then save them

Notes
- Security: the script uses the `secrets` module for secure random generation (preferred over `random` for password generation).
- Symbols: `string.punctuation` is used by default; some target systems may reject certain punctuation characters. If needed, edit [password_tool.py](password_tool.py) to adjust/whitelist symbols.
- Strength: the strength check is heuristic (based on length and category variety). For more accurate strength scoring consider integrating a library like `zxcvbn`.
- Files: saved password files are named `passwords_YYYYMMDD_HHMMSS.txt` and are written to the current directory.

Suggested improvements
- Integrate `zxcvbn` for more accurate password strength evaluation.
- Add an option to copy generated passwords to the clipboard instead of printing them.
- Export generated passwords in CSV/JSON with metadata (length, strength).

Want me to add any of these now (for example, `zxcvbn` integration or symbol filtering)?
