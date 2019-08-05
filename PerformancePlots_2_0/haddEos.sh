#!/bin/bash
Folder=$2
listfile=`eos find $Folder | grep root | grep -v failed`
hadd $1 $listfile
