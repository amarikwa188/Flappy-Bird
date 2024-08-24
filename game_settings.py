# screen dimensions
screen_width: int = 700
screen_height: int = 400

# colors
bg_color: tuple[int,int,int] = (200,200,200)

# gameplay settings
## character stats
gravity: float = 0.25
flying: bool =  False
touching_ceiling: bool = False
last_touched: float = 0

## obstacle stats
bg_speed: float = 0.1
spawn_frequency: float = 2.0