# -*- coding: utf-8 -*-
#imported modules
import io
import array
import fileinput

#test functions
#newNum = 4
#print newNum

#MAIN
#Variables
arVerbs=["o", "as", "a", "amos", "ais", "an"]
erVerbs=["o", "es", "e", "emos", "eis", "en"]
irVerbs=["o", "es", "e", "imos", "is", "en"]
#print "You for an 'AR' verb is: " + arVerbs[1]
#print "Us for an 'IR' verb is: " + irVerbs[3]

#user input
myVerb = "start"
print myVerb
while myVerb != "end":
    print ""
    print "__________________"
    myVerb = raw_input('What is your verb, to translate to *you* ? - ')
    if myVerb == "end":
        print "Goodbye!"
        print "__________________"
    else:
        print "You typed '" + myVerb + "'?"
    print ""

    #verb identifier
    if "ar" in myVerb:
        print "Hm... I see an 'ar' verb... your verb is:"
        myVerb = str.rstrip(myVerb, 'arz')
        print myVerb + arVerbs[1]
    elif "er" in myVerb:
        print "Hm... I see an 'er' verb... your verb is:"
        myVerb = str.rstrip(myVerb, 'erz')
        print myVerb + erVerbs[1]
    elif "ir" in myVerb:
        print "Hm... I see an 'ir' verb... your verb is:"
        myVerb = str.rstrip(myVerb, 'irz')
        print myVerb + erVerbs[1]
    
# AR VERBS o as a amos ais an
# ER VERBS o es e emos eis en
# IR VERBS o es e imos is en
