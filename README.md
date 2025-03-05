# Python Task Manager

A simple command-line task management application built with Python. This project demonstrates fundamental Python programming concepts including:

- Object-Oriented Programming
- File I/O operations
- JSON data handling
- Command-line interface design
- Basic CRUD operations

## Features

- Add new tasks with title, description, and optional due date
- List all tasks with their details
- Mark tasks as completed
- Delete tasks
- Persistent storage using JSON file
- Simple command-line interface

## How to Run

Simply run the Python script:

```bash
python task_manager.py
```

## Usage

The application provides a menu-driven interface with the following options:

1. Add Task - Create a new task
2. List Tasks - View all tasks
3. Mark Task as Completed - Update task status
4. Delete Task - Remove a task
5. Exit - Close the application

## Learning Points

- Python classes and objects
- Working with JSON files
- Date and time handling
- User input validation
- Data persistence
- Error handling

# Titanic Dataset Analysis

This interactive dashboard analyzes the famous Titanic dataset using Python and Streamlit. It provides various insights and a machine learning model to predict survival probability.

## Features

1. **Dataset Overview**

   - Basic statistics
   - Data preview
   - Feature information

2. **Survival Analysis**

   - Gender distribution
   - Survival rates by gender
   - Interactive visualizations

3. **Age Distribution**

   - Age histogram
   - Age statistics
   - Survival patterns by age

4. **Passenger Class Analysis**

   - Class distribution
   - Survival rates by class
   - Interactive charts

5. **Survival Prediction**
   - Machine learning model
   - Feature importance analysis
   - Interactive prediction tool

## Setup Instructions

1. Download the Titanic dataset from Kaggle:

   - Visit: https://www.kaggle.com/c/titanic/data
   - Download `train.csv` and `test.csv`
   - Place both files in the project directory

2. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run titanic_analysis.py
   ```

## Usage

1. Select different analysis types from the sidebar
2. Interact with visualizations
3. Try the survival prediction tool with custom inputs
4. Explore various aspects of the dataset through interactive charts

## Learning Points

- Data preprocessing
- Exploratory data analysis
- Data visualization
- Machine learning basics
- Interactive dashboard creation
