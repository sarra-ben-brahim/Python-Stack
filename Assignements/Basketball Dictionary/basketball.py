class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.age = dict['age']
        self.position = dict['position']
        self.team = dict['team']
        
    @classmethod
    def get_team(cls, team_list):
        player_objects = []
        for player in team_list:
            player_objects.append(cls(player))
        return player_objects
    
        
        

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
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}
    
# Create your Player instances here!
# player_jason = ???

player_jason = Player(jason)
player_kevin = Player(kevin)
player_kyrie = Player(kyrie)
print(player_jason.name, "," , player_jason.age, ",", player_jason.position, ",", player_jason.team)
print(player_kevin.name, "," , player_kevin.age, ",", player_kevin.position, ",", player_kevin.team)
print(player_kyrie.name, "," , player_kyrie.age, ",", player_kyrie.position, ",", player_kyrie.team)


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
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "", 
    	"age":16, 
    	"position": "P", 
    	"team": "en"
    }
]

new_team = []

for player in players:
    plyr = Player(player)
    new_team.append(player)
    

print(new_team)