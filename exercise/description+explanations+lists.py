#Beschreibungen
#symbol description, Symbol Beschreibung
symDesc = {}
symDesc["Symbol"] = "Beschreibung"
symDesc["\t []"] = " ... list"
symDesc["\t {}"] = " ... dict"
symDesc["\t ()"] = " ... tuple"

for i,z in zip(symDesc.keys(),symDesc.values()):
    print(i,"\t",z)
        
print("")

#methods description, Methoden Beschreibung
methDesc = {}
methDesc["Methode"] = "Beschreibung"
methDesc["\t filterFile"] = "... makes a copy of oldFile, omitting any lines that begin with #:"
methDesc["\t dump"]= "... To store a data structure"
methDesc["\t load"]= "... get a single value from the file, complete with its original type."
methDesc["\t __init__"]= "... "

for i,z in zip(methDesc.keys(),methDesc.values()):
    print(i,"\t",z)

print("")

#statement description, Anweisungsbeschreibung
stateDesc = {}
stateDesc["statement"] = "Anweisungsbeschreibung"
stateDesc["\t continue"] = "... ends the current iteration of the loop, but continues looping"
stateDesc["\t raise"] = "... takes two arguments: the exception type and specific information about the error."
stateDesc["\t import"] = "... "
stateDesc["\t pass"] = "... "

for i,z in zip(stateDesc.keys(),stateDesc.values()):
    print(i,"\t",z)

print("")

#format operator description, Format-Operator Beschreibung
forOpDesc = {}
forOpDesc["format operator"] = "Beschreibung"
forOpDesc["\t %..."] = "... The number after the percent sign is the minimum number of spaces the number will take up"
forOpDesc["\t string"] = "... "
forOpDesc["\t sequence %d"] = "... means that the first expression in the tuple should be formatted as an integer, d = decimal"

for i,z in zip(forOpDesc.keys(),forOpDesc.values()):
    print(i,"\t",z)

print("")

#No Idea where i have to sort this One und Beschreibung
noIdeaWhereIHaveToSortThisOne = {}
noIdeaWhereIHaveToSortThisOne["NIWHEREIHTSTO"] = "Beschreibung"
noIdeaWhereIHaveToSortThisOne["\t pickling"] = "... called because it “preserves” data structures & contains the necessary commands"
noIdeaWhereIHaveToSortThisOne["\t class"] = "benutzerdefinierter Verbindungstyp"
noIdeaWhereIHaveToSortThisOne["\t Point"] = "is two numbers (e.g. coordinates) that are treated collectively as a single object \n members of this type are called instances of the type or objects"

for i,z in zip(noIdeaWhereIHaveToSortThisOne.keys(),noIdeaWhereIHaveToSortThisOne.values()):
    print(i,"\t",z)

print("")

#Error Fehlermeldungen und Beschreibung
errorReport = {}
errorReport["Error"] = "\tBeschreibung" + "e.g."
errorReport["\tZeroDivisionError: integer division or modulo"] = "... created an exception" + ">>> print 55/0"
errorReport["\t IndexError: list index out of range"] = "... >>> a = [] >>> print a[5]"

for i,z in zip(errorReport.keys(),errorReport.values()):
    print(i,"\t",z)

#Ende Beschreibungen