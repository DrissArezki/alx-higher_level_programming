#!/bin/bash
#This script send a request to a URL and displays the size bytes of the response body
curl -s "$1" | wc -c
