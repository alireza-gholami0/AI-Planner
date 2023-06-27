from Domains.TireDomain import TireDomain
from Problems.TireProblem import TireProblem
from Problems.BlocksWorldProblem import BlockWorldProblem
from Domains.BlocksWorldDomain import BlockWorldDomain
from Planners.BackwardPlanner import BackwardPlanner
from Planners.ForwardH import ForwardH

# b = BlockWorldDomain()
# back = ForwardH(BlockWorldProblem(b))
b = BlockWorldDomain()
back = BackwardPlanner(BlockWorldProblem(b))

print(back.search())