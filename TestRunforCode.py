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
        leaderboard=[sorted_rows[0:9]]
        print(type(leaderboard))
        for leader in range(0,9):
            print(leaderboard[leader], end="\n")
            print()

    FILE.close()
    

print("'Share Scores' selected")
fileSortR()
