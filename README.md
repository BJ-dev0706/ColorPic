# ColorPic

A professional Python-based color picker application with a modern, clean interface. This tool allows you to quickly grab any color from your screen and copy it to your clipboard in HEX format. Perfect for designers, developers, or anyone who needs to work with consistent color values.

## Features

- **Pick any color from your screen** by clicking anywhere on your desktop
- **Live color preview** with visual swatch of the selected color
- **One-click copy** to clipboard in HEX format
- **Modern UI** built with CustomTkinter for a professional look
- **Modular architecture** with clean separation of concerns
- **Comprehensive testing** with unit tests included

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
│   └── README.md          # Technical documentation
├── main.py                # Application entry point
├── setup.py               # Package setup configuration
├── requirements.txt       # Python dependencies
├── MANIFEST.in           # Package manifest
├── README.md             # This file
├── LICENSE               # License file
└── .gitignore            # Git ignore rules
```

## Getting Started

### Prerequisites

- **Python 3.8+**  
- **pip** (Python package manager)

### Installation

1. **Clone this repository**:

   ```bash
   git clone https://github.com/BJ-dev0706/ColorPic.git
   cd ColorPic
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Optional: Install as a package**:

   ```bash
   pip install -e .
   ```

### Usage

#### Running the Application

```bash
python main.py
```

#### Using the Color Picker

1. Click **"Pick Color from Screen"** - a semi-transparent overlay appears
2. Move your cursor to any pixel and click to sample the color
3. The selected color appears with its HEX code
4. Click **"Copy Color"** to copy the HEX code to your clipboard

#### Running Tests

```bash
python -m unittest discover tests
```

## Architecture

### Core Components

- **`src/config.py`**: Centralized configuration and constants
- **`src/utils.py`**: Color conversion and utility functions
- **`src/color_picker.py`**: Core color picking logic with overlay management
- **`src/ui.py`**: User interface components and layout
- **`main.py`**: Application entry point

### Key Features

- **Modular Design**: Clean separation between UI, logic, and utilities
- **Configuration Management**: Centralized settings for easy customization
- **Type Hints**: Full type annotation for better code quality
- **Documentation**: Comprehensive docstrings and comments
- **Testing**: Unit tests for critical functionality

## Development

### Setting up Development Environment

```bash
# Clone and setup
git clone https://github.com/BJ-dev0706/ColorPic.git
cd ColorPic

# Install in development mode
pip install -e .

# Run tests
python -m unittest discover tests -v
```

### Code Style

- Follow PEP 8 guidelines
- Use type hints for all functions
- Include docstrings for all classes and methods
- Maintain test coverage for new features

## Contributing

1. Fork the project
2. Create your feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m "Add some AmazingFeature"`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for modern UI
- Uses [PyAutoGUI](https://github.com/asweigart/pyautogui) for screen capture
- Inspired by the need for a simple, professional color picker tool

---

⭐ **Star this repository** if you find it useful! Feel free to open issues or pull requests for improvements.
