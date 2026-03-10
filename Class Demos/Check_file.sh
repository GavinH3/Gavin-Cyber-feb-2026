#!/bin/bash

if [ -f /etc/passwd ]; then
    echo "The passwd file exists."
else
    echo "Warning! The passwd file is missing."
fi