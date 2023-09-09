#!/bin/bash

CURRDIR=$PWD

if [ "$1" == "uninstall" ]
then
    echo "Removing collection..."
    rm -rfv ~/.ansible/collections/ansible_collections/andrewdomain
    exit 0
fi

cd `dirname -- ${BASH_SOURCE[0]}`
ansible-galaxy collection build andrewdomain/custom_modules/ --force
ansible-galaxy collection install andrewdomain/custom_modules/ --force
cd $CURRDIR
