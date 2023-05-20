class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

# Player instances
kevin = Player(
    name="Kevin Durant",
    age=34,
    position="small forward",
    team="Brooklyn Nets"
)

jason = Player(
    name="Jason Tatum",
    age=24,
    position="small forward",
    team="Boston Celtics"
)

kyrie = Player(
    name="Kyrie Irving",
    age=32,
    position="Point Guard",
    team="Brooklyn Nets"
)
class Player:
    def __init__(self, player_info):
        self.name = player_info['name']
        self.age = player_info['age']
        self.position = player_info['position']
        self.team = player_info['team']

# List of dictionaries
Player = [
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
]

# List of Player instances
Player_instances = []
for player_dict in Player:
    Player_instances.append(Player)
