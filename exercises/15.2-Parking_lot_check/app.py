parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:


def get_parking_lot(parking):
  state = {
     "total_slots": 0,
     "available_slots": 0,
     "occupied_slots": 0
  }
  for row in parking: 
    for col in row:
      if col != 0:
        state["total_slots"] += 1
      if col == 2:
        state["available_slots"] += 1
      if col == 1:
        state["occupied_slots"] += 1
  return state
state = get_parking_lot(parking_state)
print(state)