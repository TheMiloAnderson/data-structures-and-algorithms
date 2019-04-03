class QuickSort(object):
    """ Implements a quick sort algorithm with .sort method """

    def sort(self, arr):
        high = len(arr) - 1
        self._sort(arr, 0, high)

    def _sort(self, arr, low, high):
        if low < high:
            p = self._partition(arr, low, high)
            self._sort(arr, low, p-1)
            self._sort(arr, p+1, high)

    def _partition(self, arr, low, high):
        i = j = low
        while j < high:
            if arr[j] <= arr[high]:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
            j += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

    def __repr__(self):
        return str(self.__class__) + str(self.__dict__)

    def __str__(self):
        return '<QuickSort Algorithm>'