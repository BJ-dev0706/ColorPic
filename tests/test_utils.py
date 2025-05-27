"""
Unit tests for utility functions.
"""

import unittest
from src.utils import rgb_to_hex, format_color_display


class TestUtils(unittest.TestCase):
    """
    Test cases for utility functions.
    """
    
    def test_rgb_to_hex(self):
        """Test RGB to hex conversion."""
        # Test basic colors
        self.assertEqual(rgb_to_hex(255, 0, 0), "#ff0000")  # Red
        self.assertEqual(rgb_to_hex(0, 255, 0), "#00ff00")  # Green
        self.assertEqual(rgb_to_hex(0, 0, 255), "#0000ff")  # Blue
        self.assertEqual(rgb_to_hex(255, 255, 255), "#ffffff")  # White
        self.assertEqual(rgb_to_hex(0, 0, 0), "#000000")  # Black
        
        # Test mixed colors
        self.assertEqual(rgb_to_hex(128, 128, 128), "#808080")  # Gray
        self.assertEqual(rgb_to_hex(255, 165, 0), "#ffa500")  # Orange
    
    def test_format_color_display(self):
        """Test color display formatting."""
        test_color = "#ff0000"
        expected = "Selected Color: #ff0000"
        self.assertEqual(format_color_display(test_color), expected)
        
        test_color = "#00ff00"
        expected = "Selected Color: #00ff00"
        self.assertEqual(format_color_display(test_color), expected)


if __name__ == "__main__":
    unittest.main() 