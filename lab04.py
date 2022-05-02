from Stack import *
# def printMaze(maze):
# 	for row in range(len(maze)):
# 		for col in range(len(maze[0])):
# 			print("|{:<2}".format(maze[row][col]), sep='',end='')
# 		print("|")
# 	return
def solveMaze(maze,startX,startY):

    s = Stack()

    s.push([startX,startY])

    step = 1
    maze[startX][startY]=step
    step+=1

    while s.size() != 0:

        x = s.peek()[0]
        y = s.peek()[1]

        if maze[x-1][y] == " " :

            s.push([x-1,y])
            maze[x-1][y] = step
            

            step+=1
                
           

        elif maze[x][y-1] == " " :
            s.push([x,y-1])


            maze[x][y-1] = step

            step+=1
            
        elif maze[x+1][y] == " " :

            s.push([x+1,y])
            maze[x+1][y] = step
            
            step+=1

        elif maze[x][y+1] == " " :

            s.push([x,y+1])
            maze[x][y+1] = step
            
            step+=1
        
        elif maze[x-1][y] == "G":
            return True
        elif maze[x][y-1] == "G":
            return True
        elif maze[x+1][y] == "G":
            return True
        elif maze[x][y+1] == "G":
            return True
        
        else:
            s.pop()
            
    return False


    










    



