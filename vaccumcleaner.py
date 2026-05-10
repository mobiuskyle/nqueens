import random

# SIMPLE VACUUM CLEANER AGENT
#
# Environment:
#   - Multiple rooms/locations arranged in a grid
#   - Each location can be 'Dirty' or 'Clean'
#
# Agent Behaviour (Reflex Agent):
#   - PERCEIVE the current location's status
#   - If DIRTY  → CLEAN it
#   - If CLEAN  → MOVE to the next unvisited dirty location
#
# Performance Measure:
#   - Number of locations cleaned
#   - Total moves taken (lower = more efficient)

class VacuumEnvironment:
    """Represents the environment with multiple rooms."""

    def __init__(self, locations):
        """
        Initialise the environment.
        locations: list of room names e.g. ['A', 'B', 'C', 'D']
        Each room is randomly assigned as 'Dirty' or 'Clean'.
        """
        self.locations = locations
        # Randomly assign dirt status to each room at startup
        self.status = {loc: random.choice(['Dirty', 'Clean'])
                       for loc in locations}

    def display(self):
        """Print the current state of all rooms."""
        print("\nEnvironment Status:")
        for loc, state in self.status.items():
            print(f"  Room {loc}: {state}")

    def is_all_clean(self):
        """Check if all rooms are clean."""
        return all(s == 'Clean' for s in self.status.values())


class VacuumAgent:
    """
    A simple reflex-based vacuum cleaner agent.
    Perceives the current room and acts accordingly.
    """

    def __init__(self, environment):
        self.env = environment
        self.location = environment.locations[0]  # Start at first room
        self.moves = 0
        self.cleans = 0

    def perceive(self):
        """Return the current location and its dirty/clean status."""
        return self.location, self.env.status[self.location]

    def act(self):
        """
        Agent action based on percept:
          - CLEAN if current location is dirty
          - MOVE  if current location is clean
        """
        location, status = self.perceive()

        if status == 'Dirty':
            print(f"  [ACTION] Room {location} is DIRTY → Cleaning...")
            self.env.status[location] = 'Clean'   # Clean the room
            self.cleans += 1
        else:
            print(f"  [ACTION] Room {location} is CLEAN → Moving...")

        # Move to next room (cycle through all rooms)
        current_index = self.env.locations.index(self.location)
        next_index = (current_index + 1) % len(self.env.locations)
        self.location = self.env.locations[next_index]
        self.moves += 1

    def run(self):
        """
        Run the agent until all rooms are clean.
        Safety limit: max_steps prevents infinite loops.
        """
        max_steps = len(self.env.locations) * 3  # reasonable upper bound

        print("\n--- Vacuum Agent Starting ---")
        self.env.display()
        print("\n--- Agent Actions ---")

        step = 0
        while not self.env.is_all_clean() and step < max_steps:
            self.act()
            step += 1

        # Final report
        print("\n--- All Rooms Cleaned! ---")
        self.env.display()
        print(f"\nPerformance Summary:")
        print(f"  Rooms Cleaned : {self.cleans}")
        print(f"  Total Moves   : {self.moves}")
        print(f"  Steps Taken   : {step}")


# MAIN — Run the Vacuum Agent
if __name__ == "__main__":
    # Define the rooms in the environment
    rooms = ['A', 'B', 'C', 'D', 'E']

    # Create environment and agent
    environment = VacuumEnvironment(rooms)
    agent = VacuumAgent(environment)

    # Run the agent
    agent.run()