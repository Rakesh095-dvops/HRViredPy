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
## Testing 
### Iteration 1 
<bold>For testing purpose CPU thresold has been set as 10% </bold> 

```
# Configuration 
CPU_THRESHOLD = 10  # CPU percentage limit (e.g., 80%)
CHECK_INTERVAL = 2  # Time in seconds between CPU checks
```
#### Test results-console 

```
~Q2> python .\cpuMonitor.py
Monitoring CPU usage...
Alert! CPU usage exceeds threshold: 30.1%
Alert! CPU usage exceeds threshold: 13.6%
Alert! CPU usage exceeds threshold: 13.8%
Alert! CPU usage exceeds threshold: 19.8%
Alert! CPU usage exceeds threshold: 16.9%
Alert! CPU usage exceeds threshold: 15.4%
Alert! CPU usage exceeds threshold: 15.2%
Alert! CPU usage exceeds threshold: 11.7%
Alert! CPU usage exceeds threshold: 14.3%
Alert! CPU usage exceeds threshold: 11.2%
Alert! CPU usage exceeds threshold: 13.6%
Alert! CPU usage exceeds threshold: 13.8%
Alert! CPU usage exceeds threshold: 19.8%
Alert! CPU usage exceeds threshold: 16.9%
Alert! CPU usage exceeds threshold: 15.4%
Alert! CPU usage exceeds threshold: 15.2%
Alert! CPU usage exceeds threshold: 11.7%
Alert! CPU usage exceeds threshold: 14.3%
Alert! CPU usage exceeds threshold: 11.2%

Monitoring stopped by user.
```
### Iteration 2
<bold>For testing purpose CPU thresold has been set as 80% </bold> 
```
# Configuration
CPU_THRESHOLD = 80  # CPU percentage limit (e.g., 80%)
```
#### Test results-console 
```
\Q2> python .\cpuMonitor.py
Monitoring CPU usage...

Monitoring stopped by user.
```