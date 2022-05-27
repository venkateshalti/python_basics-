# This module is called in module_import.py
def main():
    print("this function is directly called from its file, not from an import")



if __name__ == '__main__':
    main()
else:
    print("this is being called as a module inside a package in another program")