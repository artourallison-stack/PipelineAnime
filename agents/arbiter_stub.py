from agents.base import AgentBase

class ArbiterStub(AgentBase):
    def run(self, context):
        context.log("ArbiterStub: integrity OK, allowing next step")
        return True
