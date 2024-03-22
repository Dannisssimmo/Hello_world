def linux_proverka():
    import sys
    assert ('linux' in sys.platform), "This code runs on Linux only."
    print('doing something')
try:
    linux_proverka()
except AssertionError as error:
    print(error)
    print("The linux_interaction() function was not executed")
print('huilo')
