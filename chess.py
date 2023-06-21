class Branch:
    
    def __init__(self):
        self.branches = []

class Game:

    def __init__(self)
        self.line = [] #contains turns.
    
    def __eq__(self, move ):
        return move ==self.move

    def add_line(self, moves_string):
        """
        Extract the moves from a string and add them to the game's line.
        :param moves_string: String containing moves separated by spaces.
        """ 
        moves_list = moves_string.strip().split()
        turn = 1
        for i in range(0, len(moves_list), 2):
            white _move = moves_list[i]
            black_move = moves_list[i + 1] if i + 1 < len(moves_list) else None
            new_move = Move(white_move, black_move, turn)
            self.line.appent(new_move)
            turn += 1

    def load_from_json(self, json_file):
        """
        Load game data from a JSON file and add the moves to the game's line.
        :param json_file: Path to the JSON file.
        """
        with open(json_file) as f:
            data = json.load(f)
        for game_data in data:
            moves_string = game_data['moves']
            self.add_line(moves_string)
    
    game = Game()
    game.load_from_json('jsonpath')