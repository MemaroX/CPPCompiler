class TopDownParser:
    def __init__(self):
        self.grammar = {}

    # Adding rules dynamically
    def add_rule(self, non_terminal, rule):
        if non_terminal not in self.grammar:
            self.grammar[non_terminal] = []
        self.grammar[non_terminal].append(rule)

    # Checking if the grammar is "simple"
    def is_simple(self):
        for non_terminal, rules in self.grammar.items():
            first_terminals = set()
            for rule in rules:
                first_symbol = rule[0]  # Take the first symbol in the rule
                if first_symbol.isupper():  # Non-terminal symbols are not allowed to start the rule
                    print(f"Invalid rule for non-terminal {non_terminal}: Rule starts with non-terminal '{first_symbol}'")
                    return False
                elif first_symbol in first_terminals:  # If a rule starts with the same terminal symbol
                    print(f"Invalid rules for non-terminal {non_terminal}: Rules start with the same terminal '{first_symbol}'")
                    return False
                first_terminals.add(first_symbol)
        return True

    # Parsing a string using Top-Down Parsing
    def parse(self, string, start_symbol):
        return self._parse_recursive(string, start_symbol, 0)

    def _parse_recursive(self, string, current_symbol, index):
        if index >= len(string):
            return index if current_symbol == "" else -1

        if current_symbol.islower():  # If it's a terminal symbol
            if string[index] == current_symbol:
                return index + 1
            return -1

        if current_symbol.isupper():  # If it's a non-terminal symbol
            if current_symbol in self.grammar:
                for rule in self.grammar[current_symbol]:
                    index_new = index
                    for symbol in rule:
                        result = self._parse_recursive(string, symbol, index_new)
                        if result == -1:
                            break
                        index_new = result
                    if index_new != index:
                        return index_new
            return -1

# Main program
if __name__ == "__main__":
    parser = TopDownParser()

    while True:
        print("\nMenu:")
        print("1. Add Grammar Rules")
        print("2. Check if Grammar is Simple")
        print("3. Parse a String")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            non_terminal = input("Enter non-terminal: ")
            rule_count = int(input(f"Enter number of rules for non-terminal '{non_terminal}': "))
            for i in range(rule_count):
                rule = input(f"Enter rule number {i + 1} for non-terminal '{non_terminal}': ")
                parser.add_rule(non_terminal, rule)

        elif choice == "2":
            if parser.is_simple():
                print("The Grammar is Simple.")
            else:
                print("The Grammar isn't Simple.")

        elif choice == "3":
            start_symbol = input("Enter start symbol: ")
            string = input("Enter string to parse: ")
            if parser.parse(string, start_symbol) != -1:
                print(f"String '{string}' is Accepted")
            else:
                print(f"String '{string}' is Rejected")

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")
