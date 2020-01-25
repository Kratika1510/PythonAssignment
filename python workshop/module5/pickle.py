import pickle
phonebook={'Chris':'555-1111','Katie':'555-2222','joanne':'555-3333'}
output_file=open('phonebook.dat','wb')
pickle.dump(phonebook,output_file)
output_file.close()
infile=open('phonebook.dat','rb')
print(pickle.load(infile))
print(infile.read())
