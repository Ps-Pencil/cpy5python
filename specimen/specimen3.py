# To determine the longest line of the record
MaxLineLength = 0
infile = open("COUNTRIES.txt","r")
line = infile.readline()
while line:
    length = len(line)
    if line[-1] == '\n':
        length -= 1
    if length > MaxLineLength:
        MaxLineLength = length
    line = infile.readline()
infile.close()
# Hash Key
def HashKey(ThisCountry):
    result = 0
    for char in ThisCountry:
        result += ord(char)
    result %= 373
    return result + 1

def CreateCountry():
    infile = open("COUNTRIES.txt",'r')
    #empty the file
    open("NEWFILE","w").close()
    
    outfile = open("NEWFILE",'r+b')
    first = infile.readline()
    
    # Loop over each record
    while first:
        
        # Delete the line breaks
        if first[-1] == '\n':
            first = first[:-1]
        
        key = HashKey(first.split(' ')[0])
        outfile.seek( (key - 1) * MaxLineLength)
        
        # Check whether the cell is already taken
        char = outfile.read(1)
        while char != b'' and char != b'\x00':
            
            # Align the file cursor
            if outfile.tell() % MaxLineLength == 1:
                outfile.seek(outfile.tell() - 1)
            elif outfile.tell() % MaxLineLength == MaxLineLength - 1:
                outfile.seek(outfile.tell() + 1)
            
            # If it is already taken, move the cursor to the next cell
            outfile.seek(outfile.tell() + MaxLineLength)
            
            # If it reaches maximum number, move to the start
            if outfile.tell() == 373 * MaxLineLength:
                outfile.seek(0)
            char = outfile.read(1)
        
        # Align
        if outfile.tell() % MaxLineLength == 1:
            outfile.seek(outfile.tell() - 1)
        elif outfile.tell() % MaxLineLength == MaxLineLength - 1:
            outfile.seek(outfile.tell() + 1)
        
        # Insert in the record
        outfile.write(first.encode("UTF-8"))
        first = infile.readline()
    infile.close()
    outfile.close()
    return 0
CreateCountry()

def LookUpCountry(CountryName):
    key = HashKey(CountryName)
    infile = open("NEWFILE", 'rb')
    infile.seek( (key - 1) * MaxLineLength)
    record = infile.read(MaxLineLength).decode("UTF-8")
    # need to add in country not exist check. 
    while record.split(' ')[0] != CountryName:
        key += 1
        infile.seek( (key - 1) * MaxLineLength)
        record = infile.read(MaxLineLength).decode("UTF-8")
    infile.close()
    while record[-1] == '\x00':
        record = record[:-1]
    return str(key) + ' ' + record

print(HashKey("India"))
print(LookUpCountry("India"))
print(HashKey("Chile"))
print(LookUpCountry("Chile"))
