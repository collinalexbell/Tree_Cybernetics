from rich import print
from rich.console import Console

print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())

console = Console()
console.rule("[bold red]Treelon")
console.print([1,2,3])
