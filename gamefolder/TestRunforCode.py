#Eliza Lamster
#6/16/2021

def fileSortR():
    scoredata="ElizaGame.txt"
    FILE=open(scoredata, 'r')
    content_List=FILE.readlines()
    for element in content_List:
        global elem_List
        elem_List=element.split()
    FILE.close()
    with open(scoredata, "r") as firstfile:
        rows=firstfile.readlines()
        sorted_rows=sorted(rows, key = lambda x: int(x.split()[1]), reverse=True,)
        print
        for row in sorted_rows:
            if content_List[1]>3:
                print(row)
            print(row)
    FILE.close()
    

print("'Share Scores' selected")
fileSortR()
