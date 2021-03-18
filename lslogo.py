import sys
import state
import interpreter
import parser

def run():

    width = int(sys.argv[1])
    height  = int(sys.argv[2])
    #width = 15
    #height  = 15
    filename = sys.argv[3]
    

    etat = state.init_state(width,height,parser.parse_program(filename))

    #print(etat)
    interpreter.execute(etat["program"][10],etat)

    return None

run()