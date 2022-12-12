# Exam 3

## Rules of Behavior
1. Do not communicate with anyone during the exam (no email, no social media, no Discord, no texting, no phones, no talking, no passing notes, no internet communicating).  If there is any evidence of communicating with anyone during the exam you will receive a zero.
1. You **must** turn off your cell phone and store it away.
1. Your submission **must** be solely you own work without the assistance of anyone by any means.
1. All programming code **must** be written in Python.
1. You **must** use Tuffix to unit test your program.
1. All your code **must** be pushed to Github by the scheduled end of class today.  Any submissions after that time will not be considered.
1. You may use your book.
1. You may use the Internet as a **reference only**.
1. If you have questions, approach the instructor desk.
     
## Program Instructions
1. Write several Python classes that perform as a Tuffy Titan Vehicle management module.  You are provided a very simple main.py file that you may use as you are developing your class hierarchies.
1. The class hierarchies should use the following structure:

<p align="center">
  <img src="./exam03a_graphics.png" width="600" title="Hierarchy Diagram">
</p>

1. Create a `vehicle` module to meet the following requirements:
     1. Create a file named `vehicle.py`.
          1. Define a class named `Vehicle`.
               1. Define a class variable (shared by all instances) named `wheel_type` and initialized to the string `Tires`.   
               1. Define a member function named `__init__` to meet the following requirements:
                    1. Take a `self` object as a positional parameter.
                    1. Take a `color` string as a keyword parameter.
                    1. Take a `engine_type` string as a keyword parameter.
                    1. Define a `self.color` instance variable initialized to the `color` parameter.
                    1. Define a `self.engine_type` instance variable initialized to the `engine_type` parameter.
                    1. Define a `self.towing_capacity` instance variable initialized to the integer `0`.

          1. Define a class named `Car` which inherits from the `Vehicle` class.
               1. Define a class variable (shared by all instances) named `vehicle_classification` and initialized to the string `Car`.   
               1. Define a member function named `__init__` to meet the following requirements:
                    1. Take a `self` object as a positional parameter.
                    1. Take a `color` string as a keyword parameter.
                    1. Take a `engine_type` string as a keyword parameter.
                    1. Take a `passengers` integer as a keyword parameter.
                    1. Call the parent class initialization function and pass the `color` and `engine_type` parameters.
                    1. Define a `self.passengers` instance variable initialized to the `passengers` parameter.

          1. Define a class named `Truck` which inherits from the `Vehicle` class.
               1. Define a class variable (shared by all instances) named `vehicle_classification` and initialized to the string `Truck`.   
               1. Define a member function named `__init__` to meet the following requirements:
                    1. Take a `self` object as a positional parameter.
                    1. Take a `color` string as a keyword parameter.
                    1. Take a `engine_type` string as a keyword parameter.
                    1. Take a `passengers` integer as a keyword parameter.
                    1. Call the parent class initialization function and pass the `color` and `engine_type` parameters.
                    1. Define a `self.passengers` instance variable initialized to the `passengers` parameter.

          1. Define a class named `Sedan` which inherits from the `Car` class.
               1. Define a class variable (shared by all instances) named `vehicle_type` and initialized to the string `Sedan`.   
               1. Define a class variable (shared by all instances) named `doors` and initialized to the integer `4`.   

          1. Define a class named `Coupe` which inherits from the `Car` class.
               1. Define a class variable (shared by all instances) named `vehicle_type` and initialized to the string `Coupe`.   
               1. Define a class variable (shared by all instances) named `doors` and initialized to the integer `2`.   

          1. Define a class named `Pickup` which inherits from the `Truck` class.
               1. Define a class variable (shared by all instances) named `vehicle_type` and initialized to the string `Pickup`.   
               1. Define a class variable (shared by all instances) named `doors` and initialized to the integer `2`.   

          1. Define a class named `SUV` which inherits from the `Truck` class.
               1. Define a class variable (shared by all instances) named `vehicle_type` and initialized to the string `SUV`.   
               1. Define a class variable (shared by all instances) named `doors` and initialized to the integer `5`.   


1. OPTIONAL: Run the main.py file as you are developing your model and classes.

    ```
    python3 -m main
    ```

1. Run the unit testing program to ensure that your program runs as expected.

    ```
    . python3 test.sh
    ```
       
    The unit testing will output the results of a series of tests using specific input and expected output.  Any error will provide information on where the expected output is different from the actual output.  You will need to edit your source code to fix the error and run `./test.sh` repeatedly until it passes all the test.

## Submission
Periodically throughout the exercise, and when you have completed the exercise, **submit the complete repository to Github**.

   <pre>git add .<br>git commit -m "<i>your comment</i>"<br>git push</pre>

In case it asks you  to configure global variables for an email and name, just copy the commands it provides then replace the dummy text with your email and Github token.

   <pre>git config --global user.email "<i>tuffy@csu.fullerton.edu</i>"<br>git config --global user.name "<i>Tuffy Titan</i>"<br>git commit -m "<i>your comment</i>"<br>git push</pre>

When you completed the final Github push, go back into github.com through the browser interface and ensure all your files have been correctly updated.  You should have the following files:
```
vehicle.py
test.txt
```
    
## Grading
1. All points add up to a total of 100 points possible as detailed below.  Partial credit will be given where applicable.

| Points | Description |
| --- | --- |
|45|initial git clone of this repository to your Tuffix machine|
|5|vehicle.py file submitted and meets the program requirements |
|5|unit test passes Test01_vehicle_instance_object|
|5|unit test passes Test02_vehicle_class_variable|
|5|unit test passes Test03_car_instance_object|
|5|unit test passes Test04_car_class_variable|
|5|unit test passes Test05_truck_instance_object|
|5|unit test passes Test06_truck_class_variable|
|5|unit test passes Test07_sedan|
|5|unit test passes Test08_coupe|
|5|unit test passes Test09_pickup|
|5|unit test passes Test10_suv|

