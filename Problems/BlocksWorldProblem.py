from Model.Predicate import Predicate
from Model.State import State
from Problems.Problem import Problem

class BlockWorldProblem(Problem):
    def __init__(self, domain):
        # Initialize a TireProblem object with a specified domain
        super().__init__(domain)

        # Define the predicates for the problem
        on_d_table = Predicate(
            "on",
            ["d", "table"],
        )
        clear_d = Predicate(
            "clear",
            ["d"],
        )
        on_c_table = Predicate(
            "on",
            ["c", "table"],
        )
        on_b_c = Predicate(
            "on",
            ["b", "c"],
        )
        on_a_b = Predicate(
            "on",
            ["a", "b"],
        )
        clear_a = Predicate(
            "clear",
            ["a"],
        )
        clear_a = Predicate(
            "clear",
            ["a"],
        )
        on_a_b = Predicate(
            "on",
            ["a", "b"],
        )
        on_b_d = Predicate(
            "on",
            ["b", "d"],
        )
        on_d_c = Predicate(
            "on",
            ["d", "c"],
        )
        # Create the initial and goal states using the defined predicates
        temp_initial_state = State("", [on_d_table, clear_d, on_c_table, on_b_c, on_a_b, clear_a], [])
        temp_goal_state = State("", [on_c_table, on_d_c, on_b_d, on_a_b, clear_a], [])

        # Set parent indices for the initial and goal states
        temp_initial_state.set_parent_index(-1)
        temp_goal_state.set_parent_index(-1)

        # Set the initial and goal states for the problem
        self.initial_state = temp_initial_state
        self.goal_state = temp_goal_state
