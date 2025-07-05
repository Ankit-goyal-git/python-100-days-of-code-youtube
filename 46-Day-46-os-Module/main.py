# import os

# if(not os.path.exists("data")):
#     os.mkdir("data")

# for i in range(0, 100):
#     os.mkdir(f"data/Day{i+1}")
    
# import os

# # Run the "ls" command and print the output
# output = os.system("ls")
# print(output)  # Output: ['myfile.txt', 'otherfile.txt']


import os

# Run the "ls" command and get the output as a file-like object
f = os.popen("ls")

# Read the contents of the output
output = f.read()
print(output)  # Output: ['myfile.txt', 'otherfile.txt']

# Close the file-like object
f.close()