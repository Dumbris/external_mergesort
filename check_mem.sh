#!/bin/sh

ps aux | grep external_sort | awk '{sum=sum+$6}; END {print sum/1024 " MB"}'