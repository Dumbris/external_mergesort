#!/bin/sh

#WARNING! sudo required

GROUPNAME=myGroup2
cgcreate -g memory:/$GROUPNAME
echo $(( 2 * 1024 * 1024 )) > /sys/fs/cgroup/memory/$GROUPNAME/memory.limit_in_bytes
echo $(( 2 * 1024 * 1024 )) > /sys/fs/cgroup/memory/$GROUPNAME/memory.memsw.limit_in_bytes