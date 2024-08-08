#!/bin/bash

# Step 1: Remove previous compilation outputs
rm -f ./a.out

# Step 2: Compile the C++ program
/usr/bin/g++ -o a.out walk.cc
if [ $? -ne 0 ]; then
    echo "Failed to compile walk.cc"
    exit 1
fi

# Step 3: Remove previous test outputs
rm -f ./output

# Step 4: Execute the test script and capture the return code
./test.sh
retcode=$?

# Step 5: Print the score based on the test script's return code
echo "Score: $retcode out of 2 correct."

# Step 6: Output the original submission
echo "*************Original Submission*************"
cat walk.cc

