from Domains.Domain import Domain
from Model.Action import Action
from Model.Predicate import Predicate


class BlockWorldDomain(Domain):
    def __init__(self):
        # Initialize name, object types and actions for the domain
        self.name = "b Domain"
        self.object_type = {"block": [], "table": []}
        self.actions = []
        # Define the possible objects in the domain (tires and locations)
        self.define_objects()
        # Define the available actions in the domain
        self.define_actions()

    def define_objects(self):
        # Add two types of tires and two locations to the domain
        self.object_type["block"].append("a")
        self.object_type["block"].append("b")
        self.object_type["block"].append("c")
        self.object_type["block"].append("d")
        self.object_type["table"].append("table")

    def define_actions(self):
        clear_table = Predicate(
            "clear",
            [self.object_type["table"][0]],
        )
        # For each tire type, create remove and put actions for each location
        for block in self.object_type["block"]:
            # Define predicate for tire being on ground
            on_block_table = Predicate(
                "on",
                [block, self.object_type["table"][0]],
            )
            clear_block = Predicate(
                "clear",
                [block],
            )

            # For each location, create remove and put action
            for x in self.object_type["block"]:
                clear_x = Predicate(
                    "clear",
                    [x],
                )
                block_on_x = Predicate(
                    "on",
                    [block, x],
                )
                if x != block:
                    move_table_name = f"movetable({block}, {x})"
                    movetable_action = Action(
                        move_table_name,
                        [block_on_x,clear_block],
                        [],
                        [on_block_table,clear_x],
                        [block_on_x],
                    )
                    self.actions.append(movetable_action)
                for y in self.object_type["block"]:
                    clear_y = Predicate(
                        "clear",
                        [y],
                    )
                    block_on_y = Predicate(
                        "on",
                        [block, y],
                    )
                    if y != x and x != block and y!= block:
                        move_name = f"move({block}, {x}, {y})"
                        move_action = Action(
                            move_name,
                            [block_on_x,clear_block,clear_y],
                            [],
                            [block_on_y,clear_x],
                            [clear_y,block_on_x],
                        )
                        self.actions.append(move_action)
                    if block != y:
                        move_name = f"move({block}, table, {y})"
                        move_action = Action(
                            move_name,
                            [on_block_table,clear_block,clear_y],
                            [],
                            [block_on_y],
                            [clear_y,on_block_table],
                        )
                        self.actions.append(move_action)
