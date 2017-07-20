#!/bin/python

import sys
import os


# Complete the function below.

class Zombie(object):
    def __init__(self, i):
        self.zombie_id = i
        self.know_list = []


# recursively remove zomblie cluster from zombie_list
def mergeCluster(zombie_list):
    # remove from zombie_id.know_list
    for z in zombie_list:
        # merge know_list of each
        # print z.know_list
        for i in z.know_list:
            if (i == z.zombie_id):
                pass
            # print z.zombie_id, z.know_list,  i, zombie_list[i].know_list
            """ optimization: deDup here to avoid performance issue with very long relation lists """
            z.know_list = list(set(z.know_list + zombie_list[i].know_list))
            """ fix: forward ith zombie's relation to it's knownZombies to fix the problem of <=2nd degree reached """
            zombie_list[i].know_list = z.know_list

    # make sets from know_list
    know_list_sets = []
    for z in zombie_list:
        know_list_sets.append(set(z.know_list))

    # print know_list_sets

    cluster_no_dup = []
    # filter unique know_list set
    for e in know_list_sets:
        if e not in cluster_no_dup:
            cluster_no_dup.append(e)

    # print cluster_no_dup
    return len(cluster_no_dup)


def zombieCluster(zombies):
    # cluster count
    cluster_count = 0

    # remaining zombies
    zombie_list = []

    # clustered zombies
    cluster_list = []

    for i in range(0, len(zombies)):
        # new zombie
        z = Zombie(i)
        for j in range(len(zombies[i])):
            # zombie knows
            if zombies[i][j] == '1':
                # print z,i,j,zombies[i][j], type(zombies[i][j])
                z.know_list.append(j)

        zombie_list.append(z)

    # remove a cluster from zombie_list
    return mergeCluster(zombie_list)


f = open(os.environ['OUTPUT_PATH'], 'w')

_zombies_cnt = 0
_zombies_cnt = int(raw_input())
_zombies_i = 0
_zombies = []
while _zombies_i < _zombies_cnt:
    _zombies_item = raw_input()
    _zombies.append(_zombies_item)
    _zombies_i += 1

res = zombieCluster(_zombies);
f.write(str(res) + "\n")

f.close()

