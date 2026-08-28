# test_crestprime.py
"""
Tests for CrestPrime module.
"""

import unittest
from crestprime import CrestPrime

class TestCrestPrime(unittest.TestCase):
    """Test cases for CrestPrime class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CrestPrime()
        self.assertIsInstance(instance, CrestPrime)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CrestPrime()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
