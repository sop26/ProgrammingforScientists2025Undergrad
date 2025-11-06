from datatypes import OrderedPair, Boid, Sky 
import math

#add your additional functions from cogniterra here!

def simulate_boids(initial_sky: Sky, num_gens: int, time_step: float) -> list[Sky]:
    """
    Simulates the boids by updating the sky for specified number of generations each specified time step long
    """
    skies = [update_sky(initial_sky, time_step)]
    for i in range(1, num_gens):
        skies.append(update_sky(skies[i-1], time_step))
    return skies

def update_sky(current_sky: Sky, time_step: float) -> Sky:
    """
    Updates the boids in the sky after one time step
    """
    new_sky = copy_sky(current_sky)
    for i in range(len(new_sky.boids)):
        boid = new_sky.boids[i]
        old_boid = current_sky.boids[i]
        boid.acceleration = update_acceleration(new_sky, i)
        boid.velocity = update_velocity(boid, old_boid.acceleration, new_sky.max_boid_speed, time_step)
        boid.position = update_position(boid, old_boid.acceleration, old_boid.velocity, new_sky.width, time_step)
    return new_sky

def update_position(b: Boid, old_acceleration: OrderedPair, old_velocity: OrderedPair, sky_width: float, time_step: float) -> OrderedPair:
    """
    Output new position based on current position, old velocity, and old acceleration
    """
    new_pos_x = 1/2 * old_acceleration.x * time_step**2 + old_velocity.x * time_step + b.position.x
    new_pos_y = 1/2 * old_acceleration.y * time_step**2 + old_velocity.y * time_step + b.position.y
    if new_pos_x > sky_width or new_pos_x < sky_width:
        new_pos_x %= sky_width
    if new_pos_y > sky_width or new_pos_y < sky_width:
        new_pos_y %= sky_width
    return OrderedPair(new_pos_x, new_pos_y)

def update_velocity(b: Boid, old_acceleration: OrderedPair, max_boid_speed: float, time_step: float) -> OrderedPair:
    """
    Updates the boid's velocity based on acceleration
    """
    new_velo_x = 1/2 * (b.acceleration.x + old_acceleration.x) * time_step + b.velocity.x
    new_velo_y = 1/2 * (b.acceleration.y + old_acceleration.y) * time_step + b.velocity.y
    speed = math.sqrt(new_velo_x**2 + new_velo_y**2) 
    if speed > max_boid_speed:
        new_velo_x = max_boid_speed * new_velo_x/speed
        new_velo_y = max_boid_speed * new_velo_y/speed
    return OrderedPair(new_velo_x, new_velo_y)

def update_acceleration(current_sky: Sky, i: int) -> OrderedPair:
    """
    Outputs the new acceleration of a boid based on neighboring boids
    """
    align_accel = net_acceleration_due_to_alignment(current_sky, i) 
    cohesion_accel = net_acceleration_due_to_cohesion(current_sky, i)
    separation_accel = net_acceleration_due_to_separation(current_sky, i)
    
    final_accel = sum_vectors([align_accel, cohesion_accel, separation_accel])
    return final_accel

def net_acceleration_due_to_cohesion(current_sky: Sky, i: int) -> OrderedPair: 
    """
    Computes the net acceleration of a boid resulting from nearby boids based on the principle of cohesion. Nearby       boids tend to stick together.
    """
    boid = current_sky.boids[i]
    boid_pos = boid.position
    sum_x = 0
    sum_y = 0
    num_in_proxim = 0
    
    for other_boid in current_sky.boids:
        other_pos = other_boid.position
        d = distance(boid_pos, other_pos)
        if boid != other_boid and d < current_sky.proximity:
            num_in_proxim += 1
            if d == 0: 
                continue
            sum_x += (other_pos.x - boid_pos.x)/d
            sum_y += (other_pos.y - boid_pos.y)/d  
    
    if num_in_proxim == 0:
          return OrderedPair(0.0, 0.0)
                     
    cohesion = current_sky.cohesion_factor
    net_accel_x = cohesion * sum_x/num_in_proxim # mass is 1
    net_accel_y = cohesion * sum_y/num_in_proxim
    
    return OrderedPair(net_accel_x, net_accel_y)

