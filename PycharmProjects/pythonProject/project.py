
import PySimpleGUI as s
s.theme("Black")

label1 = s.Text("Select archive")
input1 = s.Input()
choose_button1 = s.FilesBrowse("Choose",key="archive")

label2 = s.Text("Select dest dir")
input2 = s.Input()
choose_button2 = s.FolderBrowse("Choose",key="folder")

extract_button = s.Button("Extract")
output_label = s.Text(key="output", text_color="green")

window = s.Window("Archive Extractor",layout=[[label1,input1,choose_button1],
                                              [label2,input2,choose_button2],
                                              [extract_button,output_label]])
while True:
    event,values = window.read()
    print(event,values)
    archivepath = values["archive"]
    dest_dir = values["folder"]
    extract_archive(archivepath,dest_dir)
    window["output"].update(value="extraction completed")

window.close()



