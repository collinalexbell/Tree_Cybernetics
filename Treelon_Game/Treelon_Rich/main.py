from rich import print
from rich.console import Console

console = Console()
console.rule("[bold red]Treelon")
console.print("[bold magenta]Treelon[/bold magenta]!", locals())
console.print([1,2,3])
