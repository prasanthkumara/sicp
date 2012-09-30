def star(x,y):
    return(x==1 and y or x%2==0 and star(x/2,2*y) or y+star(x-1,y))
