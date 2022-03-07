
import math

def main():
    name = "#1 Picnic"
    radius = 6.83
    height = 10.16
    cost = 0.28
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    cost_efficiency = compute_cost_efficiency(volume, cost)
    print(f"{name} {storage_efficiency:.1f} {cost_efficiency:.0f}")

    name = "#1 Tall"
    radius = 7.78
    height = 11.91
    cost = 0.43
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    cost_efficiency = compute_cost_efficiency(volume, cost)
    print(f"{name} {storage_efficiency:.1f} {cost_efficiency:.0f}")

    name = "#2 "
    radius = 8.73
    height = 11.59
    cost = 0.45
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    cost_efficiency = compute_cost_efficiency(volume, cost)
    print(f"{name} {storage_efficiency:.1f} {cost_efficiency:.0f}")

    name = "#2.5"
    radius = 10.32
    height = 11.91
    cost = 0.61
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    cost_efficiency = compute_cost_efficiency(volume, cost)
    print(f"{name} {storage_efficiency:.1f} {cost_efficiency:.0f}")

    name = "#3 Cylinder"
    radius = 10.79
    height = 17.78
    cost = 0.86
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    cost_efficiency = compute_cost_efficiency(volume, cost)
    print(f"{name} {storage_efficiency:.1f} {cost_efficiency:.0f}")

    name = "#5"
    radius = 13.02
    height = 14.29
    cost = 0.83
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    cost_efficiency = compute_cost_efficiency(volume, cost)
    print(f"{name} {storage_efficiency:.1f} {cost_efficiency:.0f}")

    name = "#6Z"
    radius = 5.40
    height = 8.89
    cost = 0.22
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    cost_efficiency = compute_cost_efficiency(volume, cost)
    print(f"{name} {storage_efficiency:.1f} {cost_efficiency:.0f}")

    name = "#8Z Short"
    radius = 6.83
    height = 7.62
    cost = 0.26
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    cost_efficiency = compute_cost_efficiency(volume, cost)
    print(f"{name} {storage_efficiency:.1f} {cost_efficiency:.0f}")

    name = "#10"
    radius = 15.72
    height = 17.78
    cost = 1.53
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    cost_efficiency = compute_cost_efficiency(volume, cost)
    print(f"{name} {storage_efficiency:.1f} {cost_efficiency:.0f}")

    name = "#211"
    radius = 6.83
    height = 12.38
    cost = 0.34
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    cost_efficiency = compute_cost_efficiency(volume, cost)
    print(f"{name} {storage_efficiency:.1f} {cost_efficiency:.0f}")

    name = "#300"
    radius = 7.62
    height = 11.27
    cost = 0.38
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    cost_efficiency = compute_cost_efficiency(volume, cost)
    print(f"{name} {storage_efficiency:.1f} {cost_efficiency:.0f}")

    name = "#303"
    radius = 8.10
    height = 11.11
    cost = 0.42
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    cost_efficiency = compute_cost_efficiency(volume, cost)
    print(f"{name} {storage_efficiency:.1f} {cost_efficiency:.0f}")

def compute_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(volume, surface_area):
    storage_efficiency = volume / surface_area
    return storage_efficiency

def compute_cost_efficiency(volume, cost):
    cost_efficiency = volume / cost
    return cost_efficiency

main()