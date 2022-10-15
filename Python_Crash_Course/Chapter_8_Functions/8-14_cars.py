def record_car(make, model, wheels=4, **car_info):
    """Records info about a specific car in a dictionary."""
    car_info["make"] = make
    car_info["model"] = model
    car_info['wheels'] = wheels
    return car_info


car = record_car(
    "subaru",
    "forester",
    color="maroon",
    year=2006,
    name="N/A",
    tow_package=False,
)

print(car)
