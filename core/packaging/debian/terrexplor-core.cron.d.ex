#
# Regular cron jobs for the terrexplor-core package
#
0 4	* * *	root	[ -x /usr/bin/terrexplor-core_maintenance ] && /usr/bin/terrexplor-core_maintenance
