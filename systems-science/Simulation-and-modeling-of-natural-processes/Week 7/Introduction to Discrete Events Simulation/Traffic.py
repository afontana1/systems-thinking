"""Discrete-event simulation of a simple traffic light system.

Algorithm:
- Events are ordered by time in a priority queue.
- Car arrivals enqueue a light-change event if the light is red and the
  car is the first in line.
- Light changes from red->green clear the queue after Tp per car.
"""
from __future__ import annotations

from dataclasses import dataclass, field
import heapq
from typing import Protocol


Tp = 10  # time for one car to pass
Tc = 30  # latency to change light


class Event(Protocol):
    time: float

    def execute(self, queue: "EventQueue", state: "TrafficState") -> None: ...


@dataclass
class TrafficState:
    cars_waiting: int = 0
    green: bool = False

    def turn_green(self) -> None:
        self.green = True

    def turn_red(self) -> None:
        self.green = False

    def add_car(self) -> None:
        self.cars_waiting += 1

    def clear_cars(self) -> None:
        self.cars_waiting = 0


@dataclass(order=True)
class ScheduledEvent:
    time: float
    seq: int
    event: Event = field(compare=False)


class EventQueue:
    def __init__(self) -> None:
        self._heap: list[ScheduledEvent] = []
        self._seq = 0

    def push(self, event: Event) -> None:
        heapq.heappush(self._heap, ScheduledEvent(event.time, self._seq, event))
        self._seq += 1

    def pop(self) -> Event:
        return heapq.heappop(self._heap).event

    def __bool__(self) -> bool:
        return bool(self._heap)


@dataclass
class CarArrival:
    time: float

    def execute(self, queue: EventQueue, state: TrafficState) -> None:
        if not state.green:
            state.add_car()
            if state.cars_waiting == 1:
                queue.push(LightToGreen(self.time + Tc))


@dataclass
class LightToGreen:
    time: float

    def execute(self, queue: EventQueue, state: TrafficState) -> None:
        state.turn_green()
        queue.push(LightToRed(self.time + Tp * state.cars_waiting))
        state.clear_cars()


@dataclass
class LightToRed:
    time: float

    def execute(self, queue: EventQueue, state: TrafficState) -> None:
        state.turn_red()


def main() -> None:
    queue = EventQueue()
    for t in [10, 25, 35, 60, 75]:
        queue.push(CarArrival(t))

    state = TrafficState()

    while queue:
        event = queue.pop()
        print(f"{event.__class__.__name__} at t={event.time}")
        event.execute(queue, state)


if __name__ == "__main__":
    main()
