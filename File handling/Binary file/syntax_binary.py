# .dat is the syntax for binary files
#Must use the module called pickle
import pickle

# Reading from a binary file
d = pickle.load(f)  # Load one record at a time

# Writing to a binary file
d = [1, 2, 3]
pickle.dump(d, f)  # Adds the record d in the object f

