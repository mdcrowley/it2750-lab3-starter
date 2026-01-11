######################################
## WARNING! DO NOT MODIFY THIS FILE ##
######################################

import os.path
import sys
import unittest
import string
import random

test_file = "lab3_problem2"
test_inputs = [random.randint(9, 50)]

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

    source.main()
    captured = capsys.readouterr()
    output = captured.out.split('\n')
    output.pop() # Remove last blank line since split by \n

    tc = unittest.TestCase()
    
    # Test: Ensure 3 lines of output
    assert len(output) == 3, "Incorrect number of output lines"

    # Test: The chars variable matches requirements
    assert(output[1] == string.ascii_uppercase + string.ascii_lowercase + string.digits), "The chars variable does not contain correct characters"
    
    # Test: Ensure the string matches the possible chars and length
    tc.assertRegex(output[2], '^[A-Za-z0-9]{' + str(test_inputs[0]) + '}$'), "Result string does not match length requested or does not contain correct characters"

######################################
## WARNING! DO NOT MODIFY THIS FILE ##
######################################