import gradio as gr
from pipeline.controller import run_pipeline

def run():
    result, logs, status = run_pipeline()
    return result, "\n".join(logs), status

with gr.Blocks() as demo:
    gr.Markdown("## Pipeline v0 — Control Panel")

    run_btn = gr.Button("Run pipeline")

    output_image = gr.Image(label="Result (stub)")
    output_logs = gr.Textbox(label="Pipeline logs", lines=15)
    output_status = gr.Textbox(label="Police Engineer status")

    run_btn.click(fn=run, outputs=[output_image, output_logs, output_status])

if __name__ == "__main__":
    demo.launch()
