import os

totalSize = 0
for filename in os.listdir('/home/ventu/Downloads'):
    totalSize = totalSize + os.path.getsize(os.path.join('/home/ventu/Downloads', filename))

print(totalSize / 1024)