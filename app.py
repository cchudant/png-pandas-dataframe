import gradio as gr

from extract_pandas_dataframe import extract

def convert(file):
    extract(file, 'output.csv')
    return 'output.csv'

demo = gr.Interface(convert, "file", "file")
demo.launch()
