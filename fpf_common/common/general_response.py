class GeneralResponse:
    status: bool = False
    message: str
    errors: list = []
    map_response: dict = {}
    some_object = None

    def __init__(self, status: bool, message: str = None):
        self.status = status
        self.message = message

    def add_message(self, message):
        self.message = message
        return self

    def add_some_object(self, some_object):
        self.some_object = some_object
        return self

    def update_status(self, status: bool):
        self.status = status
        return self
