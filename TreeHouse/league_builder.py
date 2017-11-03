import csv
def player_csv():
    with open('soccer_players.csv', newline = '') as csvfile:
        player = csv.reader(csvfile, delimiter = ',')
        rows = list(player)
        player_rows = rows[1:]
        exp_player = []
        noob_player = []
        for items in player_rows:
            if items[2] == 'YES':
                exp_player.append(tuple(items))
            elif items[2] == 'NO':
                noob_player.append(tuple(items))
        Sharks = []
        Sharks.extend(exp_player[:3])
        Sharks.extend(noob_player[:3])

    with open('teams.txt','a') as file:
        file.write('Sharks' + '\n')
        for items in Sharks:
            row1 = str(items[0] + ", " + items[1] + ", " + items[2] + ", " + items[3])
            file.write((row1) + '\n')

    with open('teams.txt','a') as file:
        file.write('=====' + '\n')

        Raptors = []
        Raptors.extend(exp_player[3:6])
        Raptors.extend(noob_player[3:6])
    with open('teams.txt','a') as file:
        file.write('Raptors' + '\n')
        for items in Raptors:
            row2 = str(items[0] + ", " + items[1] + ", " + items[2] + ", " + items[3])
            file.write((row2) + '\n')

    with open('teams.txt','a') as file:
        file.write('=====' + '\n')

        Dragons = []
        Dragons.extend(exp_player[6:])
        Dragons.extend(noob_player[6:])

    with open('teams.txt','a') as file:
        file.write('Dragons' + '\n')
        for items in Dragons:
            row3 = str(items[0] + ", " + items[1] + ", " + items[2] + ", " + items[3])
            file.write((row3) + '\n')





if __name__ == '__main__':
    player_csv()
