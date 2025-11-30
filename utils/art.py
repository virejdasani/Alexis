class Art:
    def draw_ascii_art(self, command):
        """Draws ASCII art based on user input."""
        try:
            return self.generate_custom_text_art(command)
        except NameError:
            return "Invalid command. Try 'square', 'triangle', 'circle', or 'custom'."
        

    def generate_custom_text_art(self, text):
        """Generates ASCII art for custom text using pyfiglet."""
        try:
            import pyfiglet
            ascii_art = pyfiglet.figlet_format(text)
            return ascii_art
        except ImportError:
            return "pyfiglet module not installed. Run 'pip install pyfiglet' to enable custom text art."

    # Example usage
    def make_art(self):
        print("Welcome to the ASCII Art Drawer!")
        while True:
            command = input("\nEnter the shape to draw (or 'exit' to quit): ").strip().lower()
            if command == "exit":
                print("Goodbye!")
                break
            print(self.draw_ascii_art(command))
