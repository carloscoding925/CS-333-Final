# Carlos Hernandez
# CS 333, Erin Keith

from todoList import ToDoList
from task import Task

import unittest
from unittest import mock

class TestingIntegratedMethods(unittest.TestCase):

    @mock.patch('todoList.input', create=True)
    def test_modify_date(self, mockedInput):
        myList = ToDoList()
        sampleTask = Task()

        myList.addTask(sampleTask)

        mockedInput.side_effect = ["1", "02/12/2024"]
        self.assertTrue(myList.modifyTask("1"), "Task modify menu not prompted")

        newTask = myList.returnTask()
        sampleTask.changeDate("02/12/2024")

        self.assertEqual(newTask.returnDate(), sampleTask.returnDate(), "Date not changed")

    @mock.patch('todoList.input', create=True)
    def test_modify_desc(self, mockedInput):
        myList = ToDoList()
        sampleTask = Task()

        myList.addTask(sampleTask)

        mockedInput.side_effect = ["2", "New Description"]
        self.assertTrue(myList.modifyTask("1"), "Task modify menu not prompted")

        newTask = myList.returnTask()
        sampleTask.changeDescription("New Description")

        self.assertEqual(newTask.returnDesc(), sampleTask.returnDesc(), "Description not changed")

    @mock.patch('todoList.input', create=True)
    def test_modify_completion(self, mockedInput):
        myList = ToDoList()
        sampleTask = Task()

        myList.addTask(sampleTask)

        mockedInput.side_effect = ["3", "T"]
        self.assertTrue(myList.modifyTask("1"), "Task modify menu not prompted")

        newTask = myList.returnTask()
        sampleTask.setComplete(True)

        self.assertEqual(newTask.returnComplete(), sampleTask.returnComplete(), "Boolean not updated")

    def test_print_all(self):
        myList = ToDoList()
        sampleTask = Task()

        for x in range(5):
            myList.addTask(sampleTask)

        self.assertTrue(myList.printAllTasks())

    @mock.patch('todoList.input', create=True)
    def test_print_specific(self, mockedInput):
        myList = ToDoList()
        sampleTaskOne = Task()
        sampleTaskTwo = Task()
        sampleTaskThree = Task()

        sampleTaskOne.setTask("09/25/2001", "Born", True)
        sampleTaskTwo.setTask("06/01/2019", "Graduated", True)
        sampleTaskThree.setTask("12/15/2025", "Graduated Uni", False)

        myList.addTask(sampleTaskOne)
        myList.addTask(sampleTaskTwo)
        myList.addTask(sampleTaskThree)

        self.assertTrue(myList.printSpecificTask(1), "Task not printed")
        self.assertTrue(myList.printSpecificTask(2), "Task not printed")
        self.assertTrue(myList.printSpecificTask(3), "Task not printed")
        self.assertFalse(myList.printSpecificTask(4), "Out of bounds index accessed")