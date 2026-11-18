def shell_loop():
    """Main interactive loop of PyOsX."""

    print("Welcome to PyOsX!")
    print("Type Ctrl+D to exit.")

    while True:
        try:
            # 1. Display the prompt and read user input
            command = input("pyosx> ")

            # 2. Ignore empty commands
            if not command.strip():
                continue

            # 3. Temporary output for testing the REPL
            print(f"Command received: {command}")

        except KeyboardInterrupt:
            # Ctrl+C: return to the prompt
            print("\nUse Ctrl+D to exit.")

        except EOFError:
            # Ctrl+D: exit the shell
            print("\nGoodbye!")
            break
