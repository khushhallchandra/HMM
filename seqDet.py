# sequence detection using viterbi algorithm
import pylab
from pomegranate import *
from matplotlib import pyplot as plt
# To define HMM we need (A,B,pi)
# Define B
urn1 = DiscreteDistribution({'R':0.1,'B':0.4,'G':0.5})
urn2 = DiscreteDistribution({'R':0.3,'B':0.3,'G':0.4})
urn3 = DiscreteDistribution({'R':0.45,'B':0.18,'G':0.37})

# These urns are state of the system

s1 = State(urn1, name = 'urn1')
s2 = State(urn2, name = 'urn2')
s3 = State(urn3, name = 'urn3')

hmm = HiddenMarkovModel('Ball pick up')
hmm.add_states([s1,s2,s3])

# Define Pi
hmm.add_transition(hmm.start, s1, 0.4)
hmm.add_transition(hmm.start, s2, 0.35)
hmm.add_transition(hmm.start, s3, 0.25)

# Define A
hmm.add_transition(s1, s1, 0.2)
hmm.add_transition(s1, s2, 0.5)
hmm.add_transition(s1, s3, 0.3)

hmm.add_transition(s2, s1, 0.5)
hmm.add_transition(s2, s2, 0.1)
hmm.add_transition(s2, s3, 0.4)

hmm.add_transition(s3, s1, 0.4)
hmm.add_transition(s3, s2, 0.4)
hmm.add_transition(s3, s3, 0.3)

hmm.bake()

seq = list('RRGBBBGGRR')
logp, path = hmm.viterbi( seq )
print "Sequence: ",''.join(seq)
print "Log Probability: ",logp
print "Path: {}".format(" ".join( state.name for idx, state in path[1:-1] ) )