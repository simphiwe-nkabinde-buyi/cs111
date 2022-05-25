import math

can_list = [
    {
        'name': '#1 Picninc',
        'radius': 6.83,
        'height': 10.16,
        'cost': 0.28
    },
    {
        'name': '#1 Tall',
        'radius': 7.78,
        'height': 11.91,
        'cost': 0.43
    },
    {
        'name': '#2',
        'radius': 8.73,
        'height': 11.59,
        'cost': 0.45
    },
    {
        'name': '#2.5',
        'radius': 10.32,
        'height': 11.91,
        'cost': 0.61
    },
    {
        'name': '#3 Cylinder',
        'radius': 10.79,
        'height': 17.78,
        'cost': 0.86
    },
    {
        'name': '#5',
        'radius': 13.02,
        'height': 14.29,
        'cost': 0.83
    },
    {
        'name': '#6Z',
        'radius': 5.40,
        'height': 8.89,
        'cost': 0.22
    },
    {
        'name': '#8Z Short',
        'radius': 6.83,
        'height': 7.62,
        'cost': 0.26
    },
    {
        'name': '#10',
        'radius': 15.72,
        'height': 17.78,
        'cost': 1.53
    },
    {
        'name': '#211',
        'radius': 6.83,
        'height': 12.38,
        'cost': 0.34
    },
    {
        'name': '#300',
        'radius': 7.62,
        'height': 11.27,
        'cost': 0.38
    },
    {
        'name': '#303',
        'radius': 8.10,
        'height': 11.11,
        'cost': 0.42
    }

]
def main():
    best_store = None
    best_cost = None
    max_store_eff = 0
    max_cost_eff = 0

    for can in can_list:
        #get storage and cost efficiency of can
        store_eff = compute_storage_efficiency(can['radius'], can['height'])
        cost_eff = compute_cost_efficiency(can['radius'], can['height'], can['cost'])
        #print can name and efficiencies
        print(f"{can['name']}, {store_eff:.2f}, {cost_eff:.2f}")
        
        #store max cost efficiency
        if store_eff > max_store_eff:
            max_store_eff = store_eff
            best_store = can

        #store max cost efficiency
        if cost_eff > max_cost_eff:
            max_cost_eff = cost_eff
            best_cost = can
    print()
    print(f"Best can size storage efficiency\n name:{best_store['name']}, r:{best_store['radius']}, h:{best_store['height']}")
    print(f"Best can size cost efficiency\n name:{best_cost['name']}, r:{best_cost['radius']}, h:{best_cost['height']}")


def cylinder_volume(radius, height):
    """compute and return the volume of a cylinder

    Parameters
        radius: the radius of the cylinder
        height: the height of then cylinder
    Return: the volume of a cylinder
    """
    return math.pi * radius**2 * height

def cylinder_surface_area(radius, height):
    """compute and return the surface area of cylinder

    Parameters
        radius: the radius of the cylinder
        height: the height of then cylinder
    Return: the surface of a cylinder
    """
    return 2*math.pi * radius * (radius + height)

def compute_storage_efficiency(radius, height):
    """compute and return the storage efficiency of a cylinder can

    Parameters
        radius: the radius of the cylinder
        height: the height of then cylinder
    Return: the storage efficiency of the cylinder
    """
    return cylinder_volume(radius, height) / cylinder_surface_area(radius, height)

def compute_cost_efficiency(radius, height, cost):
    """compute and return the cost efficeincy of a cylinder can

    Parameters
        radius: the radius of the cylinder
        height: the height of then cylinder
        cost: the cost per can
    Return: the cost efficiency of the cylinder
    """
    return cylinder_volume(radius, height) / cost



main()