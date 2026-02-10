from agents.base import AgentBase

class PoliceEngineerStub(AgentBase):
    def run(self, context):
        context.log("PoliceEngineerStub: pipeline OK, no block")
        return "OK"
