#!/bin/bash
rm options.rc
for item in $(cat ./options | awk '{print $2}');do 
echo -e "use $item \n options" >> options.rc
done
