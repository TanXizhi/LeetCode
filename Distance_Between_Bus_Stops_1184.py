class Solution:
    def distanceBetweenBusStops(self, distance: list[int], start: int, destination: int) -> int:
        start, destination = min(start, destination), max(start, destination)
        cw = sum(distance[start:destination])
        ccw = sum(distance[:start])+sum(distance[destination:])
        return(min(cw, ccw))
