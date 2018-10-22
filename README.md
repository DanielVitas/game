# Projektna naloga za UVP
Projekt za UVP

Potrebne knjiznice: pygame

  GAMEPLAY:
    Goal: Destroy all green rectangles.
    Mehanics: Shoot bullets that curve around gravity fields.

  BUILD MODE:
    W,A,S,D .............. move character
    TAB .............. lock/unlock camera
    1 .............. place obstacle
    2 .............. place shootable block (u can shoot, but cannot move through)
    3 .............. place target
    4 .............. place spawn (the character will spawn at it)
    MOUSE 1 .............. select (objects are considered 'selected' only while u are HOLDING the button)
    MOUSE 2 (scroller) .............. fire
    MOUSE 3 .............. gravity field
    DELETE .............. delete selected object
    - .............. zoom out
    = .............. zoom in
    ↑, ← .............. contract selected object
    ↓, → .............. stretch selected object
      SPACE .............. center camera on character

    While an object is selected it will move with your mouse.

    When clicking save you will be asked (in command prompt) to enter the level name, then your level will
    be saved in files\levels\*name*.txt

  PLAY MODE:
    W,A,S,D .............. move character
    TAB .............. lock/unlock camera
    MOUSE 1 .............. fire
    MOUSE 3 .............. gravity field
    DELETE .............. delete object hovered by your mouse (only gravity fields)
    - .............. zoom out
    = .............. zoom in
      SPACE .............. center camera on character

  OTHER:
    ESC .............. back/menu

    Key Bindings: To bind key to the action first HOLD the desired key and WHILE HOLDING the key press MOUSE1.
