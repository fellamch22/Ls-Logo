


def display(canvas):

    print("_"*(len(canvas[0])+6))

    for  i  in range(len(canvas)):
        print( '| ',"".join(canvas[i]),' |')

    print("_"*(len(canvas[0])+6))

#display([['*','*'],['*','*']])