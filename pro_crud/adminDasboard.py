import pro_crud as crud
from rich.panel import Panel
from rich.layout import Layout
from rich.text import Text
from rich.align import Align
from rich.console import Console
from rich.prompt import Prompt
import os

def mydashBoard():
    os.system("cls" if os.name == "nt" else "clear")
    console = Console()
    layout = Layout()

    layout.split(
        Layout(size=1, name="head"),
        Layout(ratio=1, name="main")
    )

    layout["main"].split_row(Layout(name="side"), Layout(name="sosialMedia", ratio=2))


    layout["side"].split(
        Layout(Panel(Align.center(Text("1.BUAT DATA", justify="center"), vertical="middle"),style="red bold")),
        Layout(Panel(Align.center(Text("2.BACA DATA", justify="center"), vertical="middle"),style="red bold")),
        Layout(Panel(Align.center(Text("3.UPDATE DATA", justify="center"), vertical="middle"),style="red bold")),
        Layout(Panel(Align.center(Text("4.HAPUS DATA", justify="center"), vertical="middle"),style="red bold")),
        
    )
    
    layout["head"].update("test")

    layout["sosialMedia"].update(
        Panel(Align.center(
            Text("""Github: https://github.com/Muhyari\nThank you\nHit Ctrl+C to exit""",justify="center")
        ,vertical="middle"),style="green")
    )


    console.print(layout)
    while True:
        userInput =  Prompt.ask("Pilihan [1-4]: ",default="none")
        if userInput == "none":
            continue
        elif userInput == "1":
            crud.database.createData()
        elif userInput == "2":
            crud.database.readData()
        elif userInput == "3":
            crud.database.updateData()
        elif userInput == "4":
            crud.database.deleteData()
        else:
            break