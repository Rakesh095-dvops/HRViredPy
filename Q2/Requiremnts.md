# Python Exercise

## Question 2

Q2. As a DevOps engineer, it is crucial to monitor the health and performance of servers. Write a Python program to monitor the health of the CPU. Few pointers to be noted:

●       The program should continuously monitor the CPU usage of the local machine.

●       If the CPU usage exceeds a predefined threshold (e.g., 80%), an alert message should be displayed.

●       The program should run indefinitely until interrupted.

●       The program should include appropriate error handling to handle exceptions that may arise during the monitoring process.

Hint:

●       The psutil library in Python can be used to retrieve system information, including CPU usage. You can install it using pip install psutil.

●       Use the psutil.cpu_percent() method to get the current CPU usage as a percentage.
```
Expected Output:

Monitoring CPU usage...

Alert! CPU usage exceeds threshold: 85%

Alert! CPU usage exceeds threshold: 90%

... (continues until interrupted) 
```

## Test results-pytest

```


```
## Test results-console 

```

```