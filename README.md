# ECSE3038 Lab 1

We were required to write this code as a laboratory skills in order to sharpen our skills and in partial fulfillment of the course Engineering IoT (ECSE3038). The aim, requirements and outline of the lab are as below:

## Aim

To become more familiar with Git, GitHub and Python and the development environment.

## Requirements
Students should create a repository on GitHub and push code to this repository. Students should also make changes to the code on their local machine and commit these changes to the repository.

The code that the students are expected to write will not be specific to a particular topic.

## Outline
In the Python programming language, you are expected to design and implement a simple script that performs actions as defined be the requirements below. These actions or functions must be added to your code one after the other separated by a commit to the repository hosted on GitHub. 

Addition of any further functionality is up to you but the following functions must be included:

1. Write a function, `parallel()`, that, when called, outputs the outputs the effective resistance of a network of 2 or more resistors connected in parallel. The function should be able to accept a list of numbers of any length.
    
    eg. 
    
    ```jsx
    > parallel([330, 1000, 2200])
    > "222.973 ohms"
    ```
    
    (5 marks)
    
2. Write a function, `potential_divider()`, that takes two values as argument, a number that represents a voltage supply value and a list of numbers that represent resistance values of resistors connected in series. The function should output the voltage drop across each resistor in your resistor list. The function should be able to accept a list of numbers of any length.
    
    
    ![circuit.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a129ced3-215b-4845-9c90-04db26a64068/circuit.png)
    
    eg. 
    
    ```jsx
    > potential_divider(9, [3000, 1000])
    > "6.75v"
    > "2.25v"
    ```
    
    (5 marks)
    
3. Write a function, `temperature_check()`, that accepts a single number, a patient's body temperature, and a single character, the unit of temperature. The function should output whether the patient is hypothermic, hyperthermic or has normal body temperature based on the number passed to the function. 
    
    The second value passed as argument should tell the function whether the condition should calculated in degrees celcius or degrees fahrenheit.
    
    An appropriate message should be written to the screen with the result. You’re free to use what ever reasonable temperature limits you feel will adequately act as boundaries for these conditions.
    
    eg. 
    
    ```jsx
    > temperature_check(14, "C")
    > "the patient is hypothermic"
    
    > temperature_check(37, "C")
    > "the patient's temperature is normal"
    
    > temperature_check(37, "F")
    > "the patient is hypothermic"
    ```
    
    (5 marks)

## JOKE
Two bytes meet.  The first byte asks, “Are you ill?”
The second byte replies, “No, just feeling a bit off.”


