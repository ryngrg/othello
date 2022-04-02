class AI_Agent:
    def __init__(self, player, depth=5):
        self.player = player
        self.max_depth = depth

    def get_move(self, game):
        board, player, n_moves, moves = game.get_curr_info()
        if player == self.player and n_moves > 0:
            if player == 1:
                best_score = None
                for i in range(n_moves):
                    child = game.copy()
                    child.make_move(i)
                    score = self.minimax(child, 1, False)
                    if best_score is None or score > best_score:
                        best = i
                        best_score = score
                    del child
            else:
                best_score = None
                for i in range(n_moves):
                    child = game.copy()
                    child.make_move(i)
                    score = self.minimax(child, 1, True)
                    if best_score is None or score < best_score:
                        best = i
                        best_score = score
                    del child
            return best
        else:
            return None

    def minimax(self, game, depth, is_max):
        if game.end or depth >= self.max_depth:
            return self.heuristic(game, depth)
        if is_max:
            pass
        else:
            pass
        return 0

    @staticmethod
    def heuristic(game, depth):
        if game.end:
            if game.winner == 0:
                return 0
            elif game.winner == 1:
                return 10000
            elif game.winner == 2:
                return -10000
        return 20 * (game.count(1) - game.count(2)) - (5 * depth)
