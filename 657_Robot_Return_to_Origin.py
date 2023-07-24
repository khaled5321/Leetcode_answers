class Solution:
    def judgeCircle(self, moves: str) -> bool:
        origin = [
            moves.count('R') - moves.count('L'),
            moves.count('U') - moves.count('D')
        ]
            
        return False if any(origin) else True
