import modules.scripts as scripts
import gradio as gr
import os

from modules import script_callbacks


def load_note():
    
    path = os.path.join(scripts.basedir(), "extensions", "sd-webui-hotarunote", "data", "hotarunote.txt")
    if not os.path.exists(path):
        f = open(path, 'w')
        f.close()

    f = open(path, 'r')
    txt = f.read()
    f.close()

    return txt


def save_note(notetextarea):
    
    path = os.path.join(scripts.basedir(), "extensions", "sd-webui-hotarunote", "data", "hotarunote.txt")
    f = open(path, 'w')
    f.write(notetextarea)
    f.close()


def on_ui_tabs():
    
    # Create data directory
    path = os.path.join(scripts.basedir(), "extensions", "sd-webui-hotarunote", "data")
    if not os.path.exists(path):
        os.makedirs(path)    

    # Setup UI
    with gr.Blocks(analytics_enabled=False) as ui_component:

        notetextarea = gr.Textbox(value=load_note(), interactive=True, lines=20, max_lines=200)
        savebutton =gr.Button(value="Save")        
        loadbutton =gr.Button(value="Load")        

        savebutton.click(fn=save_note, inputs=[notetextarea])
        loadbutton.click(fn=load_note, outputs=[notetextarea])

        return [(ui_component, "HotaruNote", "hotarunote")]

script_callbacks.on_ui_tabs(on_ui_tabs)
