# test_identityverifier.py
"""
Tests for IdentityVerifier module.
"""

import unittest
from identityverifier import IdentityVerifier

class TestIdentityVerifier(unittest.TestCase):
    """Test cases for IdentityVerifier class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = IdentityVerifier()
        self.assertIsInstance(instance, IdentityVerifier)
        
    def test_run_method(self):
        """Test the run method."""
        instance = IdentityVerifier()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
