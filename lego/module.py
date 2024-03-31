import time

def connect() -> None:
    print("Working... (waiting for 5 seconds)")
    time.sleep(5)
    print("Done job!")

# Only Run if the current module is executed manually
# like 
# $python module.py
if __name__ == "__main__":
    connect()