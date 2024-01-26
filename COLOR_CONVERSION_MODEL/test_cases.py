""" 
Unit Test for Assignment A3

This module implements several test cases for a3.  It is incomplete.  You should look 
though this file for places to add tests.

SHADAB RAZA
DATE: 23 Feb, 2023
""" 
import introcs
import a3


def test_complement():
    """
    Test function complement
    """
    print('Testing complement')
    
    # One test is really good enough here
    comp = a3.complement_rgb(introcs.RGB(250, 0, 71))
    introcs.assert_equals(255-250, comp.red)
    introcs.assert_equals(255-0,   comp.green)
    introcs.assert_equals(255-71,  comp.blue)
    
    # One more for good measure
    comp = a3.complement_rgb(introcs.RGB(128, 64, 255))
    introcs.assert_equals(255-128, comp.red)
    introcs.assert_equals(255-64,  comp.green)
    introcs.assert_equals(255-255, comp.blue)


def test_str5():
    """
    Test function str5
    """
    print('Testing str5')

    introcs.assert_equals('130.6',  a3.str5(130.59))
    introcs.assert_equals('130.5',  a3.str5(130.54))
    introcs.assert_equals('100.0',  a3.str5(100))
    introcs.assert_equals('100.6',  a3.str5(100.56))
    introcs.assert_equals('99.57',  a3.str5(99.566))
    introcs.assert_equals('99.99',  a3.str5(99.99))
    introcs.assert_equals('100.0',  a3.str5(99.995))
    introcs.assert_equals('22.00',  a3.str5(21.99575))
    introcs.assert_equals('21.99',  a3.str5(21.994))
    introcs.assert_equals('10.01',  a3.str5(10.013567))
    introcs.assert_equals('10.00',  a3.str5(10.000000005))
    introcs.assert_equals('10.00',  a3.str5(9.9999))
    introcs.assert_equals('9.999',  a3.str5(9.9993))
    introcs.assert_equals('1.355',  a3.str5(1.3546))
    introcs.assert_equals('1.354',  a3.str5(1.3544))
    introcs.assert_equals('0.046',  a3.str5(.0456))
    introcs.assert_equals('0.045',  a3.str5(.0453))
    introcs.assert_equals('0.006',  a3.str5(.0056))
    introcs.assert_equals('0.001',  a3.str5(.0013))
    introcs.assert_equals('0.000',  a3.str5(.0004))
    introcs.assert_equals('0.001',  a3.str5(.0009999))
    introcs.assert_equals('0.000',  a3.str5(1e-9))


def test_str5_color():
    """
    Test the str5 functions for cmyk and hsv.
    """
    print('Testing str5_cmyk and str5_hsv')
    
    # Tests for str5_cmyk
    # We need to make sure the coordinates round properly
    text = a3.str5_cmyk(introcs.CMYK(98.448, 25.362, 72.8, 1.0))
    introcs.assert_equals('(98.45, 25.36, 72.80, 1.000)',text)
    
    text = a3.str5_cmyk(introcs.CMYK(0.0, 1.5273, 100.0, 57.846))
    introcs.assert_equals('(0.000, 1.527, 100.0, 57.85)',text)
    
    text = a3.str5_hsv(introcs.HSV(1.1, 0.8968, 0.2))
    introcs.assert_equals('(1.100, 0.897, 0.200)',text)

    text = a3.str5_hsv(introcs.HSV(96.769, 0.7958, 0.261))
    introcs.assert_equals('(96.77, 0.796, 0.261)',text)



def test_rgb_to_cmyk():
    """
    Test translation function rgb_to_cmyk
    """
    print('Testing rgb_to_cmyk')
    
    # The function should guarantee accuracy to three decimal places
    
    # Check for Upper extreme value conversion
    rgb = introcs.RGB(255, 255, 255)
    cmyk = a3.rgb_to_cmyk(rgb)
    introcs.assert_equals(0.0, round(cmyk.cyan,3))
    introcs.assert_equals(0.0, round(cmyk.magenta,3))
    introcs.assert_equals(0.0, round(cmyk.yellow,3))
    introcs.assert_equals(0.0, round(cmyk.black,3))
    
    # Check for Lower extreme value conversion ( when black is equal to 1 )
    rgb = introcs.RGB(0, 0, 0)
    cmyk = a3.rgb_to_cmyk(rgb)
    introcs.assert_equals(0.0, round(cmyk.cyan,3))
    introcs.assert_equals(0.0, round(cmyk.magenta,3))
    introcs.assert_equals(0.0, round(cmyk.yellow,3))
    introcs.assert_equals(100.0, round(cmyk.black,3))
        
    # Check for Intermediate value conversion    
    rgb = introcs.RGB(217, 43, 164)
    cmyk = a3.rgb_to_cmyk(rgb)
    introcs.assert_equals(0.0, round(cmyk.cyan,3))
    introcs.assert_equals(80.184, round(cmyk.magenta,3))
    introcs.assert_equals(24.424, round(cmyk.yellow,3))
    introcs.assert_equals(14.902, round(cmyk.black,3))


