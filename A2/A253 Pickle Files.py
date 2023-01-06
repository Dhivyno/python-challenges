import pickle

NUM_LINES = 100
DUMMY_RECORD = ('', '', 0)
records = [DUMMY_RECORD] * NUM_LINES

with open('records.pkl', 'wb') as f:
    pickle.dump(records, f)

def check_dummy_record(index):
    with open('records.pkl', 'rb') as f:
        records = pickle.load(f)
    return records[index] == DUMMY_RECORD

print(check_dummy_record(0))
print(check_dummy_record(1))
print(check_dummy_record(99))
records[0] = ('Dhiv', 'Dhiv@gmail.com', 25)
with open('records.pkl', 'wb') as f:
    pickle.dump(records, f)
print(check_dummy_record(0))
print(check_dummy_record(1))
print(check_dummy_record(99))
