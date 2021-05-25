import json
X={}
while 1:
    Auth=int(input("Please press 1 to: translator developer or 2 to translator user \
or 3 to Exit:"))
    if Auth==1:
        while 1:
            word=input("enter the english word: ")
            word=word.upper()

            translate=input("enter the arabic word: ")
            translate=translate.upper()

            X[word]=translate

            z=input('press Enter to write anothe word or weite exit to finish ')
            z=z.upper()
            
            if z=='EXIT':
                with open('sample.json', 'r') as openfile:
                    json_object = json.load(openfile)
                    json_object.update(X)
                    json_object = json.dumps(json_object)
                    with open("sample.json", "w") as outfile:
                        outfile.write(json_object)
                break

    elif Auth==2:
        while 1:
            with open('sample.json', 'r') as openfile:
                json_object = json.load(openfile)
            word=input("enter the english word: ")
            word=word.upper()
            if word == "EXIT":
                break
            if word in json_object:
                print("the translat is: "+json_object[word])
            else:
                print ("the word not entered yet")
            print ("enter another word or EXIT to close ")
    elif Auth==3:
        break
