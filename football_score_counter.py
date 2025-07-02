class football:
    def __init__(self,team_name,target=3):
        self.team_name=team_name
        self.target=target
    def score(self):
        if self.target <= 1:
            print(f"{self.team_name} wins!")
       
        else:
            self.target-=1
            print(f"{self.team_name} needs {self.target} goals to win!")
Barcelona=football("Barcelona")
Madrid=football("Madrid")
Barcelona.score()
Madrid.score()
Barcelona.score()
Barcelona.score()
