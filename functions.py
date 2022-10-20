import time


def slowPrint(text, delay):
    """
   Makes the strings slower by a certain amount of time
    """
    print(text)
    time.sleep(delay)