#!/bin/bash
wget https://iotanalytics.unsw.edu.au/iottestbed/pcap/filelist.txt -O filelist.txt --no-check-certificate
cat filelist.txt | egrep -v "(^#.*|^$)" | xargs -n 2 wget --no-check-certificate
