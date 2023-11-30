import modules.scripts as scripts
#from pathlib import Path
#import platform
import gradio as gr
import os
#import pathlib
#import glob
#import re

from modules import script_callbacks

def load_note():
    
    filename = "hotarunote.txt"
    path = os.path.join(scripts.basedir(), "extensions", "sd-webui-hotarunote", "data", filename)
    if not os.path.exists(path):
        f = open(path, 'w')
        f.close()

    f = open(path, 'r')
    txt = f.read()
    f.close()

    return txt


def save_note(notetextarea):
    
    filename = "hotarunote.txt"
    path = os.path.join(scripts.basedir(), "extensions", "sd-webui-hotarunote", "data", filename)
    f = open(path, 'w')
    f.write(notetextarea)
    f.close()


def create_dir():
    path = os.path.join(scripts.basedir(), "extensions", "sd-webui-hotarunote", "data")
    if not os.path.exists(path):
        os.makedirs(path)    


def on_ui_tabs():
    create_dir()

    with gr.Blocks(analytics_enabled=False) as ui_component:

        notetextarea = gr.Textbox(value=load_note(), interactive=True, lines=20, max_lines=200)
        savebutton =gr.Button(value="Save")        
        loadbutton =gr.Button(value="Load")        

        savebutton.click(fn=save_note, inputs=[notetextarea])
        loadbutton.click(fn=load_note, outputs=[notetextarea])

        return [(ui_component, "HotaruNote", "hotarunote")]

script_callbacks.on_ui_tabs(on_ui_tabs)
