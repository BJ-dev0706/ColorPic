# Color Picker

A simple and intuitive Python-based color picker application. This tool allows you to quickly grab any color from your screen and copy it to your clipboard in HEX format. Perfect for designers, developers, or anyone who needs to work with consistent color values.

## Features

- **Pick any color from your screen** by clicking anywhere on your desktop.
- **Live color preview** visible once you pick a color, showing a swatch of the selected color.
- **Simple "Copy Color" button** to copy the selected color's HEX code to your clipboard.
- **CustomTkinter** interface for a modern, clean look.

## Getting Started

### Prerequisites

- **Python 3.6+**  
- **pip** (Python package manager)

### Installation

1. **Clone this repository** or [download the source code](https://github.com/BJ-dev0706/ColorPic/archive/refs/heads/main.zip):

   ```bash
   git clone https://github.com/BJ-dev0706/ColorPic.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd YOUR_REPO
   ```

3. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   > *Note: If you do not have a `requirements.txt` yet, you can install the needed libraries like so:*  
   ```bash
   pip install pyautogui customtkinter
   ```

### Usage

1. Run the application:

   ```bash
   python index.py
   ```

2. Click the **"Pick Color from Screen"** button. A semi-transparent fullscreen overlay will appear.
3. Move your cursor to the pixel you want to sample, then click. The application will display the selected color and provide its HEX code.
4. Click **"Copy Color"** to copy the HEX code to your clipboard for use in design programs, IDEs, or anywhere else.

### About the Code

- **`index.py`**: Contains the main logic, including:
  - `pick_color_from_screen()`: Creates the fullscreen overlay and captures mouse clicks for color selection.
  - `capture_screen_color(event)`: Determines the color from the screen at the clicked point and updates the label.
  - `copy_color()`: Copies the current color value to your clipboard.
- **CustomTkinter**: A modern reimagining of Tkinter for better UI styling and theming.
- **PyAutoGUI**: Used to capture screen pixels for color reading.

## Contributing

1. Fork the project.
2. Create your feature branch:  
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes:  
   ```bash
   git commit -m "Add some AmazingFeature"
   ```
4. Push to the branch:  
   ```bash
   git push origin feature/AmazingFeature
   ```
5. Open a pull request explaining your changes.

## License

This project is open-source and available under the [MIT License](LICENSE). You are free to use, modify, and distribute this project, but please provide attribution back to the original repository.

---

Thank you for checking out **Color Picker**! If you find this project useful, please consider giving a ⭐ on [GitHub](https://github.com/BJ-dev0706/ColorPic). Feel free to open issues or pull requests if you have any questions or improvements.
