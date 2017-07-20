# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys



####
# pre_req parser
def parse_pre(pre, op_seq):
    # pre with no pre_req, append itself
    if op_dict[pre] == []:
        op_seq.append(pre)
    # pre has pre_req, append itself and recursively it's pre_req
    else:
        op_seq.append(pre)
        for pre_pre in op_dict[pre]:
            op_seq.append(pre_pre)
            parse_pre(pre_pre, op_seq)

            ####
# list of available operations
op_dict = {}  # operation dictionary
last_op = ''  # the last operation passed in as input, for testing
aaa = [
"two,one",
"one",
"four,two,three",
"three,one",
"five",
"final,four,five"]

for line in aaa:
    # parse str to op_name[pre_req]
    temp = line.strip().split(',')
    operation_name = temp[0]
    pre_req = temp[1:]

    # populate dictionary
    op_dict[operation_name] = pre_req

    # update last_op for testing
    last_op = operation_name


# operation sequence for producing last_op_obj
op_seq = []

# start parsing sequence
for pre in op_dict[last_op]:
    parse_pre(pre, op_seq)

op_seq.reverse()

# remove duplicates
op_seq_no_dup = []
for e in op_seq:
    if e not in op_seq_no_dup:
        op_seq_no_dup.append(e)
op_seq_no_dup.append(last_op)

for op_name in op_seq_no_dup:
    print "Operation %s on part X" % op_name