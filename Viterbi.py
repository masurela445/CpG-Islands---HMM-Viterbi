def Viterbi(x, states, Transition, Emmission):
    return_string = '' 
    product_weight = [dict()]
    for state in states:
        product_weight[0][state] = (1, state)
    for i in range(len(x)):
        product_weight.append(dict())
        for state in states:
            max_probability = 0
            state_prev = ''
            for k in states:
                probability=  product_weight[i][k][0]* Transition[k][state]* Emmission[state][x[i]]
                if probability > max_probability:
                    max_probability = probability
                    state_prev = k
            product_weight[i+1][state] = (max_probability,state_prev)

    print(product_weight)
    max_weight = 0
    prev = ''
    store = ''
    for key in product_weight[-1].keys():
        if product_weight[-1][key][0] > max_weight:
            max_weight = product_weight[-1][key][0]
            prev = product_weight[-1][key][1]
            store = key
    return_string = store + return_string 
    print(return_string)
    for i in range(2,len(product_weight)):
        return_string = prev  + return_string
        prev = product_weight[-i][prev][1]
                
    # for weight in product_weight[1:]:
    #     # print(weight)
    #     max_weight = max(weight.values())
    #     for key in weight.keys():
    #         if weight[key] == max_weight:
    #             return_string += key
    #             break
    
    return return_string

# Input_x = 'xyxzzxyxyy'
# Input_states = ['A', 'B']
# Input_Transition = {'A':{'A':0.641, 'B':0.359},'B':{'A':0.729, 'B':0.271}}
# Input_Emission = {'A':{'x':0.117, 'y':0.691,'z':0.192},'B':{'x':0.097, 'y':0.42,'z':0.483}}

# print(Viterbi(Input_x,Input_states,Input_Transition,Input_Emission))

Input_x = ''
Input_states = []
alphabet = []
Input_Transition = dict()
Input_Emission = dict()
with open("10_dataset.txt", "r") as f:
    lines = f.readlines()
    Input_x = lines[0].strip()
    for element in lines[2].split():
        alphabet.append(element)
    for element in lines[4].split():
        Input_states.append(element)

with open("10_Transition.txt", "r") as f:
    lines = f.readlines()

    for line in lines[1:]:
        line = line.split()
        Input_Transition[line[0]] = dict()

        for i in range(1,len(Input_states)+1):
            Input_Transition[line[0]][Input_states[i-1]]=float(line[i])

with open("10_Emission.txt", "r") as f:
    lines = f.readlines()

    for line in lines[1:]:
        line = line.split()
        Input_Emission[line[0]] = dict()

        for i in range(1,len(alphabet)+1):
            Input_Emission[line[0]][alphabet[i-1]]=float(line[i])

# print(Input_Transition)
# print(Input_Emission)
print(Viterbi(Input_x,Input_states,Input_Transition,Input_Emission))
