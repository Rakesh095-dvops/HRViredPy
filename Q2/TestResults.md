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