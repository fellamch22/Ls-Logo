import state as st
import ui 
import time
# to solve :
# ajouter le cas de PEN UP ET PEN DOWN

def execute(instruction,etat_tortue):

    # on donne en parametre le canvas la liste des variables 
    # et l'instruction qui est le tuple de la forme 
    # (code_instruction,liste d'arguments)

    etat = etat_tortue

    op , args = instruction

    if op == st.OP_ASSIGN :

        if isinstance(args[1],int) :
            etat["environment"][args[0]] = args[1]
        else:
            v = etat["environment"][args[1]]
            etat["environment"][args[0]] = v
        
        etat["pc"] = next_instruction(etat["pc"],etat["program"])  

    elif op == st.OP_FORWARD:

        n = args[0] if isinstance(args[0],int) else etat["environment"][args[0]]
        teta = etat["direction"] if etat["direction"] > 0 else etat["direction"]+360
        a = (teta % 360) if n > 0 else (teta + 180 ) % 360

        l , c = etat["position"]

        if a == 0 :

            if etat["drawing"]:

                #etat["canvas"][l][c] = etat["color"]

                for i in range(0,abs(n)):
                    c += 1

                    if c % etat["width"] == 0:
                     c = 0

                    etat["canvas"][l][c] = etat["color"]

            else:

                c = (c + abs(n)) % etat["width"]

             
        elif a == 45 :

            if etat["drawing"] :

                #etat["canvas"][l][c] = etat["color"]

                for i in range(0,abs(n)):
                    c += 1
                    l -= 1

                    if c % etat["width"] == 0:
                        c = 0
                    if l == -1 :
                        l = etat["height"] - 1

                    etat["canvas"][l][c] = etat["color"]

            else :

                c = (c + abs(n)) % etat["width"]
                l = etat["height"]- 1 - (abs(n) // (etat["height"]-1))

        elif a == 90 :

            if etat["drawing"]:

                #etat["canvas"][l][c] = etat["color"]

                for i in range(0,abs(n)):

                    l -= 1

                    if l == -1 :
                        l = etat["height"] - 1

                    etat["canvas"][l][c] = etat["color"]

            else:

                l = etat["height"]- 1 - (abs(n) // (etat["height"]-1))



        elif a == 135 :


            if etat["drawing"] :

                #etat["canvas"][l][c] = etat["color"]

                for i in range(0,abs(n)):
                    c -=1
                    l -=1

                    if c == -1 :
                        c = etat["width"] - 1 
                    if (l) == -1 :
                        l = etat["height"] - 1

                    etat["canvas"][l][c] = etat["color"]
            else:
                 c = etat["width"]- 1 - (abs(n) // (etat["width"]-1))
                 l = etat["height"]- 1 - (abs(n) // (etat["height"]-1))

                
        elif a == 180 :


            if etat["drawing"]:

            #etat["canvas"][l][c] = etat["color"]

                for i in range(0,abs(n)):
                    c -= 1
                    if c == -1:
                        c = etat["width"] -1

                    etat["canvas"][l][c] = etat["color"]
            else:

                 c = etat["width"]- 1 - (abs(n) // (etat["width"]-1))


        elif a == 225 :

            if etat["drawing"]:
            #etat["canvas"][l][c] = etat["color"]

                for i in range(0,abs(n)):
                    c -= 1
                    l += 1
                    if c == -1:
                        c = etat["width"] - 1 
                    if l % etat["height"] == 0 :
                        l = 0

                etat["canvas"][l][c] = etat["color"]

            else:

                c = etat["width"]- 1 - (abs(n) // (etat["width"]-1))
                l = ( l + abs(n) ) % etat["height"]


        elif a == 270 :

            if etat["drawing"]:
            #etat["canvas"][l][c] = etat["color"]

                for i in range(0,abs(n)):

                    l += 1

                    if l % etat["height"] == 0 :
                        l = 0

                    etat["canvas"][l][c] = etat["color"]
            
            else:

                l = ( l + abs(n) ) % etat["height"]



        elif a == 315 :

            if etat["drawing"] :
            #etat["canvas"][l][c] = etat["color"]

                for i in range(0,abs(n)):
                    c += 1
                    l += 1
                    if c % etat["width"] == 0:
                        c =  0

                    if l % etat["height"] == 0 :
                        l = 0
                        
                    etat["canvas"][l][c] = etat["color"]

            else:

                c = ( c + abs(n) ) % etat["width"]
                l = ( l + abs(n) ) % etat["height"]


        etat["position"] = (l,c)
        etat["pc"] = next_instruction(etat["pc"],etat["program"])  

    
    elif op == st.OP_ROTATE:

        etat["direction"] += args[0]
        etat["pc"] = next_instruction(etat["pc"],etat["program"])  
    
    elif op == st.OP_PEN_DOWN:

        etat["drawing"] = True
        etat["pc"] = next_instruction(etat["pc"],etat["program"])  

    elif op == st.OP_PEN_UP:

        etat["drawing"] = False
        etat["pc"] = next_instruction(etat["pc"],etat["program"])  

    elif op == st.OP_COLOR:

        etat["color"] = args[0]
        etat["pc"] = next_instruction(etat["pc"],etat["program"])  

    elif op == st.OP_INCR:

        if isinstance(args[1],int) :

            etat["environment"][args[0]] += args[1]

        else:

            etat["environment"][args[0]] += etat["environment"][args[1]]

        etat["pc"] = next_instruction(etat["pc"],etat["program"])  
    elif op == st.OP_GOTO:

        if isinstance(args[0],int) :

            etat["pc"] = args[0]

        else:

            etat["pc"] = etat["environment"][args[0]]
        

    elif op == st.OP_GOTONZ:

        pos = args[0] if isinstance(args[0],int) else etat["environment"][args[0]]
        expr = args[1] if isinstance(args[1],int) else etat["environment"][args[1]]
        
        if expr == 0 :

            etat["pc"] = next_instruction(etat["pc"],etat["program"])

        else:

            etat["pc"] = pos


    #time.sleep(4)'
    #print(etat["pc"])
    if etat["pc"] != None:

        execute(etat["program"][etat["pc"]],etat)
    else:
            ui.display(etat["canvas"])




def next_instruction(instruction,program):

    kiter = list(program)

    i = 0
    res = None

    for k in kiter :

        if k == instruction :

            res = kiter[i+1] if i+1 < len(kiter) else None
        
        i +=1
    return res
