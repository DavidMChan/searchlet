# Copyright (c) 2018 David Chan
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import itertools
import heapq

from typing import List, Any, Union


class PriorityQueue(object):

    REMOVED = '<removed-element>'
    EXISTS_LOWER_PRIORITY = 1
    EXISTS_UPDATED = 2
    NONEXIST = 0

    def __init__(self, ) -> None:
        self.memory: List[Any] = []
        self.counter = itertools.count()
        self.size = 0
        self.map = {}

    def push(self, element: Any, priority: Union[float, int]=0) -> int:
        return_value = PriorityQueue.NONEXIST
        if element in self.map:
            if self.map[element][0] < priority:
                return PriorityQueue.EXISTS_LOWER_PRIORITY
            self.remove_element(element)
            return_value = PriorityQueue.EXISTS_UPDATED
        else:
            self.size += 1
        count = next(self.counter)
        entry = [priority, count, element]
        self.map[element] = entry
        heapq.heappush(self.memory, entry)
        return return_value

    def remove_element(self, element) -> None:
        entry = self.map.pop(element)
        entry[-1] = PriorityQueue.REMOVED
    
    def pop(self, ) -> Any:
        while self.memory:
            priority, _, element = heapq.heappop(self.memory)
            if element is not PriorityQueue.REMOVED:
                del self.map[element]
                self.size -= 1
                return (priority, element)
        raise KeyError("Tried to pop from an empty queue")
    
    def empty(self, ) -> bool:
        return self.size <= 0
