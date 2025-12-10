import queue
expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"
def brackets_ok(expression):

    stack = queue.LifoQueue()   

    for i in expression:        
        if i not in "[](){}":
            continue

        
        if i in "([{":
            stack.put(i)

       
        else:
            if stack.empty():
                return False    

            last = stack.get()

            
            if (i == ")" and last != "(") or \
               (i == "]" and last != "[") or \
               (i == "}" and last != "{"):
                return False

    return stack.empty()

print(brackets_ok(expression2))

