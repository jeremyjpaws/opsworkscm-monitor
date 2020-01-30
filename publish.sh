#!/bin/bash -xe
rm code.zip 
cd src
zip -r ../code.zip .
cd ..
aws lambda update-function-code --function-name MonitorOWPE --zip-file fileb://code.zip
