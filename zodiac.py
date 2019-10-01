mon = int(input("What is your birth month? (number format)"))
day = int(input("What is your birth day? (number format)"))

def print_zodiac_sign(month, day):
	if month == 1:
		if day >= 20:
			print("Aquarius")
		else:
			print("Capricorn")

	if month == 2:
		if day <= 18:
			print("Aquarius")
		else:
			print("Pisces")

	if month == 3:
		if day <= 20:
			print("Pisces")
		else:
			print("Aries")

	if month == 4:
		if day <= 19:
			print("Aries")
		else:
			print("Taurus")

	if month == 5:
		if day <=  20:
			print("Taurus")
		else:
			print("Gemini")

	if month == 6:
		if day <= 20:
			print("Gemini")
		else:
			print("Cancer")

	if month == 7:
		if day <= 22:
			print("Cancer")
		else:
			print("Leo")

	if month == 8:
		if day <= 22:
			print("Leo")
		else:
			print("Virgo")

	if month == 9:
		if day <= 22:
			print("Virgo")
		else:
			print("Libra")

	if month == 10:
		if day <= 22:
			print("Libra")
		else:
			print("Scorpio")

	if month == 11:
		if day <= 21:
			print("Scorpio")
		else:
			print("Sagittarius")

	if month == 12:
		if day <= 21:
			print("Sagittarius")
		else:
			print("Capricorn")

print_zodiac_sign(mon, day)
