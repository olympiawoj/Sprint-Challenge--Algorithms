"""
YOU CAN NOT
-You may NOT modify any pre-defined robot methods.
- Use iterators (while, for, etc)
- Store any variables =
- Access any instance variables self._anything


YOU CAN
- Use any predefined robot methods
- You may use logical operators. (`if`, `and`, `or`, `not`, etc.)
- Define robot helper methods


This robot sorts lists ONLY using the abilities
- Move left or right
- Pick up an item
- If you pick up an item whole holding one, swap them
- Compare item holding to one in front of it
- Switch light on head on or off

Methods:
can_move_right(self):

self.position = 0

Step 1:
1. Robot sets lights off and swaps None and value in index0

2. IF it can move right
    - Compare the item at index 0 you're holding with item in index 1
    - If this compare returns a number of 1, then index 0 is GREATER than the item in index 1, which means SWAP!!


3. Swap item0 with item1 using swap_item method

4. Else, the compare returns ether a number of 0 or 1 which means the values are equal OR the value of item0 is LESS than the value at index1

5. Once at the end of the list, move back to index 0 - do this by checking for None

if compare_item is NOT none, that means that there's an item on the left and right, so each item should be moved left

6. Once at the beginning, the loop Repeats






"""


class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        print('after move right list', self._list)
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and returns True.
        Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item
        print('items swapped', self._item, self._list[self._position])

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"

    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"

    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out

        # Base case
        # If light is off, array is not sorted
        # Start with item in index 0
        if self.can_move_right() == False and self.light_is_on() == False:
            return

        else:
            # Swap item, adding None to our list
            self.set_light_off()
            self.swap_item()
            # Can we move right?
            while self.can_move_right() == True:
                # Move right
                self.move_right()

                # Compare item at index i+1 to item at i
                if self.compare_item() == 1:
                    # index 0 > index 1 so swap
                    self.swap_item()
                    self.set_light_on()

            # If there's an item that is None, move Robot to left
            while self.compare_item() is not None:
                self.move_left()

            self.swap_item()
            self.move_right()
        return self.sort()


# if __name__ == "__main__":
#     # Test our your implementation from the command line
#     # with `python robot_sort.py`

#     l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1,
#          45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

#     robot = SortingRobot(l)

#     robot.sort()
#     print(robot._list)

robot = SortingRobot([5, 4, 3, 2, 1])
robot.sort()
print(robot._list)
