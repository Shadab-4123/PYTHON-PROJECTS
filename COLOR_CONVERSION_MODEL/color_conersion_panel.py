""" 
Functions for Assignment A3

This file contains the functions for the assignment. You should replace the stubs
with your own implementations.

SHADAB RAZA     
DATE: 22 Feb, 2023
"""
import introcs


def complement_rgb(rgb):
    """
    Returns the complement of color rgb.
    
    Parameter rgb: the color to complement
    Precondition: rgb is an RGB object
    """
    
    return introcs.RGB(255 - rgb.red, 255 - rgb.green, 255 - rgb.blue)


def str5(s):
    """
    Returns value as a string, but expanded or rounded to be exactly 5 characters.
    
    The decimal point counts as one of the five characters.
   
    Examples:
        str5(1.3546)  is  '1.355'.
        str5(21.9954) is  '22.00'.
        str5(21.994)  is  '21.99'.
        str5(130.59)  is  '130.6'.
        str5(130.54)  is  '130.5'.
        str5(1)       is  '1.000'.
    
    Parameter value: the number to convert to a 5 character string.
    Precondition: value is a number (int or float), 0 <= value <= 360.
    """
    # Remember that the rounding takes place at a different place depending 
    # on how big value is. Look at the examples in the specification.
    if 'e' in str(s):
        s1 = "{:.5f}".format(s)
        
        return (str5(float(s1)))

    elif len(str(s)) > 5:
        k         = str(float(s))
        slicc1    = k[:k.find('.')+1]
        l         = (5 - len(str(slicc1)))
        check_all = str("{:.{}f}".format(s, l))

        return check_all if len(check_all)==5 else check_all[:-1]

    else:
        k = str(float(s))
        
        slicc2 = k[:k.find('.')+1]
        
        l = (5 - len(str(slicc2)))
        
        return str("{:.{}f}".format(s, l))    



def str5_cmyk(cmyk):
    """
    Returns the string representation of cmyk in the form "(C, M, Y, K)".
    
    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)
    
    Example: if str(cmyk) is 
    
          '(0.0,31.3725490196,31.3725490196,0.0)'
    
    then str5_cmyk(cmyk) is '(0.000, 31.37, 31.37, 0.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter cmyk: the color to convert to a string
    Precondition: cmyk is an CMYK object.
    """
    return '('+((str5(cmyk.cyan)+ ', ' + str5(cmyk.magenta) + ', ' + str5(cmyk.yellow) + ', ' + str5(cmyk.black)))+')'
    

def str5_hsv(hsv):
    """
    Returns the string representation of hsv in the form "(H, S, V)".
    
    In the output, each of H, S, and V should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsv)
    
    Example: if str(hsv) is 
    
          '(0.0,0.313725490196,1.0)'
    
    then str5_hsv(hsv) is '(0.000, 0.314, 1.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter hsv: the color to convert to a string
    Precondition: hsv is an HSV object.
    """
    return ('('+(( str5(hsv.hue)  + ', ' + str5(hsv.saturation) + ', ' + str5(hsv.value)))+')')


    


def rgb_to_cmyk(rgb):
    """
    Returns a CMYK object equivalent to rgb, with the most black possible.
    
    Formulae from https://www.rapidtables.com/convert/color/rgb-to-cmyk.html
    
    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to the range 0..1 by dividing them by 255.0.
    red     = rgb.red    / 255
    green   = rgb.green / 255
    blue    = rgb.blue / 255
    black   = 1 - max(red, green, blue)

    if black == 1:

        return introcs.CMYK(0.0, 0.0, 0.0, 100.0)

    else:

        c   = ( 1 - red   - black) / ( 1 - black )
        m   = ( 1 - green - black) / ( 1 - black )
        y   = ( 1 - blue  - black) / ( 1 - black )

        return introcs.CMYK(c * 100, m * 100, y * 100, black * 100)    


def cmyk_to_rgb(cmyk):
    """
    Returns an RGB object equivalent to cmyk
    
    Formulae from https://www.rapidtables.com/convert/color/cmyk-to-rgb.html
   
    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object.
    """
    # The CMYK numbers are in the range 0.0..100.0. 
    # Deal with them the same way as the RGB numbers in rgb_to_cmyk()

    cyan      = cmyk.cyan     / 100
    magenta   = cmyk.magenta / 100
    yellow    = cmyk.yellow / 100
    black     = cmyk.black / 100
    red       = ( 1 - cyan ) * ( 1 - black )
    green     = ( 1 - magenta ) * ( 1 - black )
    blue      = ( 1 - yellow ) * ( 1 - black )

    return introcs.RGB(round(red * 255), round(green * 255), round(blue * 255))


def rgb_to_hsv(rgb):
    """
    Return an HSV object equivalent to rgb
    
    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV
   
    Parameter hsv: the color to convert to a HSV object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to range 0..1 by dividing them by 255.0.

    red   = rgb.red    / 255
    green = rgb.green / 255
    blue  = rgb.blue / 255
    maxm  = max(red, green, blue)
    minm  = min(red, green, blue)

    if maxm == minm:
        hue=0

    elif maxm == red and green >= blue:
        hue = 60.0 * ( green - blue ) / ( maxm - minm )

    elif maxm == red and green < blue:
        hue = 60.0 * ( green - blue ) / ( maxm - minm ) + 360.0

    elif maxm == green:
        hue = 60.0 * ( blue - red ) / ( maxm - minm ) + 120.0

    elif maxm == blue:
        hue = 60.0 * ( red - green ) / ( maxm - minm ) + 240.0 

    if maxm == 0:
        saturation = 0
    else:
        saturation = 1 - minm / maxm

    value = maxm 

    return introcs.HSV(float(hue), float(saturation), float(value))


