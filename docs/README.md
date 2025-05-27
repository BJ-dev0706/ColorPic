# ColorPic Documentation

## Project Structure

```
ColorPic/
├── src/                    # Source code package
│   ├── __init__.py        # Package initialization
│   ├── config.py          # Configuration settings
│   ├── utils.py           # Utility functions
│   ├── color_picker.py    # Core color picking logic
│   └── ui.py              # User interface components
├── tests/                 # Test package
│   ├── __init__.py        # Test package initialization
│   └── test_utils.py      # Unit tests for utilities
├── docs/                  # Documentation
│   └── README.md          # This file
├── main.py                # Application entry point
├── setup.py               # Package setup configuration
├── requirements.txt       # Python dependencies
├── MANIFEST.in           # Package manifest
├── README.md             # Project README
├── LICENSE               # License file
└── .gitignore            # Git ignore rules
```

## Module Overview

### `src/config.py`
Contains all configuration constants and settings for the application.

### `src/utils.py`
Utility functions for color operations:
- `rgb_to_hex()`: Convert RGB values to hex
- `get_pixel_color()`: Get pixel color at coordinates
- `format_color_display()`: Format color for display

### `src/color_picker.py`
Core ColorPicker class that handles:
- Screen overlay creation
- Color capture from screen
- Color storage and management

### `src/ui.py`
User interface components:
- Main window setup
- UI layout and styling
- Event handling

### `main.py`
Application entry point that initializes and runs the UI.

## Usage

Run the application:
```bash
python main.py
```

Run tests:
```bash
python -m unittest discover tests
```

Install as package:
```bash
pip install -e .
``` 