#!/bin/bash
lowercase(){
    echo "$1" | sed "y/ABCDEFGHIJKLMNOPQRSTUVWXYZ/abcdefghijklmnopqrstuvwxyz/"
}
OS=`lowercase \`uname\``
echo "$OS"
if [ "$OS" == "msys" ]; then
	echo "Windows"
elif [ "$OS" == "linux" ]; then
	echo "Linux"
fi 

case "$OS" in 
	msys) echo "msys" ;;
esac 

echo "$OSTYPE"
