import unittest
from unittest.mock import patch
from Framework import main


class TestModemon(unittest.TestCase):

    @patch('Framework.main.switch_monitor_mode')  # Patch the function in main.py
    def test_modemon(self, mock_switch_monitor_mode):
        # Call the function to be tested
        main.modemon()

        # Assert that the function in app.py calls the function in monitor.py
        mock_switch_monitor_mode.assert_called_once()


if __name__ == '__main__':
    unittest.main()
