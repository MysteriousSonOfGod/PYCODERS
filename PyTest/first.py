#Pytest is a testing framework based on python. It is mainly used to write API test cases
# Pytest is a python based testing framework, which is used to write and execute test codes. In the present days of REST services, pytest is mainly used for API testing even though we can use pytest to write simple to complex tests, i.e., we can write codes to test API, database, UI, etc.
#
# Advantages of Pytest
# The advantages of Pytest are as follows −
#
# Pytest can run multiple tests in parallel, which reduces the execution time of the test suite.
#
# Pytest has its own way to detect the test file and test functions automatically, if not mentioned explicitly.
#
# Pytest allows us to skip a subset of the tests during execution.
#
# Pytest allows us to run a subset of the entire test suite.
#
# Pytest is free and open source.
#
# Because of its simple syntax, pytest is very easy to start with.
#
# In this tutorial, we will explain the pytest fundamentals with sample programs.Pytest is a python based testing framework, which is used to write and execute test codes. In the present days of REST services, pytest is mainly used for API testing even though we can use pytest to write simple to complex tests, i.e., we can write codes to test API, database, UI, etc.
#
# Advantages of Pytest
# The advantages of Pytest are as follows −
#
# Pytest can run multiple tests in parallel, which reduces the execution time of the test suite.
#
# Pytest has its own way to detect the test file and test functions automatically, if not mentioned explicitly.
#
# Pytest allows us to skip a subset of the tests during execution.
#
# Pytest allows us to run a subset of the entire test suite.
#
# Pytest is free and open source.
#
# Because of its simple syntax, pytest is very easy to start with.
#
# In this tutorial, we will explain the pytest fundamentals with sample programs
# now, we will start with our first pytest program. We will first create a directory and thereby, create our test files in the directory.
#
# Let us follow the steps shown below −
#
# Create a new directory named automation and navigate into the directory in your command line.
#
# Create a file named test_square.py and add the below code to that file.

import math
import os

def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

def testsquare():
   num = 7
   assert 7*7 == 49

def tesequality():
   assert 10 == 11


print("_________----------------------- The v increases the verbosity -----------------------___________")
