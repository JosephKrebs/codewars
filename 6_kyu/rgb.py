def indi(code):
    if code > 255:
        code = 255
        
    if code < 0:
        code = 0
    code = hex(code)[2:]
    
    if len(code) < 2:
        code = "0" + code
        
    return code    

def rgb(r, g, b):
    return indi(r).upper() + indi(g).upper() + indi(b).upper()