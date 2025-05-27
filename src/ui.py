"""
User Interface components and layout for ColorPic application.
"""

import customtkinter as ctk
from customtkinter import CTkFont

from .config import *
from .color_picker import ColorPicker


class ColorPickerUI:
    """
    Main UI class for the Color Picker application.
    """
    
    def __init__(self):
        """
        Initialize the UI components.
        """
        self.root = None
        self.color_label = None
        self.color_picker = None
        self._setup_ui()
    
    def _setup_ui(self) -> None:
        """
        Set up the main UI components and layout.
        """
        # Configure customtkinter
        ctk.set_appearance_mode(APPEARANCE_MODE)
        ctk.set_default_color_theme(COLOR_THEME)
        
        # Create main window
        self.root = ctk.CTk()
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.title(WINDOW_TITLE)
        
        # Create header frame
        self._create_header()
        
        # Create main content frame
        self._create_main_content()
        
        # Initialize color picker
        self.color_picker = ColorPicker(self.root, self.color_label)
    
    def _create_header(self) -> None:
        """
        Create the header section with title.
        """
        header_frame = ctk.CTkFrame(master=self.root, corner_radius=CORNER_RADIUS)
        header_frame.pack(pady=HEADER_PADDING_Y, padx=MAIN_PADDING, fill="x")
        
        title_font = CTkFont(
            family=TITLE_FONT_FAMILY,
            size=TITLE_FONT_SIZE,
            weight=TITLE_FONT_WEIGHT
        )
        
        title_label = ctk.CTkLabel(
            master=header_frame,
            text=APP_NAME,
            font=title_font
        )
        title_label.pack(pady=10)
    
    def _create_main_content(self) -> None:
        """
        Create the main content area with buttons and color display.
        """
        main_frame = ctk.CTkFrame(master=self.root, corner_radius=CORNER_RADIUS)
        main_frame.pack(padx=MAIN_PADDING, fill="both", expand=True)
        
        # Pick color button
        screen_pick_button = ctk.CTkButton(
            master=main_frame,
            text=PICK_COLOR_BUTTON_TEXT,
            command=self._pick_color_command,
            corner_radius=8,
            height=BUTTON_HEIGHT
        )
        screen_pick_button.pack(pady=(15, 10))
        
        # Color display label
        self.color_label = ctk.CTkLabel(
            master=main_frame,
            text=DEFAULT_COLOR_TEXT,
            width=200,
            height=40,
            corner_radius=6
        )
        self.color_label.pack(pady=(0, 15))
        
        # Copy color button
        copy_button = ctk.CTkButton(
            master=main_frame,
            text=COPY_COLOR_BUTTON_TEXT,
            command=self._copy_color_command,
            corner_radius=8,
            height=BUTTON_HEIGHT
        )
        copy_button.pack(pady=(0, 20))
    
    def _pick_color_command(self) -> None:
        """
        Command handler for pick color button.
        """
        if self.color_picker:
            self.color_picker.pick_color_from_screen()
    
    def _copy_color_command(self) -> None:
        """
        Command handler for copy color button.
        """
        if self.color_picker:
            self.color_picker.copy_current_color()
    
    def run(self) -> None:
        """
        Start the application main loop.
        """
        if self.root:
            self.root.mainloop() 