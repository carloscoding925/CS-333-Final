Carlos Hernandez
CS 333 - Final Project

--OVERVIEW--

This project is a simple To-Do List application developed in Python. The main features
include adding/removing tasks, displaying all tasks, and modifying tasks to change
dates, descriptions, and completion status.  

--TESTING--
This project is tested using unittest and each class has a dedicated suite of unit tests 
allocated for it. A file for testing how the task and ToDoList class interact with each 
other has also been included. Within the local development environment, to check how much 
of the code has been tested {coverage} has been installed and is the main tool used to check 
this statistic. Once the code has been pushed to the dedicated Github repository, a github 
workflow .yml page automates the build and testing of the application. Pytest is the tool of 
choice used within the repository to automatically test the application upon push.

--BUILD / DEPLOYMENT--
To build & deploy the application, an additional .yml page has been added to the github
/ workflows folder that links the Github repository to a Dockerhub repository. Upon push,
the application is containerized and published to the linked Dockerhub repository. From 
here, the application can be downloaded from Dockers online website or Docker Desktop.