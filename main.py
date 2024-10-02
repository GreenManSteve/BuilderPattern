from director.director import Director
from products.accer import Accer
from products.mac import Mac

# Director accepts Mac() or Accer()

computer_builder = Director(Mac())
computer_builder.build_computer()
computer = computer_builder.get_computer()
computer.display()