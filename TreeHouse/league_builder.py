import csv
def player_csv():
    with open('soccer_players.csv', newline = '') as csvfile:
         # save the soccer_player csv lines into player variable
        player = csv.reader(csvfile, delimiter = ',')
         # save the lines in player in row variable as a list to be able to iterate through them 
        rows = list(player)
         # from rows grab everything after the first row
        player_rows = rows[1:]
         # create empty lists to separate experianced players vs new players 
        exp_player = []
        noob_player = []
         # place players in appropriate list
        for items in player_rows:
            if items[2] == 'YES':
                exp_player.append(tuple(items))
            elif items[2] == 'NO':
                noob_player.append(tuple(items))
                
         # create Sharks team with 3 new players and 3 experianced players
        Sharks = []
        Sharks.extend(exp_player[:3])
        Sharks.extend(noob_player[:3])
        
         # create and write the Shark list to the teams.txt file
    with open('teams.txt','a') as file:
        file.write('Sharks' + '\n')
        for items in Sharks:
            row1 = str(items[0] + ", " + items[1] + ", " + items[2] + ", " + items[3])
            file.write((row1) + '\n')
        
        # add some ==== simbols to separate the teams 
    with open('teams.txt','a') as file:
        file.write('=====' + '\n')
        
        # create Raptors team with 3 new players and 3 experianced players
        Raptors = []
        Raptors.extend(exp_player[3:6])
        Raptors.extend(noob_player[3:6])
        
         # create and write the Raptors list to the teams.txt file
    with open('teams.txt','a') as file:
        file.write('Raptors' + '\n')
        for items in Raptors:
            row2 = str(items[0] + ", " + items[1] + ", " + items[2] + ", " + items[3])
            file.write((row2) + '\n')
            
        # add some ==== simbols to separate the teams 
    with open('teams.txt','a') as file:
        file.write('=====' + '\n')
        
        # create Dragons team with 3 new players and 3 experianced players
        Dragons = []
        Dragons.extend(exp_player[6:])
        Dragons.extend(noob_player[6:])
        
         # create and write the Dragons list to the teams.txt file
    with open('teams.txt','a') as file:
        file.write('Dragons' + '\n')
        for items in Dragons:
            row3 = str(items[0] + ", " + items[1] + ", " + items[2] + ", " + items[3])
            file.write((row3) + '\n')





if __name__ == '__main__':
    player_csv()
