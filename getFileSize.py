import os

totalSize = 0
for filename in os.listdir('/home/username/Downloads'):
    totalSize = totalSize + os.path.getsize(os.path.join('/home/user/', filename))

print(totalSize / 1024)
