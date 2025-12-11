translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}
word = input("Enter word to translate: ")
if word in translations:
    res = translations[word]
    print(res)
else:
    print("word not avalible")    
