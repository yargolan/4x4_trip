class FileStructureError(Exception):
    """Exception raised for errors in the input file."""

    def __init__(self, message="The request file structure is wrong."):
        self.message = message
        super().__init__(self.message)
