# Carlos Hernandez
# CS 333, Erin Keith
from task import Task

import unittest

class TestingTaskMethods(unittest.TestCase):

    def test_initialization(self):
        sampleTask = Task()

        self.assertEqual(sampleTask.returnDesc(), "Sample Description", "Descriptions do not match")
        self.assertEqual(sampleTask.returnDate(), "01/01/0001", "Dates do not match")
        self.assertFalse(sampleTask.returnComplete(), "Booleans do not match")

    def test_date_change(self):
        sampleTask = Task()

        sampleTask.changeDate("09/25/2001")

        self.assertEqual(sampleTask.returnDate(), "09/25/2001", "Dates are not equal")

    def test_description_change(self):
        sampleTask = Task()

        sampleTask.changeDescription("Testing")

        self.assertEqual(sampleTask.returnDesc(), "Testing", "Descriptions are not equal")

    def test_setcomplete(self):
        sampleTask = Task()

        sampleTask.setComplete(True)

        self.assertTrue(sampleTask.returnComplete(), "Booleans are not equal")

    def test_taskset(self):
        sampleTask = Task()

        sampleTask.setTask("01/02/0003", "Test Desc", True)

        self.assertEqual(sampleTask.returnDate(), "01/02/0003", "Dates do not match")
        self.assertEqual(sampleTask.returnDesc(), "Test Desc", "Descriptions do not match")
        self.assertTrue(sampleTask.returnComplete(), "Booleans do not match")
    
    def test_taskPrint(self):
        sampleTask = Task()

        self.assertTrue(sampleTask.printTask(), "Task did not print")

        sampleTask.setComplete(True)

        self.assertTrue(sampleTask.printTask(), "Task did not print")