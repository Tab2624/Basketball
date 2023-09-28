players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32,
        "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33,
        "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32,
        "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32,
        "position": "Point Guard", 
    "team": "Brooklyn Nets"
}
    


class Player:
    def __init__(self, player):
        self.name = player["name"]
        self.age = player["age"]
        self.position = player["position"]
        self.team = player["team"]


    def display_player(self):
        print(f"name: {self.name}- age: {self.age}- position: {self.position}- team: {self.team}")
    
    @classmethod
    def get_team(cls, new_list):
        player_list =[]
        for dict in new_list:
            player = cls(dict)
            player_list.append(player)
        return player_list
    
    @classmethod
    def get_info(cls, incoming_list, search):
        for info in incoming_list:
            if info.name == search:
                info.display_player()
        return cls
        

team = Player.get_team(players)
for player in team:
    player.display_player()
Player.get_info(team, "Joel Embiid")