def greeting(details):
    match details:
        case [time, name]:
            return f'Good {time} {name} !'
        case [time , *names]:
            msg =''
            for name in names:
                msg+=f'Good {time} {name}\n'
            return msg
print(greeting(["evening","Ram"]))
print(greeting(["Afternoon","manoj"]))
print(greeting(["evening","Ram", "Kiran"]))
    
