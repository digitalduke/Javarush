#!/bin/bash
red=`tput setab 1 && tput setaf 4`
green=`tput setab 2 && tput setaf 4`
reset=`tput sgr0`
echo "${red}red text ${green}green text${reset} normal text" 
