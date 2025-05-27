"""
Core ColorPicker class for handling color picking functionality.
"""

import customtkinter as ctk
from typing import Optional

from .config import *
from .utils import get_pixel_color, rgb_to_hex, format_color_display


class ColorPicker:
    """
    Core color picker functionality handler.
    """
    
    def __init__(self, parent_window: ctk.CTk, color_label: ctk.CTkLabel):
        """
        Initialize the ColorPicker.
        
        Args:
            parent_window (ctk.CTk): The main application window
            color_label (ctk.CTkLabel): The label to display selected color
        """
        self.parent_window = parent_window
        self.color_label = color_label
        self.overlay_window: Optional[ctk.CTkToplevel] = None
        self.current_color: str = ""
    
    def pick_color_from_screen(self) -> None:
        """
        Start the color picking process by creating an overlay window.
        """
        self.overlay_window = ctk.CTkToplevel(self.parent_window)
        
        # Configure overlay window
        self.overlay_window.overrideredirect(True)
        self.overlay_window.attributes('-topmost', True)
        
        # Set fullscreen
        screen_width = self.parent_window.winfo_screenwidth()
        screen_height = self.parent_window.winfo_screenheight()
        self.overlay_window.geometry(f"{screen_width}x{screen_height}+0+0")
        
        # Configure appearance
        self.overlay_window.configure(fg_color=OVERLAY_COLOR)
        self.overlay_window.attributes('-alpha', OVERLAY_ALPHA)
        self.overlay_window.configure(cursor="crosshair")
        
        # Bind click event
        self.overlay_window.bind("<Button-1>", self._capture_screen_color)
    
    def _capture_screen_color(self, event) -> None:
        """
        Capture the color at the clicked position.
        
        Args:
            event: The click event containing coordinates
        """
        x, y = event.x_root, event.y_root
        
        # Get pixel color
        r, g, b = get_pixel_color(x, y)
        hex_color = rgb_to_hex(r, g, b)
        
        # Store current color
        self.current_color = hex_color
        
        # Update UI
        display_text = format_color_display(hex_color)
        self.color_label.configure(text=display_text, fg_color=hex_color)
        
        # Clean up overlay
        self._close_overlay()
    
    def _close_overlay(self) -> None:
        """
        Close and clean up the overlay window.
        """
        if self.overlay_window:
            self.overlay_window.destroy()
            self.overlay_window = None
    
    def copy_current_color(self) -> None:
        """
        Copy the current color to clipboard.
        """
        if self.current_color:
            self.parent_window.clipboard_clear()
            self.parent_window.clipboard_append(self.current_color)
    
    def get_current_color(self) -> str:
        """
        Get the currently selected color.
        
        Returns:
            str: The current color in hex format
        """
        return self.current_color 