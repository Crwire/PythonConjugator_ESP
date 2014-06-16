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
persons=["Yo ", "Tu ", "El ", "Ella ", "Nosotros ", "Vosotros ", "Ellos ", "Ellas "]

#Required functions
def print_line(): #Simple printline function
    print "___________________________________________________________\n"

#Function to return yo, tu, el, nosotros, vosotros or ellos
def return_pre (eng_pre = "i"):
    return_value = "Yo "
    if eng_pre in ("i", "I"):
        return_value = persons[0]
    elif eng_pre in ("you", "You"):
        return_value = persons[1]
    elif eng_pre in ("he", "He"):
        return_value = persons[2]
    elif eng_pre in ("she", "She"):
        return_value = persons[3]
    elif eng_pre in ("we", "We"):
        return_value = persons[4]
    else : return_value = "* "
    return return_value

#Function to conjugate verb identifier
def return_conj_verb(verb_inf, esp_pre):
    # verb_type,
    verb_stem = "*"
    full_conjugation = "*"
    verb_index = 0
    #Find list index for the verb ending i.e. o, as, a etc
    for x in range (0, 8):
        if esp_pre == persons[x]:
            verb_index = x
            break
    #Correct for El/Ella and Ellos/Ellas
    if verb_index in (3, 4, 5, 6):
        verb_index = verb_index - 1
    elif verb_index == 7:
        verb_index = verb_index-2
    #Evaluate ar, er ,ir
    if "ar" in verb_inf:
        verb_stem = str.rstrip(verb_inf, 'arz')
        verb_stem = verb_stem + arVerbs[verb_index]
        full_conjugation = esp_pre + verb_stem
    elif "er" in verb_inf:
        verb_stem = str.rstrip(verb_inf, 'erz')
        verb_stem = verb_stem + erVerbs[verb_index]
        full_conjugation = esp_pre + verb_stem
    elif "ir" in verb_inf:
        verb_stem = str.rstrip(verb_inf, 'irz')
        verb_stem = verb_stem + irVerbs[verb_index]
        full_conjugation = esp_pre + verb_stem
    else: full_conjugation = "Not a Spanish verb!"
    return full_conjugation

#user input
print_line()
myVerb = "Spanish Conjugator v1.1\nCoded by Crwire (C) June 2014"
continue_session = True
print myVerb
while continue_session == True:
    print_line()
    myVerb = raw_input('What is your verb, to translate to *you* ? - ')
    if myVerb in ("end", "e", "en", "E", "EN", "END"):
        print "Goodbye!"
        print_line()
        continue_session = False
        break
    else:
        print "You typed '" + myVerb + "'?\n"

    #Find person, conjugate then output
    myPre = raw_input('In which person? - ')
    #Final output
    print return_conj_verb(myVerb, return_pre(myPre))

    
# AR VERBS o as a amos ais an
# ER VERBS o es e emos eis en
# IR VERBS o es e imos is en
