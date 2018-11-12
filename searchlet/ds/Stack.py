# Copyright (c) 2018 David Chan
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from typing import Any


class Stack(object):
    """Simple stack class
    """

    def __init__(self,):
        self.memory = []

    def push(self, obj: Any) -> None:
        """Push an element onto the stack

        :param obj: The object to push onto the stack
        :type obj: Any
        """

        self.memory.append(obj)

    def pop(self,) -> Any:
        """Pops an element from the stack

        :return: The popped element
        :rtype: Any
        """

        ret_val = self.memory[-1]
        self.memory = self.memory[:-1]
        return ret_val

    def peek(self,) -> Any:
        """Peeks at the possible return value of the stack

        :return: The element at the top of the stack
        :rtype: Any
        """

        return self.memory[-1]

    def empty(self, ) -> bool:
        """Returns if the stack is empty
        
        :return: If the stack is empty
        :rtype: bool
        """
        return len(self.memory) == 0

    def __str__(self, ) -> str:
        return str(self.memory)

