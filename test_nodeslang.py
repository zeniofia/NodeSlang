# test_nodeslang.py
"""
Tests for NodeSlang module.
"""

import unittest
from nodeslang import NodeSlang

class TestNodeSlang(unittest.TestCase):
    """Test cases for NodeSlang class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NodeSlang()
        self.assertIsInstance(instance, NodeSlang)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NodeSlang()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
