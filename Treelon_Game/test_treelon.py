import Treelon

# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4
    
def test_Sprite():
    class Mock_Screen:
        def __init__(self):
            pass
        def blit(self, sprite_surf, position):
            self.sprite_surf = sprite_surf
            self.position = position
    mock_screen = Mock_Screen()
    mock_sprite_surf = "mock_sprite_surf"
    mock_x = 13
    mock_y = 42
    sprite = Treelon.Sprite(mock_screen, mock_sprite_surf, mock_x, mock_y)
    sprite.render()
    
    assert mock_screen.sprite_surf == mock_sprite_surf
    assert mock_screen.position == (mock_x * Treelon.TILE_SIZE, mock_y * Treelon.TILE_SIZE)
    
def test_treegame_import():
    import treegame
        
        
   
