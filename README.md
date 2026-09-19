# MASA LexiMetrics

A real-time lexical analytics engine computing character densities, whitespace distributions, word counts, and line occurrences.

## Technical Architecture

The codebase follows modular software engineering patterns and OOP structure, designed for reliability, high maintainability, and clean separation of concerns:

- **Component Layering**: User interface and computational state are decoupled into specialized controllers and event loops.
- **Defensive Engineering**: Comprehensive validation guards protect against malformed inputs and runtime exceptions.
- **Modern Design Tokens**: Designed with a high-contrast dark aesthetic adhering to modern developer tooling visual standards.

## Features

- Event-driven lexical parsing executing on each keyboard release event.
- Four distinct statistical metrics: Total Characters, Non-Whitespace Characters, Word Count, and Line Count.
- Text transformation operations for uppercase and lowercase batch conversion.
- Full clipboard buffer clearance and reset utilities.

## Prerequisites

- Python 3.10 or higher
- Required packages:

```bash
pip install customtkinter
```

## Execution

Initialize and run the module via the command line:

```bash
python "Simple Character Counter App using Tkinter in Python/index.py"
```

## Project Structure

```
.
├── Simple Character Counter App using Tkinter in Python
├── LICENSE             # MIT License
└── README.md           # Developer documentation
```

## License

This project is licensed under the terms of the MIT License. Refer to the `LICENSE` file for details.
