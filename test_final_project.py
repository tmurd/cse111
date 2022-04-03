from final_project import add_to_checked_out_dict, remove_item_from_check_out

import json

from datetime import datetime
current_date_and_time = datetime.now()

import pytest

def test_add_to_checked_out_dict():
    # Setup Stage
    # Write variable user inputs to checked_out.json
    with open("checked_out.json", "w") as outfile:
        outfile.write(json.dumps({
            "Checked Out": {

            }
        }, indent = 4))

    name = "Trenton Murdock"
    item_num = "A001"
    quantity = 1

    # Exercise stage
    add_to_checked_out_dict(name, item_num, quantity)

    # Verify stage
    # Create a time_stamp variable
    time_stamp = f"{current_date_and_time:%Y-%m-%d %H:%M}"

    check_out_dict = {
        "Checked Out":{
            name:[
                {
                    "item_num": item_num,
                    "quantity": quantity,
                    "time_stamp": time_stamp
                }
            ]
        }
    }
    
    with open("checked_out.json", "r") as outfile:
        json_data = json.load(outfile)

    assert check_out_dict == json_data

def test_remove_specific_quantity_from_check_out():
    # Setup Stage
    # Write variable user inputs to checked_out.json
    with open("checked_out.json", "w") as outfile:
        outfile.write(json.dumps({
            "Checked Out": {

            }
        }, indent = 4))

    name = "Trenton Murdock"
    item_num = "A001"

    # Exercise stage
    add_to_checked_out_dict(name, item_num, quantity=3)
    remove_item_from_check_out(name, item_num, quantity=1)

    # Verify Stage
    # Create a time_stamp variable
    time_stamp = f"{current_date_and_time:%Y-%m-%d %H:%M}"

    check_out_dict = {
        "Checked Out":{
            name:[
                {
                    "item_num": item_num,
                    "quantity": 2,
                    "time_stamp": time_stamp
                }
            ]
        }
    }
    
    with open("checked_out.json", "r") as outfile:
        json_data = json.load(outfile)

    assert check_out_dict == json_data   

def test_remove_all_items_from_check_out():

    # Setup Stage
    # Write variable user inputs to checked_out.json
    with open("checked_out.json", "w") as outfile:
        outfile.write(json.dumps({
            "Checked Out": {

            }
        }, indent = 4))

    name = "Trenton Murdock"
    item_num = "A001"
    quantity = 1

    # Exercise stage
    remove_item_from_check_out(name, item_num, quantity)

    # Verify stage
    check_out_dict = {
        "Checked Out": {}
    }
    
    with open("checked_out.json", "r") as outfile:
        json_data = json.load(outfile)

    assert check_out_dict == json_data


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])