class AI_Agent:
    def __init__(self, player):
        self.player = player

    def get_move(self, board, player, n_moves, moves):
        if player == self.player:
            return 0
        else:
            return None
