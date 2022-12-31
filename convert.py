# Done
def convert_temp(unit_in, unit_out, temp):
	"""Convert farenheit <-> celsius and return results.

	- unit_in: either "f" or "c" 
	- unit_out: either "f" or "c"
	- temp: temperature (in f or c, depending on unit_in)

	Return results of conversion, if any.

	If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

	For example:

	  convert_temp("c", "f", 0)  =>  32.0
	  convert_temp("f", "c", 212) => 100.0
	"""
	if unit_in.__eq__( "f" or "F") and unit_out.__eq__("c" or "C"):
		print('0 if')
		temp = temp - 32
		temp = temp * 5/9
		return temp
	elif unit_in.__eq__("c" or "C") and unit_out.__eq__("f" or "F"):
		print('1 elif')
		temp = ((temp * 5)/9)
		temp = temp +32
		return temp 
	elif unit_in == unit_out:
		print('2 elif')
		return temp 
	elif unit_in.__eq__("c" or "C") and unit_out.__eq__("f" or "F"):
		print('3 elif')
		temp = ((temp * 5)/9)
		temp = temp +32
		return temp 
	elif unit_in.__eq__("f" or "F") and unit_out.__eq__("c" or "C"):
		print('4 elif')
		temp = ((temp * 5)/9)
		temp = temp +32
		return temp 
	elif unit_in.__eq__("f" or "c") and (unit_out != "f" or "c"):
		print('5 elif')
		return "Invalid"
	else: 
		return "Invalid"

# test calls 
print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")

