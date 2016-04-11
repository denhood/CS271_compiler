'''
Title: Jack tokenizer
Authors: Harold Smith, Denny Hood
Class: CS 271
Description: This module will read in a jack text file, remove comments and white spaces,
    and generate a list of separate characters. Then a function called generate_words will
    group adjacent letters into keywords, integer constants and identifiers. Finally this
    module will generate an output file that the user specifies and wrap the lexical
    elements with their corresponding xml tags.
'''

import string

def open_file():
    '''this function will try to open a file stream and return a file pointer if
    successful'''
    filename = input("Enter file name: ")
    try:
        fptr = open(filename,'r')
        return fptr
    except:
        print("Error! no file name")
        return None
    
    
def file_to_list(fptr):
    '''this function takes in a file pointer and returns a list of each character
    in the file'''
    outputLst = list()
    if(fptr):
        for line in fptr:
            line = line.strip()
            if(line):
                if(line[0] != '/' and line[0] != '*'):
                    for char in line:
                        outputLst.append(char)
        fptr.close()
        return outputLst
    else:
        print("no file to read")
        return None

def generate_words(lstIn):
    '''this function takes in a list of characters and if the next character in
    the list is an ascii letter concatenates the two items and returns a list'''
    outputLst = list()
    tempStr = str()
    if(lstIn):
        for position in range(0,len(lstIn)):
            if(lstIn[position] in string.ascii_letters):
                if(position == len(lstIn)-1):
                    tempStr += lstIn[position]
                    outputLst.append(tempStr)
                    print("hit end")
                tempStr += lstIn[position]
            else:
                if(tempStr):
                    outputLst.append(tempStr)
                if(lstIn[position] != ' '):
                    outputLst.append(lstIn[position])
                tempStr = str()
    return outputLst

def is_in_list(testSym, lstIn):
    '''this function returns true if string testSym is in the list passed in'''
    if(testSym in lstIn):
        return True
    else:
        return False

def test_int(intIn):
    '''this function returns true if an integer in the list is between 0 and
    32,767'''
    try:
        test = int(intIn)
        if(test in range(0, 32768)):
            return True
        else:
            return False
    except:
        return False
    
def is_valid_identifier(stringIn):
    '''this function makes sure a string starts with a letter or a number
    and can only consist of letters, numbers and underscores'''
    validChars = string.ascii_letters + string.digits + "_"
    if(stringIn):
        if(stringIn[0] in string.ascii_letters or stringIn[0] in string.digits):
            for char in stringIn:
                if(char not in validChars):
                    print(stringIn," is not a valid identifier!")
                    return False
            return True
        else:
            print(stringIn," does not start with a letter or digit")
            return False
    else:
        print("no string to validate!")
        return False

def wrap_symbols(lstIn):
    '''this function wraps each token in the list passed in with its appropriate
    xml tags and returns a list'''
    symLst = ["(",")","{","}",";","[","]",".",",","+","-","*","/","&","|","<",">","=","~"]
    keyLst = ['class','constructor','function','method','field','static','var','int','char','boolean','void','true','false','null','this','let','do','if','else','while','return']
    outputLst = []
    for item in lstIn:
        if(is_in_list(item,symLst)):
            outputLst.append("<symbol> "+item+" </symbol>\n")
            
        elif(is_in_list(item,keyLst)):
            outputLst.append("<keyword> "+item+" </keyword>\n")
            
        elif(test_int(item)):
            outputLst.append("<integerConstant> "+item+" </integerConstant>\n")
            
        elif(item[0] == "\""):
            outputLst.append("<stringConstant> "+item[1:len(item)-1]+" </stringConstant>\n")
            
        elif(is_valid_identifier(item)):
            outputLst.append("<identifier> "+item+" </identifier>\n")
            
        else:
            print(item," does not appear as a Lexical element.")
            
    return outputLst
    
def write_list_to_file(lstIn):
    '''this function takes in a list of tokens and writes them to a file'''
    outputFile = input("enter name to write file to: ")
    lstIn = ['<tokens>\n']+lstIn+['</tokens>']
    if(isinstance(outputFile,str)):
        f = open((outputFile+".xml"),"w")
        for line in lstIn:
            f.write(line)
        f.close()
        print("file written successfully")
        return
    else:
        print("output filename invalid!")
        return

def generate_tokens_xml():
    '''main function prompts user for input filename, and output filename
    generates xml tokens for jack program
    '''
    outputLst = list()
    outputLst = generate_words(file_to_list(open_file()))
    outputLst = wrap_symbols(outputLst)
    write_list_to_file(outputLst)
    return outputLst

generate_tokens_xml()
                