def net_acceleration_due_to_alignment(current_sky: Sky, i: int) -> OrderedPair:
    """
    Computes the net acceleration of a boid resulting from nearby boids based on the principle of alignment. Nearby     boids tend to mimic each others' velocities.
    """
    boid = current_sky.boids[i]
    boid_pos = boid.position
    sum_x = 0
    sum_y = 0
    num_in_proxim = 0
    
    for other_boid in current_sky.boids:
        d = distance(boid_pos, other_boid.position)
        if boid != other_boid and d < current_sky.proximity:  
            num_in_proxim += 1
            if d == 0:
                continue
            other_velo = other_boid.velocity
            sum_x += other_velo.x/d
            sum_y += other_velo.y/d
    align = current_sky.alignment_factor
    
    if num_in_proxim == 0:
            return OrderedPair(0.0, 0.0)
      
    net_accel_x = align * sum_x / num_in_proxim # mass is 1 
    net_accel_y = align * sum_y / num_in_proxim 
    
    return OrderedPair(net_accel_x, net_accel_y)

def net_acceleration_due_to_separation(current_sky: Sky, i: int) -> OrderedPair:
    """
    Computes the net acceleration of a boid resulting from nearby boids based on the principle of separation. Boids     that flock too closely together separate to avoid collision.
    """
    boid = current_sky.boids[i]
    boid_pos = boid.position
    sum_x = 0
    sum_y = 0
    num_in_proxim = 0
    
    for other_boid in current_sky.boids:
        other_pos = other_boid.position
        d = distance(boid_pos, other_pos)
        if boid != other_boid and d < current_sky.proximity:  
            num_in_proxim += 1
            if d**2 == 0:
                continue
            sum_x += (boid_pos.x - other_pos.x)/d**2
            sum_y += (boid_pos.y - other_pos.y)/d**2
            
    if num_in_proxim == 0:
          return OrderedPair(0.0, 0.0)
      
    separation = current_sky.separation_factor        
    net_accel_x = separation * sum_x / num_in_proxim # mass is 1 
    net_accel_y = separation * sum_y / num_in_proxim 
    
    return OrderedPair(net_accel_x, net_accel_y)

# sum_vectors adds a list of OrderedPair objects and returns the total.
def sum_vectors(vectors: list[OrderedPair]) -> OrderedPair:
    sum_x = 0
    sum_y = 0
    for vector in vectors:
        sum_x += vector.x
        sum_y += vector.y
    new_pair = OrderedPair(sum_x, sum_y)
    return new_pair

def limit_speed(vel: OrderedPair, max_speed: float) -> OrderedPair:
    """
    Returns the velocity less than or equal to the max speed
    """
    speed = math.sqrt(vel.x**2 + vel.y**2)
    if speed > max_speed:
        new_x = vel.x * max_speed / speed
        new_y = vel.y * max_speed / speed
        vel = OrderedPair(new_x, new_y)
    return vel

def distance(p0: OrderedPair, p1: OrderedPair) -> float:
    """
    Compute the Euclidean distance between two points in 2D space.
    Input:
        p0 (OrderedPair): The first point, with x and y coordinates.
        p1 (OrderedPair): The second point, with x and y coordinates.
    Output:
        float: The Euclidean distance between p0 and p1.
    """
    dx = p0.x - p1.x
    dy = p0.y - p1.y
    return math.sqrt(dx * dx + dy * dy)

def copy_sky(current_sky: Sky) -> Sky:
    """
    Create a deep copy of a Sky object, duplicating all its parameters and boids.
    Input:
        current_sky (Sky): The Sky instance to be copied, containing boids and 
                           simulation parameters (e.g., width, max speed, proximity).
    Output:
        Sky: A new Sky object with identical properties and boid data as the input, 
             but stored in separate memory so changes to one do not affect the other.
    """
    new_sky = Sky()
    new_sky.width = current_sky.width
    new_sky.max_boid_speed = current_sky.max_boid_speed
    new_sky.proximity = current_sky.proximity
    new_sky.separation_factor = current_sky.separation_factor
    new_sky.alignment_factor = current_sky.alignment_factor
    new_sky.cohesion_factor = current_sky.cohesion_factor

    new_boids = []
    for b in current_sky.boids:
        pos_copy = OrderedPair(b.position.x, b.position.y)
        vel_copy = OrderedPair(b.velocity.x, b.velocity.y)
        acc_copy = OrderedPair(b.acceleration.x, b.acceleration.y)
        new_boids.append(Boid(pos_copy, vel_copy, acc_copy))

    new_sky.boids = new_boids
    return new_sky