class Player:

    def __init__(self, dict):
        self.name = dict["name"]
        self.age = dict["age"]
        self.position = dict["position"]
        self.team = dict["team"]

    def display_info(self):
        print(f"Name : {self.name}")
        print(f"Age: {self.age}")
        print(f"Position: {self.position}")
        print(f"Team: {self.team} \n")

    def __repr__(self):
        return f"Player Name: {self.name}\n"

    @classmethod
    def get_team(cls, team_list):
        new_list = []
        for player in team_list:
            new_list.append(Player(player))
        return new_list

    @classmethod
    def display_team_players_info(cls, team_list):
        for player in team_list:
            player.display_info()



kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving",
    "age": 32,
    "position": "Point Guard",
    "team": "Brooklyn Nets"
}


players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32,
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

kev = Player(kevin)
jas = Player(jason)
kyr = Player(kyrie)

kev.display_info()
jas.display_info()
kyr.display_info()

# new_team = []


# for i in players:
#     new_team.append(Player(i))


# for i in new_team:
#     i.display_info()

new_Team = Player.get_team(players)

Player.display_team_players_info(new_Team)