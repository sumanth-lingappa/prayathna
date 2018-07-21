holesDict = {
                "0" : ["C","c","E","F","f","G","H","h","I","i","J","j","K","k","L","l","M","m",
                       "N","n","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z",\
                       "1","2","3","4","5","7",],
                "1" : ["A","a","b","D","d","e","g","O","o","P","p","Q","q","R","6","9",],
                "2" : ["B","8",],
            }


if __name__ == "__main__":
    holesList = []
    T = raw_input("Enter Number")
    for i in range(int(T)):
        holes = 0
        text = raw_input("Enter Text")
        for i in list(text):
            for key in holesDict.keys():
                if i in holesDict[key]:
                    holes += int(key)
        holesList.append(holes)
    for i in range(int(T)):
        print holesList[i]
    raw_input("Hit enter to exit")
