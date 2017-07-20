// Write
a
function
that
will
execute
a
set
of
tasks in dependency
order.For
example, given
the
following
tasks
// [
    {"id": 1, "depends": [2, 3]},
    {"id": 2, "depends": []},
    {"id": 3, "depends": [2, 4]},
    {"id": 4, "depends": []}
]
// The
order in which
they
should
be
executed is as follows:
// order: 2, 4, 3, 1

from deepcopy import deepcopy

()


# queue of task

# get dep, push to left of queue

# not dep: run left

# run
def run_task(task):
    print
    task


# get dependencies and push to left of the queue
def populate_queue(tasks):
    """
    # temp queue
    queue = []

    for task in tasks:
        # finding a task in queue takes O(n) extra
        # find task in queue, insert dep before its position     2,|2,4|,3,1
        # 2,3,1,2,2,4,3,4
        # [2,4,3,1]
        # [1]

        # append depends and id to queue
        queue = queue + append(task['depends'])
        queue.append(task['id'])
    """

    # now have a queue: [2,3,1,2,2,4,3,4]
    remain_tasks = deepcopy(tasks)

    # [
    {"id": 1, "depends": [2]},
    {"id": 2, "depends": [1]},
    ]

    for dep in task['depends']:
        if
    dep == task['id']:
    return 'invalid'

    # final
    final_queue = []

    # check if any task remains
    while len(remain_tasks) > 0:

        # loop for each remaining task
        for remain_task in remain_tasks:

            # check if dependency exist in final queue
            for dep in remain_task['depends']:
                if dep not in final_queue:
                    continue

            # every dep in final_queue, ready to run
            final_queue.append(remain_task['id'])

            # remove remain_task from remain_tasks
            _ = remain_tasks.pop(remain_task)

            # dependencies, task => queue

    return final_queue


# init task array
tasks = [
    {"id": 1, "depends": [2, 3]},
    {"id": 2, "depends": []},
    {"id": 3, "depends": [2, 4]},
    {"id": 4, "depends": []}
]

# generate order
final_queue = populate_queue(tasks)

# print in order
for task in final_queue:
    run_task(task)




