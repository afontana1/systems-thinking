# Week 7 - Discrete Event Simulation

**Overview**
- Models a simple traffic light with car arrivals using a priority queue of events.

**Files**
- `Traffic.py`: Event classes, queue, state, and simulation loop.
- `Traffic.ipynb`: Notebook wrapper.

**Algorithm**
- Maintain a time-ordered event queue.
- Car arrivals add to the queue; light transitions are scheduled based on wait time.
- Process events in chronological order.

**Run**
```bash
python "Traffic.py"
```

**Dependencies**
- Standard library only
