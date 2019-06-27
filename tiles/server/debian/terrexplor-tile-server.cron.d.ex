#
# Regular cron jobs for the terrexplor-tile-server package
#
0 4	* * *	root	[ -x /usr/bin/terrexplor-tile-server_maintenance ] && /usr/bin/terrexplor-tile-server_maintenance
