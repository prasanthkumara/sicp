def star(x,y,z):
    return(x==0 and z or star(x-1,y,z+y))
