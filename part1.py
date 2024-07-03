our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

shared_routes = our_routes.intersection(competitor_routes)  #part1
print(shared_routes)

our_unique_routes = our_routes.difference(competitor_routes)   #part2
print(our_unique_routes)

destinations_not_shared = our_routes.symmetric_difference(competitor_routes)
print(destinations_not_shared)   #part3