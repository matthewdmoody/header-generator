# LinkedIn Header Code Renderer

A minimalist Python script that turns its own source code into a LinkedIn-ready header image.

## What It Does

* Reads the script's `__file__`
* Draws code onto a 1584×396 dark canvas (LinkedIn's recommended header size)
* Uses lightweight syntax highlighting
* Outputs a clean header image


## Usage

```bash
python header.py
```

The script generates:

```
linkedin_header.png
```

## Requirements

* Python 3
* Pillow (`pip install pillow`)
* A monospace font available on your system (e.g., Consolas)

## Output Example

<img width="1584" height="396" alt="linkedin_header" src="https://github.com/user-attachments/assets/27f3a791-5136-4bb2-8789-375da306bb8e" />


## Notes

Any resemblance to robust code is accidental. Its true purpose is fitting neatly into a banner, not avoiding errors.

---

For the full project and source code, see the Python file in this repository.
