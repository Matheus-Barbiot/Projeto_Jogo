import bge

def main(cont):
    own = cont.owner
    over = cont.sensors["Mouse"]
    
    if over.positive:
        hitPos = over.hitPosition
        own.worldPosition = hitPos
        own.worldPosition.z += 0.2
