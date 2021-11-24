class Sort():
    def __init__(self, data) -> None:
        self.list = data

    def select_sort(self):
        for i in range(len(self.list)):
            min_idx = i
            for j in range(i+1, len(self.list)):
                if self.list[min_idx] > self.list[j]:
                    min_idx = j
            self.list[i], self.list[min_idx] = self.list[min_idx], self.list[i]

    def insert_sort(self):
        for i in range(1, len(self.list)):
            for j in range(i, 0, -1):
                if self.list[j] < self.list[j-1]:
                    self.list[j], self.list[j-1] = self.list[j-1], self.list[j]
                else:
                    break

    def quick_sort(self, array):
        if len(array) <= 1:
            return array
        pivot = array[0]
        tail = array[1:]

        left_side = [x for x in tail if x <= pivot]
        right_side = [x for x in tail if x > pivot]

        return self.quick_sort(left_side) + [pivot] + self.quick_sort(right_side)
    
    def print_list(self):
        print(self.list)

        
        


if __name__ == "__main__":
    data = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    sort = Sort(data)

    print(sort.quick_sort(data))
    # sort.print_list()