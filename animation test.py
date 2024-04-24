while True: 
    animation_index = 0
    frames = [1,2]

    animation_index += 0.1
    if animation_index >= len(frames):
        animation_index = 0
    else:
        image = frames[int(animation_index)]
        
    print (frames)
    print (animation_index)