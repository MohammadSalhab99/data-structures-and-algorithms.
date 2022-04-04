from stack_queue_brackets.StackQueueBrackets import validateBrackets
print(validateBrackets("{}"))
print(validateBrackets(""))
print(validateBrackets("()[[Extra Characters]]"))
print(validateBrackets("(){}[[]]"))
print(validateBrackets("{}{Code}[Fellows](())"))
print(validateBrackets("[({})]"))
print(validateBrackets("(]("))
print(validateBrackets("{(})"))


def test_1():
    actual = validateBrackets("{}")
    expected = True
    assert actual == expected
def test_2():
    actual = validateBrackets("{}(){}")
    expected = True
    assert actual == expected
def test_3():
    actual = validateBrackets("())[[Extra Characters]]")
    expected = True
    assert actual == expected
def test_4():
    actual = validateBrackets("(){}[[]]")
    expected = True
    assert actual == expected
    
def test_5():
    actual = validateBrackets("[({}]")
    expected = False
    assert actual == expected
def test_6():
    actual = validateBrackets("(](")
    expected = False
    assert actual == expected
def test_7():
    actual = validateBrackets("{(})")
    expected = True
    assert actual == expected
