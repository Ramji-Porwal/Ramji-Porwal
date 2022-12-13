data=input("Input Strings: ")                           #taking multiple strings as input.
list1=data.split(",")                                   #converting given strings to list i.e.('list of strings') using split function
acronym=""                                              #creating an empty string.
for i in list1:                                         #taking collection based or iterable based for loop.
    words=i.split(" ")                                  #splitting the given strings by space to fetch the first letter.
    if (len(words)>1):                                  #condition statement for not taking string whose length is 1 or less than 1
       for i in words:                                  #iterable based loop for fetching the first letter
           acronym+=i[0]                                #fetching first word of each string.
    acronym+=" "                                        #giving space after every strings.
    acronym=acronym.upper()                             #changing acronym to uppercase
print("Acronyms of the given strings are: ",acronym)    #printing the acronyms.

