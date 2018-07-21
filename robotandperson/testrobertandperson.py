import person
import robot


r1 = robot.Robot("Tom", 'red', 30)
r2 = robot.Robot('Jerry', 'blue', 40)


r1.following = r2
r2.following = r1

r1.introduceSelf()
r2.introduceSelf()


p1 = person.Person("Alice", "aggressive", False)
p2 = person.Person("Becky", "talkative", True)

p1.robotOwned = r2
p2.robotOwned = r1

p1.robotOwned.introduceSelf()
p2.robotOwned.introduceSelf()