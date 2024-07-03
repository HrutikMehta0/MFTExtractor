import psutil

# List all disk partitions
partitions = psutil.disk_partitions()
for partition in partitions:
    print(partition.device, partition.mountpoint, partition.fstype, partition.opts)

# Get disk usage statistics
for partition in partitions:
    usage = psutil.disk_usage(partition.mountpoint)
    print(f"Disk {partition.device} - Total: {usage.total}, Used: {usage.used}, Free: {usage.free}, Percentage: {usage.percent}%")
