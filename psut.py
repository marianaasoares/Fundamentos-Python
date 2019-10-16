import psutil

print(psutil.disk_usage('/'))
for p in psutil.process_iter():
    try:
        print(p.username())
    except psutil.AccessDenied:
        pass
    try:
        print(p.cpu_affinity())
    except psutil.AccessDenied:
        pass
    print(p.pid, p.name(), p.memory_info().rss, p.memory_info().vms, p.status())