# array "fivetwelve" represents every possible TTT combination (given 2 possible cell states, X and blank)
# array "nines" has 512 rows by 9 columns

# global variables
count = 0
fivetwelve = ["" for i in range(512)] 
nines = [ [0]*9 for i in range(512)]
 
# Function to print the output
def printTheArray(arr, n):

    s = ""

    for i in range(0, n):
        s = s + str(arr[i])
        #print(s)
    
    print(s)

    global count
    global fivetwelve
    fivetwelve[count] = s    
    count = count + 1
 
# Function to generate all binary strings
def generateAllBinaryStrings(n, arr, i):
 
    if i == n:
        printTheArray(arr, n)
        return
     
    # First assign "0" at ith position
    # and try for all other permutations
    # for remaining positions
    arr[i] = 0
    generateAllBinaryStrings(n, arr, i + 1)
 
    # And then assign "1" at ith position
    # and try for all other permutations
    # for remaining positions
    arr[i] = 1
    generateAllBinaryStrings(n, arr, i + 1)
 
# Driver Code
if __name__ == "__main__":
    count = 0
    
    n = 9
    arr = [None] * n
 
    # Print all binary strings
    generateAllBinaryStrings(n, arr, 0)
    print(count)

    # fivetwelve[196] = "wahoo"

    print("test")
    print(fivetwelve)
    print("test test")
    print(nines)

# This code is contributed
# by Rituraj Jain