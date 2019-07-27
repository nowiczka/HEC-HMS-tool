:'
With the pushd command, HEC-HMS directory is added to the list. Therefore, the hms.py is launched. 
The popd command removes entries from the list and return to the previous path. 
The last code line #!/bin/bash indicates the system which program to use to run the file. 
'
pushd /home/nowiczka/hec-hms-40
./HEC-HMS.sh -s /home/nowiczka/hms.py
popd
#!/bin/bash
