class Handler:
    def __init__(self):
        self.colliders = []

    # TODO: Revisar colisiones dependiendo del tipo de collider que tenga
    def update(self):
        for col in self.colliders:
            for other in self.colliders:
                if other == col:
                    continue
                else:
                    col.is_colliding(other) # TODO: Hacer que se choque cuando colisione
