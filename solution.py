#define a module
def find_missing_char(chars):
    missingChar = ''
    #loop
    for i in range(0,len(chars)-1):
        if(ord(chars[i+1]) - ord(chars[i]) > 1):
            missingChar = chr(ord(chars[i])+1)

    return missingChar
