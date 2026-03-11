#!/bin/bash
# day2_lab.sh
# Count failed login attempts in a log file

log_file="/var/log/auth.log"   # Change to /var/log/auth.log if available
count=0

while IFS= read -r line; do