class Lockable:
    def __init__(self):
        self._locked = False

    def lock(self):
        self._locked = True

    def unlock(self):
        self._locked = False

    def is_locked(self):
        return self._locked

    def _check_locked(self):
        if self._locked:
            raise PermissionError("Account is locked")
