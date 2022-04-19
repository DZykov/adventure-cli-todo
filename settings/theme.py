class Color:


    def __init__(self):
        self.colors = {
            'PURPLE': '\033[95m',
            'CYAN': '\033[96m',
            'DARKCYAN': '\033[36m',
            'BLUE': '\033[94m',
            'GREEN': '\033[32;1m',
            'YELLOW': '\033[93m',
            'RED': '\033[91m',
            'BOLD': '\033[1m',
            'ITALIC': '\033[3m',
            'UNDERLINE': '\033[4m'
        }
        self.end = '\033[0m'
        self.text = {
            'WARNING': self.colors['RED'] + self.colors['BOLD'],
            'ADVENTURE': self.colors['PURPLE'] + self.colors['ITALIC'] + self.colors['BOLD'],
            'MISSION': self.colors['DARKCYAN'] + self.colors['BOLD'],
            'TEXT': "",
        }
        self.check = '✓'
        self.cross = '✗'
        self.error = '?'
    
    def print_text(self, text, options):
        print(self.return_text(text, options))
    
    def return_text(self, text, options):
        style = ""
        for option in options:
            if option in self.colors:
                style += self.colors[option]
            if option in self.text:
                style += self.text[option]
        return "{}{}{}".format(style, text, self.end)
