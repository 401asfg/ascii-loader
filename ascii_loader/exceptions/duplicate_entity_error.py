class DuplicateEntityError(Exception):
    """
    Raised on attempts to spawn the same instance of an entity in a room when 
    it is already contained within that room
    """
    pass
