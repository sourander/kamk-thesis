import os

class PathMerger:
    """Class for generating staging and bronze paths."""

    # Settings that should be loaded from a settings file
    container = 'S3'
    src_prefix = 'staging'
    brz_prefix = 'bronze'
    tool = 'dms'
    ss = 'company_rds'

    # Paths. These will be populated during class init.
    staging = None
    bronze = None

    def __init__(self, db, table):
        # Fetch input
        self.db = db
        self.table = table

        # Populate path variables
        self.generate_paths()

    def generate_paths(self):
        self.staging = os.path.join(self.container, self.src_prefix, self.tool, self.ss, self.db, self.table)
        self.bronze = os.path.join(self.container, self.brz_prefix, self.ss, self.db, self.table)