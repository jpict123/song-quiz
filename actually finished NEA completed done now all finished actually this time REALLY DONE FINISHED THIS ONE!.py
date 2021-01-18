while True:
    ##START##
    print("----login to song game----")
    usernameinput = input("Please input your username: ")#askes user to input username
    passwordinput = input("Please input your password: ")#askes user to input password

    #Read-in
    for line in open("accounts.txt","r").readlines(): # Read the lines
        login_info = line.split()# Split on the space , and store the results in a list of two strings
        if usernameinput == login_info[0] and passwordinput == login_info[1]:
            print("Correct credentials!")

            
            ##MAIN GAME##
            from random import randint # imports random number generator.
            import re #imports encryptor for song title
            songfile = open("SongNames.txt","r") #reads in songs and the artists accosiated with them

            points=0

            title = []
            artists = []

            for row in songfile: #seperates artists and songs from external file
                field = row.split(",")
                songs = field[0]
                artist = field[1]
                title.append(songs)
                artists.append(artist)
            songfile.close()

            while True:
                if len(title)>=1:
                    randomIndex = (randint(0, (len(title)-1))) #chooses random index
                    randomSong = title[randomIndex].title() #chooses the title from index number
                    acronym = (''.join(re.findall('[A-Z]',randomSong))) #creates title encryption
                    
                    print("What song has the title with the acronym " ,acronym, " by: " ,artists[randomIndex]) #asks the question
                
                    answer=randomSong.lower() #answer all in lower case

                    guess1=input("input your first guess for three points if you are correct!: ").lower()

                    title.pop(randomIndex)
                    artists.pop(randomIndex)

                    if guess1 == answer:
                        print("Great work you got three points")
                        points+=3 #adds three points to the players score
                    else:
                        print("Unlucky :( have another go.")
                        guess2=input("input your second chance and if you're right you'll get one point!: ").lower()
                        if guess2 == answer:
                            print("Great work you got one point")
                            points+=1 #adds one point to the players score
                        else:
                            print("you finished your game with " ,points, " points!!!")
                            break #finishes game
                else:
                    print("you finished your game with " ,points, " points!!!") 
                    break #finishes game
            ##MAIN GAME END##
            ##SCORES START##
            scorefile= open("Scores.txt","a")
            #print("This program writes data to "Scores.txt")
            #print("If the file does not exist it will be created")
            name = usernameinput
            points = str(points)
            Scores = points
            scorefile.write(name + "," + points + "\n")
            scorefile.close()

            f = open("Scores.txt", "r").readlines() # appends score variable with scores from external file
            Scores = []
            for i in f:
                fields = i.split(",")
                Scores.append([int(fields[1].rstrip("\n")),"by:",fields[0]])#removes newline and joines variables together.
            a = Scores
            #b = [item[1] for item in a]
            sortedScores = sorted(a, key = lambda x: int(x[0]), reverse = True)
            if len(a) >=5:
                for i in sortedScores[0:5]:
                    print(i)
            else:
                print("Not five scores yet :(")

            break
            ##SCORES END##
        else:
            print("Incorrect credentials.")
            continue
    ##END##

