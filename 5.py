# Διαβάζει ένα αρχείο και τροποποιεί όσες λέξεις του έχουν πάνω από 3 γράμματα.
# Το αρχείο αναμένεται να έχει όνομα 5.txt και να είναι κωδικοποιημένο σε UTF-8.
myfile = open("5.txt", encoding="utf8")
filetext = myfile.read()
myfile.close()
import string
cleantext = filetext.translate(str.maketrans("", "", string.punctuation))
wordlist = cleantext.lower().split()
moddedwordlist = [word[1:] + word[0] + "ay" if (len(word) > 3) else word for word in wordlist]
print(moddedwordlist)
