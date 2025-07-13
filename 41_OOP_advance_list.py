class AdvancedList(list):
    def sum(self):
        return sum(self)

    def average(self):
        return sum(self) / len(self) if self else 0

# Usage
my_list = AdvancedList([1, 2, 3, 4, 5])
print(my_list.sum())      # Output: 15
print(my_list.average())  # Output: 3.0
my_list.append(6)
print(my_list.sum())      # Output: 21