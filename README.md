# IT 2750 - Scripting Fundamentals for Cybersecurity
## Lab 3 - Generating Passwords Using Control Structures and Functions

### 🗒  Description
This repository contains the Python script for Lab 3 of the course IT 2750 - Scripting Fundamentals for Cybersecurity. There are three problems in this lab.

This lab comprises three interconnected problems designed to enhance Python scripting skills, particularly in the context of cybersecurity. The first problem involves creating a Python program to generate custom character sets based on user-defined preferences for uppercase, lowercase, and numeric characters. The second problem extends this concept, guiding students to write a script that generates random strings of a user-specified length, using a character set of uppercase and lowercase letters and digits. The final and most comprehensive problem tasks students with developing a Python function named `generatePassword`. This function generates passwords according to user-defined criteria, including length and character types. By completing this lab, students gain practical experience in scripting for cybersecurity applications, specifically in generating secure passwords through interactive user input and control structures.

#### Problem 1 - Generating Character Sets with Control Structures
Problem 1 focuses on creating a Python program that generates custom character sets based on user preferences. In this lab, students are tasked with designing a script that interactively asks the user for input regarding the inclusion of uppercase, lowercase, and numeric characters in the character set. The user's responses to these questions are stored in variables, and based on their choices, the program constructs a character set containing the selected character types.

#### Problem 2 - Building Random Strings with Control Structures
Problem 2 introduces students to Python programming for generating random strings of characters. In this lab, students are guided to create a Python script that interacts with the user to determine the desired length of the random string to be generated. After obtaining the user's input, the script constructs a character set containing uppercase letters, lowercase letters, and digits. Subsequently, it generates a random string of the specified length using characters from this set and displays the result on the screen.

#### Problem 3 - Generating Random Passwords
Problem 3 builds upon the concepts introduced in the previous problems. In this lab, students are tasked with creating a Python function called generatePassword that generates passwords based on user preferences. The function takes parameters for length, uppercase, lowercase, and numeric characters and returns a password that matches these criteria. Students are required to implement a loop or alternative approach to construct passwords of the specified length using the chosen character sets. The main part of the lab involves interacting with the user to gather input regarding password length and character preferences and then calling the generatePassword function to display the generated password. This exercise reinforces scripting skills and encourages students to create a practical tool for generating secure passwords, which is crucial for cybersecurity applications.

### 📝  Requirements
This lab requires you to write code that adheres to the following requirements:

#### Problem 1
In Problem 1, you will edit the script template to perform the following tasks:

- Part A: Asks the user if they want to include uppercase, lowercase, and numeric characters as part of the output character set. The user's responses are saved into the respective variables `uppercase_response`, `lowercase_response`, and `numeric_response`.
- Part B: Based on the user's choices in Part A, the script generates a character set named `chars` containing characters from the `string.ascii_` constants and prints the content of `chars` to the screen.

#### Problem 2
In Problem 2, you will edit the script template to perform the following tasks:

- Part A: Asks the user how many characters they would like to generate and saves the response in a variable called `length_response`.
- Part B: Creates a variable called `chars` containing a concatenation of `ascii_uppercase`, `ascii_lowercase`, and `digits` from the string constants. It then outputs the content of `chars` to the screen.
- Part C: Creates a loop that generates a new string of length `length_response` by randomly selecting characters from the `chars` variable and outputs the value of the new string to the screen.

#### Problem 3
In Problem 3, you will edit the script template to perform the following tasks:

- Part A: Creates a new function `generatePassword(length, uppercase, lowercase, numeric)` to generate a password of a given length using the user's choice of uppercase, lowercase, and numeric characters.
- Part B: Asks the user how long they want their password to be and whether they want to include uppercase, lowercase, and numeric characters. The script then uses the `generatePassword` function to generate and display the resulting password based on the user's preferences.

#### Additional Requirements
In order to receive credit for this lab, you must replace `YOUR_NAME_HERE` with your name and `YOUR_EMAIL_HERE` with your Tri-C email address in the code file headers for all script files in the template. Students who do not perform this action will receive a zero score.

### 🚀  Usage
To run the script, execute the script file with Python. Each part of the lab problem is commented, and you should replace the placeholder text with your own information. From the code directory of this lab, you can run the various problems using the following commands:

- Problem 1: `python lab3_problem1.py`
- Problem 2: `python lab3_problem2.py`
- Problem 3: `python lab3_problem3.py`

### 🎯  Testing
The problems in this lab are tested using code that can be found in the corresponding `tests_*.py` file for each problem. You can use these tests to check if your code runs properly and to specifications. You can run these tests on your local machine by setting your working directory to the problem folder and running `pytest` with the `tests_*.py` file for the problem. From the code directory of this lab, you can run tests using the following commands:

- Problem 1: `pytest tests_lab3_problem1.py`
- Problem 2: `pytest tests_lab3_problem2.py`
- Problem 3: `pytest tests_lab3_problem3.py`

### 🏆  Grading
This lab is worth 40 points in total using the following breakdown by problem:

- Problem 1 is worth 10 points
- Problem 2 is worth 10 points
- Problem 3 is worth 20 points

You are awarded these points if all assertions in the test file pass successfully for a problem. There is no partial credit for lab problems.

### 💻  Academic Integrity and Copyright
This lab was created by the course professor (Matthew Crowley) and he asserts copyright over all material. You are not permitted to share the labs, tests, or solutions with anyone without express written consent. Breaches of this assertion may result in both academic and legal sanctions.