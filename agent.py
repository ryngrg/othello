import math
import copy


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
                    child = copy.deepcopy(game)
                    child.make_move(i)
                    score = self.minimax(child, 1, -math.inf, math.inf, False)
                    if best_score is None or score > best_score:
                        best = i
                        best_score = score
                    del child
            else:
                best_score = None
                for i in range(n_moves):
                    child = copy.deepcopy(game)
                    child.make_move(i)
                    score = self.minimax(child, 1, -math.inf, math.inf, True)
                    if best_score is None or score < best_score:
                        best = i
                        best_score = score
                    del child
            return best
        else:
            return None

    def minimax(self, game, depth, alpha, beta, is_max):
        if game.end or depth >= self.max_depth:
            return self.heuristic(game, depth, is_max)
        if is_max:
            val = -math.inf
            for i in range(game.n_moves):
                ch = copy.deepcopy(game)
                ch.make_move(i)
                val = max(val, self.minimax(ch, depth+1, alpha, beta, False))
                alpha = max(alpha, val)
                if val >= beta:
                    break
        else:
            val = math.inf
            for i in range(game.n_moves):
                ch = copy.deepcopy(game)
                ch.make_move(i)
                val = min(val, self.minimax(ch, depth+1, alpha, beta, True))
                beta = min(beta, val)
                if val <= alpha:
                    break
        return val

    @staticmethod
    def heuristic(game, depth, is_max):
        if game.end:
            if game.winner == 0:
                return 0
            elif game.winner == 1:
                return 10000
            elif game.winner == 2:
                return -10000
        elif is_max:
            return 20 * (game.count(1) - game.count(2)) - (5 * depth)
        return 20 * (game.count(1) - game.count(2)) + (5 * depth)
