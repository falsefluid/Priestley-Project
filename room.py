#room.py
import csv
def room():
    filename="MainSheet.csv"
    fields=[]
    rows=[]
    rooms=["LC.1","LC.2","LC.3","LC.4","LC.5","P1.1","P1.2","P1.3","P1.4","P1.5"]
    temprooms = rooms # copy of rooms list for modification
    LightsOn=True
    
    # Read CSV file and load rows into 'rows' list
    with open(filename,"r") as mainfile:
        csvreader=csv.reader(mainfile)
        fields=next(csvreader)
        for row in csvreader:
            rows.append(row)

    # Iterate through rows (up to the first 100 rows for demonstration)
    for row in rows[:100]:
        a=row[11]
        b=row[1]
        c=row[2]
        
        if a =="None":
            print("==================")
            print(b, c, "is not in a room")
        
        elif a in rooms:
            print("==================")
            print(a,"In use by", b, c)
            LightsOn=True
            temprooms.remove(a) # remove room from temporary list if in use
    
    # Turns off lights for rooms not in use
    for x in range(len(temprooms)):
        print("==================")
        print(temprooms[x],"Not in use, turning lights off")
        LightsOn=False


