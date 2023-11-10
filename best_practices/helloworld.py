import sys

class CustomException(Exception):
    def __init__(self, message=None, code=None):
        self.message = message
        self.code = code
    def __str__(self):
        return f"{self.message}, {self.code}"

def pay_respects(arg):
    try:
        if arg != "F":
            raise CustomException("Error: No respects paid", 999)
        else:
            print("Hello world!")
    except CustomException as e:
        print(e)    
    print("Program end")

if __name__ == "__main__":
    # sys.argv = command line array
    if len(sys.argv) == 2:
        pay_respects(sys.argv[1])
    else:
        print("usage: python3 helloworld.py <input>")
