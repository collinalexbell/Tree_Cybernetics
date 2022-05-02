from rich import print
from rich.console import Console

console = Console()
console.rule("[bold red]Treelon")
console.print("[bold magenta]Treelon[/bold magenta]!", locals())
console.print([1,2,3], "[bold red]GO![/bold red]")

class I:
    def __init__(self, name):
        self.name = name

class Place(I):
    def __init__(self, name, north_value):
        super().__init__(name)
        self.north_value = north_value
    def print(self):
        console.print("place ", self.name)
        console.print("   at north value: ", self.north_value)

class U:
    def __init__(self):
        self.things = []
        self.places = []
    def add(self, things):
        self.things.extend(things)
    def add_place(self, place):
        self.things.append(place)
        self.places.append(place)
    def print_places(self):
        console.rule("[bold purple]<Places>")
        for place in self.places:
            place.print()
        console.rule("[bold purple]</Places>")

U_ = U()

collin = I("collin")
zeus = I("zeus")
onix = I("onlix")
U_.add([collin, zeus, onix])
U_.add_place(Place("central park tower", 5))
U_.add_place(Place("46 st hotel", 4))
U_.add_place(Place("31 st hotel", 3))
U_.add_place(Place("roxy hotel", 2))
U_.add_place(Place("56 leonard", 1))
U_.add_place(Place("gold st hotel", 0))

U_.print_places()

console.print("[bold magenta]Holons:[/bold magenta]", U_.things)
