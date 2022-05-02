from rich import print
from rich.console import Console

console = Console()
console.rule("[bold red]Treelon")
console.print("[bold magenta]Treelon[/bold magenta]!", locals())
console.print([1,2,3], "[bold red]GO![/bold red]")

class I:
    def __init__(self, name):
        self.name = name

class U:
    def __init__(self):
        self.things = []
    def add(self, things):
        self.things.extend(things)


U_ = U()

collin = I("collin")
zeus = I("zeus")
onix = I("onlix")
U_.add([collin, zeus, onix])

console.print("[bold magenta]Holons:[/bold magenta]", U_.things)
