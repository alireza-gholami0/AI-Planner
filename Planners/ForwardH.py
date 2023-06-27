from queue import Queue
from Planners.Planner import Planner
from Planners.PriorityQueue import PriorityQueue
"""
result is a list that stores the sequence of actions needed to reach the goal state, in case the planner finds a solution.

frontier is a queue data structure that stores the indices of states that need to be expanded. It follows the First-In-First-Out (FIFO) rule, meaning that the first state that was added to the queue will be the first one to be explored.

all_states is a list that stores all the states that have been generated during the search process, including both the initial state and any successor states that were created. The index of each state in this list represents its unique identifier.

visited is a set that stores all the states that have already been visited during the search process. If a state has already been visited, it will not be added to either the frontier or all_states again. This helps to prevent the algorithm from revisiting the same states multiple times and getting stuck in a loop

"""





class ForwardH(Planner):
    def __init__(self, problem):
        super().__init__(problem)

    def search(self):
        total_state_index = 0
        result = []
        frontier = PriorityQueue();
        visited = set()
        all_states = []

        # Check if goal state is already reached
        if self.goal_test(self.problem.get_initial_state()):
            return result

        # Add initial state to frontier and visited set
        frontier.enqueue_with_priority(-self.searchH(self.problem.get_initial_state()),total_state_index)
        visited.add(self.problem.get_initial_state())
        all_states.append(self.problem.get_initial_state())

        while frontier.size >= 1:
            current_state_index = frontier.dequeue()
            current_state = all_states[current_state_index]

            # Generate successor states
            successor_states = self.successor(current_state, current_state_index)

            for successor_state in successor_states:
                # If goal state is found, build solution and return
                if self.goal_test(successor_state):
                    result = self.build_solution(successor_state, all_states)
                    return result

                # Add successor state to frontier and visited set
                if successor_state not in visited:
                    total_state_index += 1
                    successor_state.heuristic = self.searchH(successor_state)
                    frontier.enqueue_with_priority(-successor_state.heuristic,total_state_index)
                    visited.add(successor_state)
                    all_states.append(successor_state)

        return result

    def searchH(self,state):
        total_state_index = 0
        result = []
        frontier = Queue()
        visited = set()
        all_states = []

        # Check if goal state is already reached
        if self.goal_test(state):
            return result

        # Add initial state to frontier and visited set
        frontier.put(total_state_index)
        visited.add(self.problem.get_initial_state())
        all_states.append(state)

        while not frontier.empty():
            current_state_index = frontier.get()
            current_state = all_states[current_state_index]

            # Generate successor states
            successor_states = self.successorH(current_state, current_state_index)

            for successor_state in successor_states:
                # If goal state is found, build solution and return
                if self.goal_test(successor_state):
                    result = self.build_solution(successor_state, all_states,state.get_parent_index())
                    return len(result)

                # Add successor state to frontier and visited set
                if successor_state not in visited:
                    total_state_index += 1
                    frontier.put(total_state_index)
                    visited.add(successor_state)
                    all_states.append(successor_state)

        return 10000000
    def successor(self, state, current_state_index):
        result = []
        # Get all possible actions

        for action in self.problem.get_domain().get_actions():
            # Check if action is applicable to state
            if action.is_applicable(state):
                new_state = action.progress(state)
                # Set parent state index and action
                new_state.set_parent_index(current_state_index)
                result.append(new_state)

        return result
    def successorH(self, state, current_state_index):
        result = []
        # Get all possible actions

        for action in self.problem.get_domain().get_actions():
            # Check if action is applicable to state
            if action.is_applicable(state):
                new_state = action.progress1(state)
                # Set parent state index and action
                new_state.set_parent_index(current_state_index)
                result.append(new_state)
        return result

    def build_solution(self, state, all_states, end_index=-1):
        result = []

        # Find goal state index
        while state.get_parent_index() != end_index:
            result.append(state.get_action_name())
            state = all_states[state.get_parent_index()]
        result.reverse()
        return result

    def goal_test(self, state):
        goal = self.problem.get_goal_state()
        return goal.get_positive_literals().issubset(
            state.get_positive_literals()
        ) and state.get_negative_literals().isdisjoint(goal.get_positive_literals())