def test_cmyk_to_rgb():
    """
    Test translation function cmyk_to_rgb
    """
    print('Testing cmyk_to_rgb')

    # The function should guarantee accuracy to three decimal places

    # Check for Lower extreme value conversion
    cmyk = introcs.CMYK(0.0, 0.0, 0.0, 100.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(0.0, round(rgb.red,3))
    introcs.assert_equals(0.0, round(rgb.green,3))
    introcs.assert_equals(0.0, round(rgb.blue,3))
    
    # Check for Upper extreme value conversion
    cmyk = introcs.CMYK(100.0, 100.0, 100.0, 100.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(0.0, round(rgb.red,3))
    introcs.assert_equals(0.0, round(rgb.green,3))
    introcs.assert_equals(0.0, round(rgb.blue,3))
    
    # Check for Intermediate extreme value conversion
    cmyk = introcs.CMYK(21.56, 6.12, 1.64, 45.96)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(108, round(rgb.red,3))
    introcs.assert_equals(129, round(rgb.green,3))
    introcs.assert_equals(136, round(rgb.blue,3))
    


def test_rgb_to_hsv():
    """
    Test translation function rgb_to_hsv
    """
    print('Testing rgb_to_hsv')
    

    # The function should guarantee accuracy to three decimal places

    # Check for Upper extreme value conversion ( when maximum = minimum )

    rgb = introcs.RGB(255, 255, 255)
    hsv = a3.rgb_to_hsv(rgb)
    introcs.assert_equals(0.0, round(hsv.hue, 3))
    introcs.assert_equals(0.0, round(hsv.saturation, 3))
    introcs.assert_equals(1.0, round(hsv.value, 3))
    

    # Check for conversion value ( When maximum = red and green >= blue )

    rgb = introcs.RGB(255, 65, 45)
    hsv = a3.rgb_to_hsv(rgb)
    introcs.assert_equals(5.714, round(hsv.hue, 3))
    introcs.assert_equals(0.824, round(hsv.saturation, 3))
    introcs.assert_equals(1.0, round(hsv.value, 3))

    # Check for conversion value ( When maximum = red and green < blue )

    rgb = introcs.RGB(245, 45, 65)
    hsv = a3.rgb_to_hsv(rgb)
    introcs.assert_equals(354.0, round(hsv.hue, 3))
    introcs.assert_equals(0.816, round(hsv.saturation, 3))
    introcs.assert_equals(0.961, round(hsv.value, 3))

    # Check for conversion value ( When maximum = green )

    rgb = introcs.RGB(145, 215, 36)
    hsv = a3.rgb_to_hsv(rgb)
    introcs.assert_equals(83.464, round(hsv.hue, 3))
    introcs.assert_equals(0.833, round(hsv.saturation, 3))
    introcs.assert_equals(0.843, round(hsv.value, 3))

    # Check for conversion value ( When maximum = blue )

    rgb = introcs.RGB(45, 125, 235)
    hsv = a3.rgb_to_hsv(rgb)
    introcs.assert_equals(214.737, round(hsv.hue, 3))
    introcs.assert_equals(0.809, round(hsv.saturation, 3))
    introcs.assert_equals(0.922, round(hsv.value, 3))

    # Check for conversion value ( When maximum = 0 and saturation = 0 )

    rgb = introcs.RGB(0, 0, 0)
    hsv = a3.rgb_to_hsv(rgb)
    introcs.assert_equals(0.0, round(hsv.hue, 3))
    introcs.assert_equals(0.0, round(hsv.saturation, 3))
    introcs.assert_equals(0.0, round(hsv.value, 3))

    # Check for Intermediate value conversion
    rgb = introcs.RGB(214, 189, 45)
    hsv = a3.rgb_to_hsv(rgb)
    introcs.assert_equals(51.124, round(hsv.hue, 3))
    introcs.assert_equals(0.79, round(hsv.saturation, 3))
    introcs.assert_equals(0.839, round(hsv.value, 3))


def test_hsv_to_rgb():
    """
    Test translation function hsv_to_rgb
    """
    print('Testing hsv_to_rgb')
    

    # The function should guarantee accuracy to three decimal places

    # Check for Lower extreme value conversion ( hi equal to 0)
    hsv = introcs.HSV(0.0, 0.0, 0.0)
    rgb = a3.hsv_to_rgb(hsv)
    introcs.assert_equals(0, round(rgb.red,3))
    introcs.assert_equals(0, round(rgb.green,3))
    introcs.assert_equals(0, round(rgb.blue,3))

    # Check for value conversion ( when hi is equal to 1 )
    hsv = introcs.HSV(87.996, 1.0, .925)
    rgb = a3.hsv_to_rgb(hsv)
    introcs.assert_equals(126, round(rgb.red,3))
    introcs.assert_equals(236, round(rgb.green,3))
    introcs.assert_equals(0, round(rgb.blue,3))


    # Check for extreme value conversion ( when hi is equal to 2 )
    hsv = introcs.HSV(145.0, 0.0, 1.0)
    rgb = a3.hsv_to_rgb(hsv)
    introcs.assert_equals(255, round(rgb.red,3))
    introcs.assert_equals(255, round(rgb.green,3))
    introcs.assert_equals(255, round(rgb.blue,3))

    # Check for extreme value conversion ( when hi is equal to 3 )
    hsv = introcs.HSV(180.0, 0.9, .78)
    rgb = a3.hsv_to_rgb(hsv)
    introcs.assert_equals(20, round(rgb.red,3))
    introcs.assert_equals(199, round(rgb.green,3))
    introcs.assert_equals(199, round(rgb.blue,3))

    # Check for extreme value conversion ( when hi is equal to 4 )
    hsv = introcs.HSV(288.0, 0.6, 0.6)
    rgb = a3.hsv_to_rgb(hsv)
    introcs.assert_equals(135, round(rgb.red,3))
    introcs.assert_equals(61, round(rgb.green,3))
    introcs.assert_equals(153, round(rgb.blue,3))

    # Check for extreme value conversion ( when hi is equal to 5 )
    hsv = introcs.HSV(276.0, 0.7, 0.3)
    rgb = a3.hsv_to_rgb(hsv)
    introcs.assert_equals(55, round(rgb.red,3))
    introcs.assert_equals(23, round(rgb.green,3))
    introcs.assert_equals(76, round(rgb.blue,3))



def test_contrast_value():
    """
    Test translation function contrast_value
    """
    print('Testing contrast_value')
    
    # contrast == -1.0 (extreme)
    result = a3.contrast_value(0.0,-1.0)
    introcs.assert_floats_equal(0.5,result)
    
    result = a3.contrast_value(1.0,-1.0)
    introcs.assert_floats_equal(0.5,result)
    
    # contrast < 0, bottom part of sawtooth
    result = a3.contrast_value(0.1,-0.5)
    introcs.assert_floats_equal(0.3,result)
    
    # contrast < 0, middle of sawtooth
    result = a3.contrast_value(0.4,-0.4)
    introcs.assert_floats_equal(0.4571429,result)
    
    # contrast < 0, upper part of sawtooth
    result = a3.contrast_value(0.9,-0.3)
    introcs.assert_floats_equal(0.8142857,result)
    
    # contrast == 0.0, bottom part of sawtooth
    result = a3.contrast_value(0.1,0.0)
    introcs.assert_floats_equal(0.1,result)
    
    # contrast == 0, middle of sawtooth
    result = a3.contrast_value(0.6,0.0)
    introcs.assert_floats_equal(0.6,result)
    
    # contrast == 0.0, upper part of sawtooth
    result = a3.contrast_value(0.9,0.0)
    introcs.assert_floats_equal(0.9,result)
    
    # contrast > 0, bottom part of sawtooth
    result = a3.contrast_value(0.1,0.3)
    introcs.assert_floats_equal(0.05384615,result)
    
    # contrast > 0, middle of sawtooth
    result = a3.contrast_value(0.4,0.5)
    introcs.assert_floats_equal(0.2,result)
    
    # contrast > 0, upper part of sawtooth
    result = a3.contrast_value(0.9,0.4)
    introcs.assert_floats_equal(0.95714286,result)
    
    # contrast == 1.0 (extreme)
    result = a3.contrast_value(0.2,1.0)
    introcs.assert_floats_equal(0.0,result)
    
    result = a3.contrast_value(0.6,1.0)
    introcs.assert_floats_equal(1.0,result)


def test_contrast_rgb():
    """
    Test translation function contrast_value
    """
    print('Testing contrast_rgb')
    
    # Negative contrast
    rgb = introcs.RGB(240, 15, 118)
    hsv = a3.contrast_rgb(rgb,-0.4)
    introcs.assert_equals(220, rgb.red)
    introcs.assert_equals(35,  rgb.green)
    introcs.assert_equals(123, rgb.blue)
    
    # Zero contrast
    rgb = introcs.RGB(240, 15, 118)
    hsv = a3.contrast_rgb(rgb, 0.0)
    introcs.assert_equals(240, rgb.red)
    introcs.assert_equals(15,  rgb.green)
    introcs.assert_equals(118, rgb.blue)


    # Positive contrast
    rgb = introcs.RGB(240, 15, 118)
    hsv = a3.contrast_rgb(rgb,0.4)
    introcs.assert_equals(249, rgb.red)
    introcs.assert_equals(6,  rgb.green)
    introcs.assert_equals(105, rgb.blue)
    
    
    


# Script Code
# THIS PREVENTS THE TESTS RUNNING ON IMPORT
if __name__ == '__main__':
    test_complement()
    test_str5()
    test_str5_color()
    test_rgb_to_cmyk()
    test_cmyk_to_rgb()
    test_rgb_to_hsv()
    test_hsv_to_rgb()
    test_contrast_value()
    test_contrast_rgb()
    print('Module a3 passed all tests.')
