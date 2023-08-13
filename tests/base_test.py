#!/usr/bin/python3
"""Unit test for base model"""
import json
import datetime
import unittest
import models
import sys
from models.base_model import BaseModel

class BaseModelTest(unittest.TestCase):
	"""Class for base model test case"""
    def base_model_test(self):
        self.assertTrue(hasattr(BaseModel, '__init__'),
                    "BaseModel class does not exist")

if __name__ == "__main__":
	unittest.main()
