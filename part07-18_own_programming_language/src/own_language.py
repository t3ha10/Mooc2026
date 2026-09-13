# Write your solution here


def convert_to_command(text, index):
  parts = text.split(" ")
  action = parts[0]

  command = {}

  command["action"] = action
  
  if action in ("ADD", "SUB", "MUL", "MOV"):
      command["variable"] = parts[1]
      command["value"] = parts[2]
  elif action == "PRINT":
      command["value"] = parts[1]
  elif action == "JUMP":
      command["name"] = parts[1]
  elif action == "END":
      pass
  elif action == "IF":
      command["op1"] = parts[1]
      command["op2"] = parts[3]
      command["operator"] = parts[2]
      sub_text = " ".join(parts[4:])
      command["run"] = convert_to_command(sub_text, index)
  else:
      if action and action[-1] == ":":
          command["action"] = "LOCATION"
          command["name"] = parts[0][:-1]
          command["index"] = index
  return command

def read_program(program):
  commands = []
  location_index = {}
  for i in range(len(program)):
    text = program[i]
    command = convert_to_command(text, i)
    commands.append(command)
    if command["action"] == "LOCATION":
      location_index[command["name"]] = command["index"]


  return commands, location_index

def calculate(operator, operand1, operand2):
  result = 0
  number_operand1 = int(operand1)
  number_operand2 = int(operand2)
  if operator == "ADD":
    result = number_operand1 + number_operand2
  elif operator == "SUB":
    result = number_operand1 - number_operand2

  elif operator == "MUL":
    result = number_operand1 * number_operand2
  return result


def exec_jump(name, location_index):
  return location_index[name]


def execute_condition(op1, op2, operator):
  if operator == "<=":
    return op1 <= op2
  elif operator == ">=":
    return op1 >= op2
  elif operator == "<":
    return op1 < op2
  elif operator == ">":
    return op1 > op2
  elif operator == "==":
    return op1 == op2
  elif operator == "!=":
    return op1 != op2

def get_variable_value(variable, variable_program):
  if variable in variable_program:
    return variable_program[variable]
  else:
    try:
      return int(variable)
    except:
      return 0

def set_variable_value(variable, variable_program, value=0):
  variable_program[variable] = value


def run(program):
  commands, location_index = read_program(program)
  # variable_program = {"A": 3, "B": 5...}
  variable_program = {}
  # location_index = {"begin": 8, "quit": 15}
  
  result = []
  i = 0
  while i < len(commands):
    line = commands[i]
    action = line["action"]
    if action == "MOV":
      variable = line["variable"]
      value_line = line["value"]
      if value_line in variable_program:
        value = variable_program[value_line]
        set_variable_value(variable, variable_program, value)
      else:
        variable_program[variable] = int(value_line)

    elif action in ["ADD", "SUB", "MUL"]:
      variable = line["variable"]

      cur_var = get_variable_value(variable, variable_program)
      val_act = line["value"]
      if val_act not in variable_program:
        value = calculate(action, cur_var, int(val_act))
      else:
        value = calculate(action, cur_var, variable_program[val_act])
      set_variable_value(variable, variable_program, value)

    elif action == "PRINT":
      value_line = line["value"]
      value = get_variable_value(value_line, variable_program)
      result.append(value)


    elif action == "JUMP":
      name = line["name"]
      i = exec_jump(name, location_index)

    elif action == "IF":
      operator = line["operator"]
      if line["op1"] in variable_program:
        op1 = variable_program[line["op1"]]
      else:
        op1 = int(line["op1"])

      if line["op2"] in variable_program:
        op2 = variable_program[line["op2"]]
      else: 
        op2 = int(line["op2"])

      if execute_condition(op1, op2, operator) == True:
        run = line["run"]
        run_action = run["action"]
        run_name = run["name"]
        i = exec_jump(run_name, location_index)
    elif action == "END":
      #   # "END"
      break
    i += 1
     
  return result
    


def get_test_data(number):
  if number == 1:
    return {}
  elif number == 2:
    return {}
  elif number == 3:
    return {}
  elif number == 4:
    return {}
  elif number == 5:
    return {
      "data": [
        'PRINT A',
        'END',
      ],
      "output": [0]
    }
  elif number == 6:
    return {
      "data": ['MOV A 1', 'MOV B 999', 'start:', 'ADD A 1', 'SUB B 1', 'ADD C 1', 'IF A == B JUMP end', 'JUMP start', 'end:', 'PRINT C'],
      "output": [499]
    }
  elif number == 7:
    return {
      "data": ["MOV N 100","PRINT 2","MOV A 3","start:","MOV B 2","MOV Z 0","test:","MOV C B","new:","IF C == A JUMP virhe","IF C > A JUMP pass_by","ADD C B","JUMP new","virhe:","MOV Z 1","JUMP pass_by2","pass_by:","ADD B 1","IF B < A JUMP test","pass_by2:","IF Z == 1 JUMP pass_by3","PRINT A","pass_by3:","ADD A 1","IF A <= N JUMP start"],
      "output": [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    }

def check_test_data(result, output):
  for i in range(len(output)):
    if result[i] != output[i]:
      return False
  
  return True

    



if __name__ == "__main__":
  
  number_of_tests = 7
  for test_number in range(1, number_of_tests + 1):
    print(f"*** Running Test Number: {test_number} ***")

    test_data = get_test_data(test_number)

    if "data" not in test_data:
      continue
    
    result = run(test_data["data"])
    
    is_correct = check_test_data(result, test_data["output"])
    if not is_correct:
      print(f"Failed test number: {test_number}")
      print(result)
