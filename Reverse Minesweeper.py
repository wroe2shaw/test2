
import string
def isOnField(cord):
    x = cord[1]
    y = cord[0]
    if(x >= 0 and x < w):
        if ( y >= 0 and y < h):
            return True
    return False

def prox(cord):
    x = cord[1]
    y = cord[0]
    proximity = matrix[y][x]
    #print(f'Proximity: {proximity}')
    if proximity == 'x':
        proxCount = 'x'
    if proximity == '.':
        proxCount = 1
    if proximity.isdigit():
            proxCount = int(proximity) + 1      
    
    return str(proxCount)


def detector(cord): 
    #print(f'Coordinates given: {cord[0], cord[1]}')
    x = cord[0]
    y = cord[1]

    #Top Row
    '''Top left'''
    if(isOnField([y-1, x-1])):
        proxCount = prox([y-1, x-1])
        matrix[y-1] =  matrix[y-1][:x-1] + proxCount + matrix[y-1][(x-1)+1:]
    '''Top Mid'''
    if(isOnField([y-1, x])):
        proxCount = prox([y-1, x])
        matrix[y-1] =  matrix[y-1][:x] + proxCount + matrix[y-1][x+1:]
    '''Top Right'''
    if(isOnField([y-1, x+1])):
        proxCount = prox([y-1, x+1])
        matrix[y-1] =  matrix[y-1][:x+1] + proxCount + matrix[y-1][(x+1)+1:]
    

    #Middle Row
    '''Middle Left'''
    if(isOnField([y, x-1])):
        proxCount = prox([y, x-1])
        matrix[y] = matrix[y][:x-1] + proxCount + matrix[y][(x-1)+1:]
    #'''Middle Mid'''
    #if(isOnField([y, x])):
    #    proxCount = prox([y, x])
    #    matrix[y] = matrix[y][:x] + '.' + matrix[y][x+1:]
    '''Middle Right'''
    if(isOnField([y, x+1])):
        proxCount = prox([y, x+1])
        matrix[y] =  matrix[y][:x+1] + proxCount + matrix[y][(x+1)+1:]

    #Bottom Row
    '''Bot Left'''
    if(isOnField([y+1, x-1])):
        proxCount = prox([y+1, x-1])
        matrix[y+1] = matrix[y+1][:x-1] + proxCount + matrix[y+1][(x-1)+1:]
    '''Bot Mid'''
    if(isOnField([y+1, x])):
        proxCount = prox([y+1, x])
        matrix[y+1] = matrix[y+1][:x] + proxCount + matrix[y+1][x+1:]
    '''Bot Right'''
    if(isOnField([y+1, x+1])):
        proxCount = prox([y+1, x+1])
        matrix[y+1] =  matrix[y+1][:x+1] + '1' + matrix[y+1][(x+1)+1:]


def disarm(cord):
    #print(f'Coordinates given: {cord[0], cord[1]}')
    #print(f'Disarming')
    x = cord[0]
    y = cord[1]
    matrix[y] = matrix[y][:x] + '.' + matrix[y][x+1:]

# w = 16
# h = 9

# matrix = [
# '................',
# '................',
# '................',
# '................',
# '................',
# '....x...........',
# '................',
# '................',
# '................',
# ]

w = 10 
h = 7 

matrix = [
    '..........',
    '.x...x...x',
    '..x......x',
    '.....x....',
    '..x.x...x.',
    'x.........',
    '.x...x...x',
]

bombLocations = []

for i in range(0,h):
    for j in range(0,w):
        'Check if bomb is found'
        if matrix[i][j] == 'x':
            bombLocations.append([j,i])
        print(matrix[i][j], end = '')
    print()

for bomb in range(len(bombLocations)):
    detector(bombLocations[bomb])

for bomb in range(len(bombLocations)):
    disarm(bombLocations[bomb])


for i in range(0,h):
    for j in range(0,w):
        print(matrix[i][j], end = '')
    print()






 