# test_blockmesh.py
"""
Tests for BlockMesh module.
"""

import unittest
from blockmesh import BlockMesh

class TestBlockMesh(unittest.TestCase):
    """Test cases for BlockMesh class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockMesh()
        self.assertIsInstance(instance, BlockMesh)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockMesh()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
