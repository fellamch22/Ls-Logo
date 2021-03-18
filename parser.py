import re
import state as st


def parse_program(filename):

    # nom des variables comme cle / contenu comme valeur
    variables = {}

    # num de la ligne comme cle / 
    # tuple(code de l'instruction comme valeur,[num.instr])
    instructions = {}

    f = open(filename)

    for x in f :

        # si c'est un commentaire on ignore

        if re.fullmatch("//[ ].*",x) == None:
            ## pas un commentaire

            # decouper en 3 groupes
            # num de ligne / instruction / commentaire si il existe
            p = re.search("(\d+) (.+)[ ]*(//[ ].*)?",x)
            
            if p :
            #    instructions[int(p.group(1))]
            #   print(p.group(2))

            #Apres le decoupage , on analyse l'instruction

            #si c'est une affectation
                 #    xsteps   = 3
                p1 = re.search("([a-z]+)[ ]{1,}[=][ ]{1,}([^ ]+)",p.group(2))
                if p1 :
                    
                    if re.fullmatch("[-]?\d+",p1.group(2)) :

                        instructions[int(p.group(1))] = (st.OP_ASSIGN,[p1.group(1),int(p1.group(2))])

                    else:

                        instructions[int(p.group(1))] = (st.OP_ASSIGN,[p1.group(1),p1.group(2)])

                else:
                    # incermentation
                    p1 = re.search("([a-z]+)[ ]{1,}[+][=][ ]{1,}([a-z]+)",p.group(2))

                    if p1 :
                        
                        instructions[int(p.group(1))] = (st.OP_ASSIGN,list(p1.group(1),p1.group(2)))
                    
                    else:

                    # incerementation 
                    #    xsteps   +=   -1
                        p1 = re.search("([a-z]+)[ ]{1,}[+][=][ ]{1,}([-]?\d+)",p.group(2))
                   
                        if p1 :
                            
                            instructions[int(p.group(1))] =  (st.OP_INCR,[p1.group(1),int(p1.group(2))])

                    
                        else:

                         p1 = re.search("FORWARD[ ]{1,}([-]?\d+)",p.group(2))


                         if p1 :

                            instructions[int(p.group(1))] = (st.OP_FORWARD,[int(p1.group(1))])

                         else:

                            p1 = re.search("FORWARD[ ]{1,}([a-z]+)",p.group(2))

                            if p1 : 
                                instructions[int(p.group(1))] = (st.OP_FORWARD,[p1.group(1)])

                            else:

                                p1 = re.search("ROTATE[ ]{1,}([-]?\d+)",p.group(2))
                            
                                if p1 :

                                    instructions[int(p.group(1))] = (st.OP_ROTATE,[int(p1.group(1))])

                                else:

                                    p1 = re.search("PEN[ ]{1,}UP",p.group(2))

                                    if p1 :

                                        instructions[int(p.group(1))] = (st.OP_PEN_UP,[])                                        

                                    else:

                                        p1 = re.search("PEN[ ]{1,}DOWN",p.group(2))

                                        if p1 :

                                            instructions[int(p.group(1))] = (st.OP_PEN_DOWN,[])
                                        
                                        else :

                                            p1 = re.search("COLOR[ ]{1,}(.)",p.group(2))
                                        
                                            if p1 :
                                                
                                                instructions[int(p.group(1))] = (st.OP_COLOR,[p1.group(1)])

                                            else:

                                                p1 = re.search("GOTONZ[ ]{1,}([^ ]+)[ ]{1,}([^ ]+)",p.group(2))

                                                if p1 :
                                                    argl = []

                                                    if re.fullmatch("\d+", p1.group(1)) :
                                                    # il faut verifier les deux au mm temps
                                                        argl.append(int(p1.group(1)))

                                                    else:

                                                        argl.append(p1.group(1))

                                                    if re.fullmatch("\d+", p1.group(2)) :
                                                    # il faut verifier les deux au mm temps
                                                        argl.append(int(p1.group(2)))

                                                    else:

                                                        argl.append(p1.group(2))

                                                    instructions[int(p.group(1))] = (st.OP_GOTONZ,argl)     

                                        

                                                else :

                                                    p1 = re.search("GOTO[ ]{1,}([^ ]+)",p.group(2))

                                                    if p1 :

                                                        if re.fullmatch("\d+", p1.group(1)) :
                                                            # il faut verifier les deux au mm temps
                                                            instructions[int(p.group(1))] = (st.OP_GOTO,[int(p1.group(1))])     

                                                        else:

                                                            instructions[int(p.group(1))] = (st.OP_GOTO,[p1.group(1)])







            





    return instructions


print(parse_program("swirloop.logo"))