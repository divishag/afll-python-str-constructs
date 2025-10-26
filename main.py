# main.py
from lexer import lexer
from parser import parser

def print_header():
    print("=" * 60)
    print("    Python String Method Syntax Validator")
    print("    Using Context-Free Grammar (PLY Tools)")
    print("=" * 60)
    print()

def print_examples():
    print("Supported Methods:")
    print("  • upper()                  - Convert to uppercase")
    print("  • replace(old, new)        - Replace all occurrences")
    print("  • replace(old, new, count) - Replace with limit")
    print()

def main():
    print_header()
    print_examples()
    
    print("Examples:")
    print('  myStr.upper()')
    print('  word.replace("a", "b")')
    print('  text.replace("old", "new", 3)')
    print()
    
    while True:
        try:
            data = input("Enter statement (or 'quit' to exit): ").strip()
            
            if not data:
                continue
                
            if data.lower() in ['quit', 'exit', 'q']:
                print("\nGoodbye!")
                break
                
        except (EOFError, KeyboardInterrupt):
            print("\n\nExiting...")
            break

        print(f"\nProcessing: {data}")
        print("-" * 60)
        
        parser.success = True
        result = parser.parse(data, lexer=lexer, debug=False)

        if parser.success:
            print(f"\n>>> Status: ACCEPTED\n")
        else:
            print(f"\n>>> Status: REJECTED\n")

if __name__ == "__main__":
    main()
