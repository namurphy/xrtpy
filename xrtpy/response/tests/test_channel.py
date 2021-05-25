import pytest
from xrtpy.response.channel import Channel

channel_names = [
    "Al-mesh",
    "Al-poly",
    "C-poly",
    "Ti-poly",
    "Be-thin",
    "Be-med",
    "Al-med",
    "Al-thick",
    "Be-thick",
    "Al-poly/Al-mesh",
    "Al-poly/Ti-poly",
    "Al-poly/Al-thick",
    "Al-poly/Be-thick",
    "C-poly/Ti-poly",
]


@pytest.mark.parametrize("channel_name", channel_names)
def test_channel_name(channel_name):
    channel = Channel(channel_name)
    assert channel.name == channel_name


cls_args_attribute = [
    (
        Channel,  # class
        [
        "Al-mesh", 
        "Al-poly", 
        "C-poly",
        "Ti-poly",
        "Be-thin",
        "Be-med",
        "Al-med",
        "Al-thick", 
        "Be-thick",
        "Al-poly/Al-mesh",
        "Al-poly/Ti-poly", 
        "Al-poly/Al-thick",
        "Al-poly/Be-thick", 
        "C-poly/Ti-poly", 
        ],  # args
        [
            "name",
            "wavelength",  # second attribute
            "transmission",
            "number_of_wavelengths",  # first attribute
        ],
    ),
    (
        geometry,  # class
        [],  # no arguments go to this class
        [
            "name",
            "focal_len",  # first attribute
            "aperture_area",  # second attribute
    ),
    (
        entrance_filter,  # class
        [],  # no arguments go to this class
        [
            "name",
            "filter_material",  # first attribute
            "filter_thickness",  # second attribute
            "filter_density",
            "wavelength",
            "transmission",
            "number_of_wavelengths",
            "mesh_trans",
            "substrate",
        ]
    ),
    (
        mirror_1,  # class
        [],  # no arguments go to this class
        [
            "name",
            "material",  # first attribute
            "density",  # second attribute
            "graze_angle",
            "wavelength",
            "REFL",
            "number_of_wavelengths",
        ]
    ),
    (
        mirror_2,  # class
        [],  # no arguments go to this class
        [
            "name",
            "material",  # first attribute
            "density",  # second attribute
            "graze_angle",
            "wavelength",
            "REFL",
            "number_of_wavelengths",
        ]
    ),
    (
        filter1,  # class
        [],  # no arguments go to this class
        [
            "name",
            "material",  # first attribute
            "filter1_thickness",  # second attribute
            "filter_density",
            "wavelength",  # first attribute
            "transmission",  # second attribute
            "number_of_wavelengths",
            "mesh_trans",  # first attribute
            "substrate",  # second attribute
        ]
    ),
    (
        filter2,  # class
        [],  # no arguments go to this class
        [
            "name",
            "material",  # first attribute
            "filter1_thickness",  # second attribute
            "filter_density",
            "wavelength",  # first attribute
            "transmission",  # second attribute
            "number_of_wavelengths",
            "mesh_trans",  # first attribute
            "substrate",  # second attribute
        ]
    ),
    (
        CCD,  # class
        [],  # no arguments go to this class
        [
            "name",
            "ev_ore_el",  # first attribute
            "full_well",  # second attribute
            "gain_l",
            "gain_r",
            "quantum_efficiency",  # first attribute
            "number_of_wavelengths",  # second attribute
            "ev_pre_el",
            "pixel_size",  # first attribute
            "wavelength",  # second attribute
        ]
    )  
]
#cls: "Channel,geometry,entrance_filter,mirror_1,mirror_2,filter1,filter2,CCD"

#argC name,wavelength,transmission,number_of_wavelengths, observatory, instrument
#argG name, focal_len, aperture_area
#argE name, filter_material,filter_thickness,filter_density, wavelength,transmission,number_of_wavelengths,mesh_trans,substrate

@pytest.mark.parametrize("cls, args, attribute", cls_args_attribute)
def test_attributes(cls, args, attribute):
    instance = cls(*args)
    getattr(instance, attribute)

####################################################

class ExampleClass():
    
    @property
    def first_property(self):
        return 1
    
    @property
    def second_property(self):
        return "2"

#put the names of properties we want to check

properties_to_check = ["first_property", "second_property", "third_property"]

@pytest.mark.parametrize("property", properties_to_check)
def test_accessing_property(property):
    instance = ExampleClass()  # change to name of class being checked
    getattr(instance, property)


# put the names of properties and the expected values
properties_and_expected_values = [
    ("first_property", 1), 
    ("second_property", "2"), 
    ("third_property", "three"), # this test should fail
]

@pytest.mark.parametrize("property, expected_value", properties_and_expected_values)
def test_accessing_property(property, expected_value):
    instance = ExampleClass()  # change to name of class being checked
    actual_value = getattr(instance, property)
    assert actual_value == expected_value