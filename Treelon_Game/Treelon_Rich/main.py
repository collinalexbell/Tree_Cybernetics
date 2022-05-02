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
    def __init__(self, name, north_value, description = ""):
        super().__init__(name)
        self.north_value = north_value
        self.description = description
    def print(self):
        console.print("place ", self.name)
        console.print("   at north value: ", self.north_value, "\n    ", self.description)

class U:
    def __init__(self):
        self.things = []
        self.places = []
        self.cur_place = None
    def add(self, things):
        self.things.extend(things)
    def add_place(self, place):
        self.things.append(place)
        self.places.append(place)
        self.cur_place = place
    def print_places(self):
        console.rule("[bold purple]<Places>")
        for place in self.places:
            place.print()
        console.rule("[bold purple]</Places>")
    def stroke(self):
        console.print("You are at: ")
        if(self.cur_place != None):
            console.print(self.cur_place.print())
        U_.print_places()
        choice = int(console.input("Choose a place to visit:"))
        if(choice >= 0 and choice < len(self.places)):
            self.cur_place = self.places[choice]
        return choice


U_ = U()

collin = I("collin")
zeus = I("zeus")
onix = I("onlix")
U_.add([collin, zeus, onix])
U_.add_place(Place("gold st hotel", 0, "a high powered man's getaway in the heart of the financial district"))
U_.add_place(Place("56 leonard", 1, "where princesses live"))
U_.add_place(Place("roxy hotel", 2, "hacker's paradise"))
U_.add_place(Place("31 st hotel", 3, "shithole"))
U_.add_place(Place("46 st hotel", 4, "jury is still out on this hotel. the neighborhood seems great."))
U_.add_place(Place("central park tower", 5, "A gorgeously tall residential tower"))

choice = 999
while(choice != -1):
    choice = U_.stroke()

console.print("[bold magenta]Holons:[/bold magenta]", U_.things)
