'''
Vikramaditya turn and walk
Scheme
He first turns and travels 10 units of distance
His second turn is upward for 20 units
Third turn is to the left for 30 units
Fourth turn is the downward for 40 units
Fifth turn is to the right(again) for 50 units
… And thus he travels, 
every time increasing the travel distance by 10 units.
Test cases
n    x,y
3    20,20
4    -20,-20
5    39,-20
7    90,-20
'''

#n = int(input('enter n:')) 

n=10
dist = 0
dir = 'r'
x=0
y=0
for i in range(1,n+1):
    dist += 10
    if dir == 'r':
        x += dist
        dir = 'u'
    elif dir == 'u':
        y += dist
        dir = 'l'
    elif dir == 'l':
        x  -= dist
        dir = 'd'
    elif dir == 'd':
        y -= dist
        dir = 'a'
    elif dir == 'a':
        x += dist
        dir = 'r'
    print(i,x,y)