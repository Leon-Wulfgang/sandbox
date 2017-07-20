# a iterator class for fibonacci number generator


class FibIterable:
    """
    this class is a generates a well known sequence of numbers
    """
    def __init__(self, iLast=1, iSecondLast=0, iMax=50):
        self.iLast = iLast
        # save the original starting point -1 position for re-iteration
        self.original_iLast = iLast
        self.iSecondLast = iSecondLast
        # save the original starting point -2 position for re-iteration
        self.original_iSecondLast = iSecondLast
        self.iMax = iMax  # end point

    def __iter__(self):
        return self    # because the object is both the iterable and the iterator

    def next(self):
        # generate the next number
        iNext = self.iLast + self.iSecondLast

        # check break point
        if iNext > self.iMax:
            # when break at the end, re-init the -1 and -2 positions to original starting point
            self.iLast = self.original_iLast
            self.iSecondLast = self.original_iSecondLast
            raise StopIteration()

        # shift -1 and -2 positions to right by 1
        self.iSecondLast = self.iLast
        self.iLast = iNext
        return iNext

o = FibIterable()

# first iteration
for i in o:
    print(i)

# second iteration made correct by re-init -1 and -2 positions when reaching end point
for i in o:
    print(i)
