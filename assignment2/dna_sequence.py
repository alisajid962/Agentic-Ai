sequences = []
valid_bases = {"A", "T", "G", "C"}
base_count = {"A": 0, "T": 0, "G": 0, "C": 0}
sequence_data = []
no_of_sequences = int(input("Enter Number of Sequences: "))
for i in range(no_of_sequences):
    sequence = input("Enter DNA Sequence: ").upper()
    if sequence == "STOP":
        print("Analysis Stopped.")
        break
    sequences.append(sequence)
for i in range(len(sequences)):
    gc_count = 0
    at_count = 0
    for j in sequences[i]:
        if j not in valid_bases:
            print(j, "is Invalid Base. Skipped.")
            continue
        base_count[j] += 1
        if j == "G" or j == "C":
            gc_count += 1
        else:
            at_count += 1
    data = (i + 1, gc_count)
    sequence_data.append(data)

print("\nSequence Classification")
for i in range(len(sequence_data)):

    gc = sequence_data[i][1]
    at = 0
    for j in sequences[i]:
        if j == "A" or j == "T":
            at += 1
    if gc > at:
        print("Sequence", sequence_data[i][0], "= GC-Rich")

    elif gc == at:
        print("Sequence", sequence_data[i][0], "= Balanced")
    else:
        print("Sequence", sequence_data[i][0], "= AT-Rich")
print("\nBase Counts")
for i in base_count:
    print(i, "=", base_count[i])

print("\nSequence Tuple")

for i in sequence_data:
    print(i)