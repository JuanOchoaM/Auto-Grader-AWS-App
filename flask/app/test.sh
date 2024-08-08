#!/bin/bash

# Execute the program and store the output
tmpoutput=$(echo -e "freddy\nsusan" | ./a.out)

# Initialize the number of correct responses
CORRECT=0

# Check if 'freddy' is in the output
if echo "$tmpoutput" | grep -q 'freddy'; then
    let CORRECT=CORRECT+1
fi

# Check if 'susan' is in the output
if echo "$tmpoutput" | grep -q 'susan'; then
    let CORRECT=CORRECT+1
fi

# Print the number of correct responses
echo $CORRECT

