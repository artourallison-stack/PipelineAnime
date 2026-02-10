import json
from PIL import Image, ImageDraw
from pipeline.context import PipelineContext
from pipeline.logger import log
from agents.visual_generator_stub import VisualGeneratorStub
from agents.arbiter_stub import ArbiterStub
from agents.police_engineer_stub import PoliceEngineerStub

def load_runtime():
    with open("config/runtime.json", "r") as f:
        return json.load(f)

def run_pipeline():
    runtime = load_runtime()
    context = PipelineContext(runtime)

    log(context, "Pipeline started")

    # Visual generation (stub)
    visual = VisualGeneratorStub()
    context.result = visual.run(context)

    # Arbiter (stub)
    arbiter = ArbiterStub()
    arbiter.run(context)

    # Police Engineer (stub)
    police = PoliceEngineerStub()
    status = police.run(context)

    log(context, "Pipeline finished")

    return context.result, context.logs, status
