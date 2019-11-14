import psutil

p = psutil.Process(pid)

print(p.memory_info())
