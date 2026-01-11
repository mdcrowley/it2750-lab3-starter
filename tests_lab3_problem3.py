######################################
## WARNING! DO NOT MODIFY THIS FILE ##
######################################

import os.path
import sys
import unittest
import random

test_file = "lab3_problem3"
test_inputs = [random.randint(9, 50), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]

if(sum(test_inputs[1:4]) == 0): test_inputs[1] = test_inputs[3] = 1

def test(monkeypatch, capsys):
    global test_file
    global test_inputs
    try:
        exists = os.path.exists(test_file + '.py')
        assert exists == True
        source = __import__(test_file)
    except:
        sys.exit()
    if len(test_inputs) > 0:
        inputs = iter(test_inputs)
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    regexChars = ""
    if test_inputs[1] == 1: regexChars += 'A-Z'
    if test_inputs[2] == 1: regexChars += 'a-z'
    if test_inputs[3] == 1: regexChars += '0-9'

    tc = unittest.TestCase()

    # Test: Generated password function works with test inputs
    gp_result = source.generatePassword(test_inputs[0], test_inputs[1], test_inputs[2], test_inputs[3])
    tc.assertRegex(gp_result, '^[' + regexChars + ']{' + str(test_inputs[0]) + '}$')

    source.main()
    captured = capsys.readouterr()
    output = captured.out.split('\n')
    output.pop() # Remove last blank line since split by \n
    
    # Test: Ensure 2 lines of output
    assert len(output) == 2
    
    # Test: Ensure password generation via stdin works
    tc.assertRegex(output[1], '^[' + regexChars + ']{' + str(test_inputs[0]) + '}$')

######################################
## WARNING! DO NOT MODIFY THIS FILE ##
######################################