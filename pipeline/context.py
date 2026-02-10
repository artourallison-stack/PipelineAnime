class PipelineContext:
    def __init__(self, runtime_config):
        self.runtime = runtime_config
        self.logs = []
        self.result = None

    def log(self, message):
        self.logs.append(message)
