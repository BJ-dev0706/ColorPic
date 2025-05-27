#!/usr/bin/env python3
"""
ColorPic - A professional color picker application.

Main entry point for the application.
"""

from src.ui import ColorPickerUI


def main():
    """
    Main function to start the ColorPic application.
    """
    app = ColorPickerUI()
    app.run()


if __name__ == "__main__":
    main() 