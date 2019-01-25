import os
import time

source = [
	'/home/digitalduke/.gitkraken',
	'/home/digitalduke/.bashrc',
]

destination = "/tmp/backup"

target = destination + os.sep + time.strftime('%Y-%m-%d-%H-%M') + '.zip'

backup_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if not os.path.exists(destination):
	os.mkdir(destination)

if os.system(backup_command) == 0:
	print "backup complete in:", target
else:
	print "backup failed."
