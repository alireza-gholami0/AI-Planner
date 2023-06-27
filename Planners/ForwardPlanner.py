from queue import Queue
from Planners.Planner import Planner

"""
result is a list that stores the sequence of actions needed to reach the goal state, in case the planner finds a solution.

frontier is a queue data structure that stores the indices of states that need to be expanded. It follows the First-In-First-Out (FIFO) rule, meaning that the first state that was added to the queue will be the first one to be explored.

all_states is a list that stores all the states that have been generated during the search process, including both the initial state and any successor states that were created. The index of each state in this list represents its unique identifier.

visited is a set that stores all the states that have already been visited during the search process. If a state has already been visited, it will not be added to either the frontier or all_states again. This helps to prevent the algorithm from revisiting the same states multiple times and getting stuck in a loop

"""





class ForwardPlanner(Planner):
    def __init__(self, problem):
        super().__init__(problem)



    def successor(self, state, current_state_index):
        result = []
        # Get all possible actions

        for action in self.problem.get_domain().get_actions():
            # Check if action is applicable to state
            if action.is_applicable(state):
                new_state = action.progress(state)
                # Set parent state index and action
                cost = 0
                for p in self.problem.get_goal_state().positive_literals:
                    if p not in action.progress1(state).positive_literals:
                        cost += 1
                new_state.heuristic = cost
                new_state.set_parent_index(current_state_index)
                result.append(new_state)

        return result

    def build_solution(self, state, all_states):
        result = []

        # Find goal state index
        while state.get_parent_index() != -1:
            result.append(state.get_action_name())
            state = all_states[state.get_parent_index()]
        result.reverse()
        return result

    def goal_test(self, state):
        goal = self.problem.get_goal_state()
        return goal.get_positive_literals().issubset(
            state.get_positive_literals()
        ) and state.get_negative_literals().isdisjoint(goal.get_positive_literals())
