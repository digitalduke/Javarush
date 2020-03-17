import os
import time
import zipfile

source = [
	'/home/digitalduke/.gitkraken',
	'/home/digitalduke/.bashrc',
]

destination = "/tmp/backup"
target = destination + os.sep + time.strftime('%Y-%m-%d-%H-%M')
comment = raw_input('input comment for this backup (can be empty): ')

if comment:
	target += "-" + comment.replace(" ", "_")

target += '.zip'

if not os.path.exists(destination):
	os.mkdir(destination)

with zipfile.ZipFile(target, 'w') as backup:
	for filename in source:
		backup.write(filename) 
	
	backup_status = backup.testzip()
	if backup_status:
		print "backup filed, problem at:", backup_status
	else:
		print "backup complete"
