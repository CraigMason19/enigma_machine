# enigma_machine
A python implementation of a M3 enigma machine. Contains 2 reflectors, 5 rotors (with notches) and a plugboard with upto 10 connections.

Created just for fun.

<img src="https://github.com/CraigMason19/enigma_machine/blob/2316fd1a24706058016ff39a0738777449df5837/enigma_machine.jpg" alt="enigma_machine" width="300" height="auto">

## Requirements
None.

## Usage

### Creation

The Enigma machine supports two reflectors ("UKW-B" & "UKW-C"). You can create a machine using any three rotors selected from a pool of five ("I", "II", "III", "IV", "V"). The machine is initialized with a reflector and three rotors.
```Python
em = M3EnigmaMachine("UKW-B", ["III", "IV", "V"])
```

Rotors can be set with or without specifying the notches. If a second argument is provided, it represents the notches on the rotors. If no second argument is given, the default value of ["A", "A", "A"] is used, which means no notch changes.
```Python
em.set_rotors(["A", "B", "C"])
em.set_rotors(["A", "B", "C"], ["D", "E", "F"])
```

You can create a plugboard with up to 10 connections. This will swap the letters before they are processed by the machine.
```Python
em.set_plugboard('AB CD EF GH IJ') 
```

### Encoding

Two methods are provided for encoding, you can encode individual letters or entire messages. 

```Python
em.encode_letter(letter)
em.encode_message(message)
```

Using the same machine settings, encoding a message will produce the encoded version, and encoding the encoded message again will revert it to the original.

```Python
em1 = M3EnigmaMachine("UKW-B", ["III", "IV", "V"])
em2 = M3EnigmaMachine("UKW-B", ["III", "IV", "V"])

m1 = em1.encode_message("HELLO") # AJKUH
m2 = em2.encode_message("AJKUH") # HELLO
```