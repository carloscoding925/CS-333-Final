# Carlos Hernandez
# CS 333, Erin Keith
from todoList import ToDoList
from task import Task

import unittest
from unittest import mock

class TestingToDoMethods(unittest.TestCase):

    def test_initialization(self):
        myList = ToDoList()
        emptyDict = {}

        self.assertEqual(myList.returnChecklist(), emptyDict, "Dictionary not empty")
        self.assertEqual(myList.returnCounter(), 0, "Counter not zero")

    def test_add_and_remove_Task(self):
        myList = ToDoList()
        sampleTask = Task()

        myList.addTask(sampleTask)

        self.assertEqual(myList.returnCounter(), 1, "Task not added")

        myList.removeTask(1)

        self.assertEqual(myList.returnCounter(), 0, "Task not removed")

    def test_print_all(self):
        myList = ToDoList()
        sampleTask = Task()

        myList.addTask(sampleTask)

        self.assertTrue(myList.printAllTasks(), "Tasks did not print")

    def test_specific_task(self):
        myList = ToDoList()
        sampleTask = Task()

        myList.addTask(sampleTask)

        self.assertTrue(myList.printSpecificTask(1), "Task index not accessed") 
        self.assertFalse(myList.printSpecificTask(2), "Out of bounds index accessed")

    @mock.patch('todoList.input', create=True)
    def test_modifyTask(self, mockedInput):
        myList = ToDoList()
        sampleTask = Task()

        myList.addTask(sampleTask)

        mockedInput.side_effect = ["1", "09/25/2001"]
        self.assertTrue(myList.modifyTask("1"), "Task modify menu not prompted")

        mockedInput.side_effect = ["2", "New Desc"]
        self.assertTrue(myList.modifyTask("1"), "Description not modified")

        mockedInput.side_effect = ["3", "T"]
        self.assertTrue(myList.modifyTask("1"), "Boolean not modified")

        mockedInput.side_effect = ["3", "F"]
        self.assertTrue(myList.modifyTask("1"), "Boolean changed")