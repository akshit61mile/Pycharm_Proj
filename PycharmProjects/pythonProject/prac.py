
import PySimpleGUI as s

def loo(km):
    return km/1.6


km_text = s.Text("Enter kilometers")
km_input = s.Input(key="km")
convert_button = s.Button("Convert")
output_label = s.Text("",key = "output")

window = s.Window("Km to Miles Convertor",layout =[[km_text,km_input],
                                                   [convert_button]],font =('Helvetica',20))

while True:
    events,values = window.read()
    match events:
        case"Covert":

            km = float(values["km"])
            result = loo(km)
            window["output"].update(value=km,text_clor ="white")
            break

window.close()



