# HackKean 2023

This project was developed by rodrigo1514 and I during the HackKean 2023 event. It is an implementation based on the BB84 Protocol, a quantum key distribution scheme.

## Overview

Using principles from quantum mechanics, this project demonstrates the process of generating a secure cryptographic key between two users. Typically, the cipher uses a random starting message. However, we opted to use a pre-defined message and then employ quantum randomization to generate a unique key specific to the two communicating parties.

## Features

- **Quantum Key Distribution**: Utilizes the BB84 protocol to securely exchange cryptographic keys.
- **Quantum Circuit Simulation**: Employs Qiskit to simulate quantum circuits and visualize quantum states.
- **Random Basis Selection**: Implements random basis selection for encoding and measuring quantum bits.
- **Error Detection and Correction**: Incorporates a method to identify and remove mismatched bits between the sender and receiver.

## Code

The main functions of the project are:

- **encode_message(bits, bases, n)**: Encodes a message into quantum states based on provided bits and bases.
- **measure_message(message, bases, n)**: Measures the quantum states in the specified bases.
- **remove_garbage(a_bases, b_bases, bits, n)**: Removes mismatched bits between sender and receiver bases.
- **sample_bits(bits, selection)**: Samples bits from the key for verification.
- **senderProg(sendermessage, n)**: Prepares the sender's message and encoding bases.
- **receiverProg(x, n)**: Simulates the receiver's measurement process.
- **makeKey(Senderbases, receiverresults, receiverbases, senderbits, message, n)**: Generates the final shared key after matching bases and sampling bits.

## Requirements

- Qiskit
- NumPy
- OpenCV (for display purposes, if needed)

## Usage

1. **Sender's Process**:
    ```python
    encoded_message, sender_bases, sender_bits = senderProg(sendermessage, n)
    ```

2. **Receiver's Process**:
    ```python
    receiver_results, receiver_bases = receiverProg(encoded_message, n)
    ```

3. **Key Generation**:
    ```python
    sender_sample = makeKey(sender_bases, receiver_results, receiver_bases, sender_bits, message, n)
    ```

This project provides a practical demonstration of quantum cryptography principles and showcases the potential of quantum computing in enhancing security.
