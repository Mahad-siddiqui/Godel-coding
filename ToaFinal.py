final_states=['q1']
start_states=['q0']
def decode_godal_encoding(encoded_str):
    """
    Decodes a string of 0s and 1s into a dictionary of transitions.
    where each transition is a tuple of (current_state, current_symbol, next_state, next_symbol, move).
    """
    encoded_str=encoded_str.strip('000')  # Remove leading and trailing 000 which indicates start and end
    transitions = encoded_str.split('00')   # each transition is separated by 00 so gettib
    parsed_transitions = {}

    for tran in transitions:
        print(tran)
        trans=tran.split('0')  
        current_state = decode_state(trans[0])
        current_symbol = decode_symbol(trans[1])
        next_state = decode_state(trans[2])
        next_symbol = decode_symbol(trans[3])
        move = decode_move(trans[4])

        parsed_transitions[(current_state, current_symbol)] = (next_state, next_symbol, move)
    
    return parsed_transitions

def decode_state(encoded_state):
    possible_states={'1':'q0','11':'q1','111':'q2'}
    return possible_states.get(encoded_state,"state not found")
def decode_symbol(encoded_symbol):
    possible_symbols={'1':'0','11':'1','111':'B'}
    return possible_symbols.get(encoded_symbol,"symbol not found")
def decode_move(encoded_move):
    possible_moves={'1':'L','11':'R'}
    return possible_moves.get(encoded_move,"move not found")

def simulate_turing_machine(transitions, input_str):
    """
    Simulates the Turing Machine for the given input string and transitions.
    """
    #remove blank symbol and explicit;y adding one
    input_str=input_str.strip('B')
    tape = ['B']+list(input_str)  

    print(f"input tape : {tape}")
    print("starting state : q0")

    head = 0   #starts from begging
    current_state = start_states[0]

    while head < len(tape):
        current_symbol = tape[head]

        if (current_state, current_symbol) not in transitions:                            
            print("Reject")
            return   
        
        print(f"current head position : {head}")
        print(f"input to transition function : ( {current_state}, {current_symbol} )")

        next_state, next_symbol, move = transitions[(current_state, current_symbol)]
        
        print(f"output from transition function : ( {next_state}, {next_symbol}, {move} )")
        tape[head] = next_symbol
        current_state = next_state

        if move == 'R':
            print("moving right")
            head += 1
        elif move == 'L':
            print("moving left")
            head -= 1
            if head<0:
                tape.insert(0,'B')
                head=0

    if current_state in final_states:  
        print("Accept")
        return

    print("Reject",current_state)


if __name__== "__main__":
    
        # Read the TM encoding from a file
    filename = input("Enter the filename containing the Turing Machine encoding: ")
    try:
        with open(filename, 'r') as file:
            encoded_tm = file.read().strip()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    
      
    transitions = decode_godal_encoding(encoded_tm)
    print("Parsed Transitions:", transitions)

    input_str = input("Enter input string (consisting of 0s and 1s): ")
    simulate_turing_machine(transitions, input_str)


    # first transformation
    # 10  1110  110  1110 11
    # q0  B    q1     B   R