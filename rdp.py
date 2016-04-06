test = ["if","(","x","=","10",")","{","let","y","=","10",";","}"]

def validate_expression(subLst):
    if("=" in subLst):
        postion = subLst.index("=")
        if(postion > 0 and postion<len(subLst)-1):
            return True
        else:
            return False
    elif(">" in subLst):
        position = subLst.index(">")
        if(position > 0 and position<len(subLst)-1):
            return True
        else:
            return False
def generate_statement(lstIn):
    position = lstIn.index("{")
    end      = lstIn.index("}")
    return lstIn[position+1:end]

def generate_expression(lstIn):
    position = lstIn.index("(")
    end      = lstIn.index(")")
    return lstIn[position+1:end]

def validate_statement(subLst):
    if(subLst[0] == 'let' and '=' in subLst and ';' in subLst):
        return True
    else:
        return False
