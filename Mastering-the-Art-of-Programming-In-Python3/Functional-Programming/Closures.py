def outer(param):
    def inner():
        print(param)
    
    return inner


func = outer(9)
func()
