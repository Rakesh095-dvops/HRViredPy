import psutil,time

# Configuration
CPU_THRESHOLD = 80  # CPU percentage limit (e.g., 80%)
CHECK_INTERVAL = 2  # Time in seconds between CPU checks

def log_cpu_exceeded(cpu_percent):
    print(f"Alert! CPU usage exceeds threshold: {cpu_percent}%")


def main():
    try:
        while True:
            cpu_percent = psutil.cpu_percent(interval=1) # Get CPU usage over 1 second interval
            if cpu_percent > CPU_THRESHOLD:
                log_cpu_exceeded(cpu_percent)
            
            time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")




if __name__ == '__main__':
    #print(psutil.cpu_percent(interval=1, percpu=True))
    print("Monitoring CPU usage...")
    main()
          