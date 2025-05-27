"""
Utility functions for color operations and helper methods.
"""

import pyautogui


def rgb_to_hex(r: int, g: int, b: int) -> str:
    """
    Convert RGB values to hexadecimal color code.
    
    Args:
        r (int): Red value (0-255)
        g (int): Green value (0-255)
        b (int): Blue value (0-255)
    
    Returns:
        str: Hexadecimal color code (e.g., "#ff0000")
    """
    return f"#{r:02x}{g:02x}{b:02x}"


def get_pixel_color(x: int, y: int) -> tuple[int, int, int]:
    """
    Get the RGB color of a pixel at the specified coordinates.
    
    Args:
        x (int): X coordinate
        y (int): Y coordinate
    
    Returns:
        tuple[int, int, int]: RGB values
    """
    screenshot = pyautogui.screenshot()
    return screenshot.getpixel((x, y))


def format_color_display(hex_color: str) -> str:
    """
    Format color for display in the UI.
    
    Args:
        hex_color (str): Hexadecimal color code
    
    Returns:
        str: Formatted display string
    """
    return f"Selected Color: {hex_color}" 