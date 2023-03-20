from cv2 import displayOverlay
from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram, plot_bloch_multivector,plot_state_city
from numpy.random import randint
from qiskit import QuantumCircuit
import qiskit.quantum_info as qi
import numpy as np


def encode_message(bits, bases,n):
    message = []
    for i in range(n):
        qc = QuantumCircuit(1)
        if bases[i] == 0: # Prepare qubit in Z-basis
            if bits[i] == 0:
                pass 
            else:
                qc.x(0)
        else: # Prepare qubit in X-basis
            if bits[i] == 0:
                qc.h(0)
            else:
                qc.x(0)
                qc.h(0)
        qc.barrier()
        message.append(qc)
    return message

def measure_message(message, bases,n):
    simulator = Aer.get_backend('aer_simulator')
    measurements = []
    
    for q in range(n):
        circ = message[q]
        if bases[q] == 0: # measuring in Z-basis
            message[q].measure_all()
        if bases[q] == 1: # measuring in X-basis
            message[q].h(0)
            message[q].measure_all()
        print(message[q])
        
        # Transpile for simulator
        circ = transpile(circ, simulator)
        # Run and get counts
        result = simulator.run(circ).result()
        # Run and get memory
        result = simulator.run(circ, shots=1, memory=True).result()
        memory = result.get_memory(circ)
        measurements.append((memory)[0][0])


    return measurements

def remove_garbage(a_bases, b_bases, bits,n):
    good_bits = []
    for q in range(n):
        if a_bases[q] == b_bases[q]:
            # If both used the same basis, add
            # this to the list of 'good' bits
            good_bits.append(bits[q])
    return good_bits

def sample_bits(bits, selection):
    sample = []
    for i in selection:
        # use np.mod to make sure the
        # bit we sample is always in 
        # the list range
        i = np.mod(i, len(bits))
        # pop(i) removes the element of the
        # list at index 'i'
        sample.append(bits.pop(i))
    return sample

global sender_bases,sender_bits,receiver_key,bit_selection,sender_key

def senderProg(sendermessage,n):
    sender_bits = sendermessage
    #print(sender_bits)

    sender_bases = randint(2, size=n)
    #print(sender_bases)

    encoded_message = encode_message(sender_bits, sender_bases,n)

    """User chooses to encode each bit on qubit in the X or Z-basis at random, 
    and stores the choice for each qubit in alice_bases. 
    0 means "prepare in the Z-basis" and a 1 means "prepare in the X-basis"""


    #print(("message"))
    #print(sendermessage)
    return(encoded_message,sender_bases,sender_bits)

def receiverProg(x,n):
    receiver_bases = randint(2, size=n)
    receiver_results = measure_message(x, receiver_bases,n)
    #print(receiver_results)
    return receiver_results,receiver_bases


def makeKey(Senderbases,receiverresults,receiverbases,senderbits,message,n):
    sender_key = remove_garbage(Senderbases, receiverbases, senderbits,n)
    #print(sender_key)
    receiver_key = remove_garbage(Senderbases, receiverbases, receiverresults,n)
    #print(receiver_key)

    sample_size = 5
    bit_selection = randint(n, size=sample_size)

    simulator = Aer.get_backend('aer_simulator')
    message = []
    for i in range(n):
        qc = QuantumCircuit(1)
        if Senderbases[i] == 0: # Prepare qubit in Z-basis
            if senderbits[i] == 0:
                pass 
            else:
                qc.x(0)
        else: # Prepare qubit in X-basis
            if senderbits[i] == 0:
                qc.h(0)
            else:
                qc.x(0)
                qc.h(0)
        qc.barrier()
        message.append(qc)
    
    simulator = Aer.get_backend('aer_simulator')
    measurements = []
    
    for q in range(n):
        circ = message[q]
        if Senderbases[q] == 0: # measuring in Z-basis
            message[q].measure_all()
        if Senderbases[q] == 1: # measuring in X-basis
            message[q].h(0)
            message[q].measure_all()
        #print(message[q])

    

    receiver_sample = sample_bits(receiver_key, bit_selection)
    print("\nreceiver_sample = " + str(receiver_sample))
    sender_sample = sample_bits(sender_key, bit_selection)
    print("sender_sample = "+ str(sender_sample))
    return sender_sample
