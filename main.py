#soundLevel = input.sound_level()
#lightLevel = input.light_level()
#rotation = input.rotation(Rotation.PITCH)
#accelX = input.acceleration(Dimension.X)
#accelY = input.acceleration(Dimension.X)
#accelZ = input.acceleration(Dimension.X)


while True:
    #print("Rotation " + rotation)
    #print("accelZ " + accelX)
    '''   
    #Sound Measurements
    print("Sound Level: " + soundLevel)
    if soundLevel >= 32:
        light.set_all(light.rgb(255,0,0))
        music.ba_ding.play_until_done()
    else:
        light.show_animation(light.rainbowAnimation, 500)
    '''
    #Temperature Measurements
    print("Temperature: " + tempF)
    if tempF >= 65:
        light.set_all(light.rgb(255,0,0))
    elif tempF >= 55:
        light.set_all(light.rgb(0,255,0))
    else:
        light.set_all(light.rgb(0,0,255))
  
    '''
    #Light Measurements
    print("Light Level: " + lightLevel)
    if lightLevel >= 200:
        light.clear()
    else:
        light.set_all(light.rgb(255,255,255))
    '''


