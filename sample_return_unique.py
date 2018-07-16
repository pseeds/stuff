def return_unique(st0,st1):
    new_string = ""
    for c in stval0:
        if c not in stval1:
            new_string += c
    
    for c in stval1:
        if c not in stval0:
            new_string += c
            
    return new_string
    
    


stval0="abcdef"
stval1="a"

rv = return_unique(stval0,stval1)

print rv,

