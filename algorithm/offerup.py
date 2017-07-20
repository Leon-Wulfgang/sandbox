#
# Let's implement a data store for strings. Please keep one copy of duplicate
# strings. Ordering is not required
# - void add(string)
# - void remove(string)
# - void remove_randomly()
# - list_all() already implemented
#
# Example:
# - add('xyz'),        list_all -> xyz
# - add('xyz'),        list_all -> xyz
# - add('abc'),        list_all -> xyz abc (may also abc xyz)
# - remove('xyz'),     list_all -> abc
# - remove_randomly(), list_all -> empty
#

# store
#

class string_storage(object):
    store = {}
    store_array = []

    def add(self, str):  # xyz   store_array[xyz]  index==0 store = {'xyz':0}  # xyz found_key = 0 #
        found_key = self.store[str]
        if not found_key:
            self.store_array.append(str)  # store_array [xyz, abc]   len=2  1
            self.store[str] = len(store_array) - 1  # store = {'xyz':0, 'abc': 1}

    def remove(self, str):
        # not found do nothing
        if str not in self.store:
            return

            # find index
        idx_str = self.store[str]  # idx_str = 0

        # swap element with last
        self.store_array[idx_str], self.store_array[len(self.store_array) - 1] = self.store_array[
                                                                                     len(self.store_array) - 1], \
                                                                                 self.store_array[
                                                                                     idx_str]  # store_array[abc, xyz]

        # remove from dict and from last of array
        del self.store[str]  # store = {'abc': 1}
        del self.store_array[len(self.store_array) - 1]  #

    def remove_randomly():
        rnd = random(len(self.store_array))
        str = self.store_array[rnd]
        del self.store_array[rnd]
        del self.store[str]