def hsv_to_rgb(hsv):
    """
    Returns an RGB object equivalent to hsv
    
    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV
    
    Parameter hsv: the color to convert to a RGB object
    Precondition: hsv is an HSV object.
    """
    hue        = hsv.hue
    saturation = hsv.saturation
    value      = hsv.value
    hi         = hue // 60
    f   = hue / 60 - hi
    p   = value * (1 - saturation)
    q   = value * (1 - f * saturation)
    t   = value * (1 - (1 - f) * saturation)

    if hi == 0 or hi == 5:
        red = value
    elif hi == 1:
        red = q
    elif hi == 2 or hi == 3:
        red = p
    elif hi == 4:
        red = t

    if hi == 0:
        green = t
    elif hi == 1 or hi == 2:
        green = value
    elif hi==3:
        green = q
    elif hi == 4 or hi == 5:
        green = p

    if hi == 0 or hi == 1:
        blue = p
    elif hi == 2:
        blue = t
    elif hi == 3 or hi == 4:
        blue = value
    elif hi == 5:
        blue = q

    return introcs.RGB(round(red * 255), round(green * 255), round(blue * 255))        


def contrast_value(value,contrast):
    """
    Returns value adjusted to the "sawtooth curve" for the given contrast
    
    At contrast = 0, the curve is the normal line y = x, so value is unaffected.
    If contrast < 0, values are pulled closer together, with all values collapsing
    to 0.5 when contrast = -1.  If contrast > 0, values are pulled farther apart, 
    with all values becoming 0 or 1 when contrast = 1.
    
    Parameter value: the value to adjust
    Precondition: value is a float in 0..1
    
    Parameter contrast: the contrast amount (0 is no contrast)
    Precondition: contrast is a float in -1..1
    """
   

    if contrast == 1:
        if value >= 0.5:
            return 1
        else:
            return 0  
    if value < 0.25 + 0.25 * contrast:
        return (( 1 - contrast ) / ( 1 + contrast )) * value           
    elif value  > 0.75 - 0.25 * contrast:
        return (( 1 - contrast ) / ( 1 + contrast )) * ( value - ( 3 - contrast ) / 4 ) + ( 3 + contrast ) / 4

    else:
        return (( 1 + contrast ) / ( 1 - contrast )) * ( value - ( 1 + contrast ) / 4 ) + ( 1 - contrast ) / 4     


def contrast_rgb(rgb, contrast):
    """
    Applies the given contrast to the RGB object rgb
    
    This function is a PROCEDURE.  It modifies rgb and has no return value.  It should
    apply contrast_value to the red, blue, and green values.
    
    Parameter rgb: the color to adjust
    Precondition: rgb is an RGB object
    
    Parameter contrast: the contrast amount (0 is no contrast)
    Precondition: contrast is a float in -1..1
    """

    red       = rgb.red / 255
    green     = rgb.green / 255
    blue      = rgb.blue / 255

    rgb.red   = round( contrast_value(red,contrast) * 255)
    rgb.green = round(contrast_value(green,contrast) * 255)
    rgb.blue  = round(contrast_value(blue,contrast) * 255)