import sys
# all gates using nand gate
nand = lambda a, b: not (a and b)
NOT = lambda a: nand(a, a)
AND = lambda a, b: NOT(nand(a, b))
OR = lambda a, b: nand(NOT(a), NOT(b))

# sample input
"""
0,1,0,1 0
1,0,0,1 1
1,0,1,0 0
0,1,1,0 1  
"""

def get_truth_table():
    truth_table = {}

    print("Entry: x1,x2,x3,...,xn y")
    print("Press Enter Ctrl+D to stop:")

    # Read multiline input
    multiline_input = sys.stdin.read()

    
    for entry in multiline_input.strip().splitlines():
        inputs_str, output_str = entry.rsplit(' ', 1)  
        inputs = tuple(map(int, inputs_str.split(',')))  
        output = int(output_str) 
        truth_table[inputs] = output  

    return truth_table

def generate_function(truth_table):
    terms = []
    for i, (inputs,output) in enumerate(truth_table.items()):
        if output:  
            term = " and ".join(
                f"{'' if val else 'not '}x[{i}]" for i, val in enumerate(inputs)
            )
            terms.append(f"({term})")
    return f"lambda x: {' or '.join(terms)}"

def main():
    print("")
    print("      Truth Table => Function Generator")
    print("")
    truth_table = get_truth_table()
    exp = generate_function(truth_table)
    formula = eval(exp)
    exp = exp[10:]
    print("")
    print("function: ",exp)
    print("")
    for inputs, output in truth_table.items():
        result = formula(inputs)
        print(f"{inputs} -> {output} == {bool(result)}")
    print("")

if __name__ == "__main__":
    main()
