from PIL import Image, ImageDraw
from agents.base import AgentBase

class VisualGeneratorStub(AgentBase):
    def run(self, context):
        context.log("VisualGeneratorStub: generating placeholder image")

        img = Image.new("RGB", (512, 512), color=(235, 235, 235))
        draw = ImageDraw.Draw(img)

        draw.rectangle([100, 100, 412, 412], outline=(50, 50, 50), width=4)
        draw.text((140, 240), "OPENING FRAME\n(STUB)", fill=(0, 0, 0))

        return img
