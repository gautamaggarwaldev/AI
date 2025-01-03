def function(*args, **kwargs):    # *args is used to pass a variable number of non-keyworded arguments to a function
    print(args)                   # **kwargs is used to pass a variable number of keyworded arguments to a function
    print(kwargs) 


function("GG", "James", name="John", age=25)


lst = [1,"gg",2,3]
dit = {"name":"John", "age":25}

function(lst, dit) 

function(*lst, **dit) 