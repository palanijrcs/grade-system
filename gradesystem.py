def get_grade(mark):
    """Return the letter grade for a valid mark."""
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


def main():
    while True:
        try:
            mark = float(input("Enter your mark (0-100): "))

            if mark < 0 or mark > 100:
                print("Invalid mark. Please enter a number between 0 and 100.")
                continue

            grade = get_grade(mark)

            # Display whole numbers without .0
            if mark.is_integer():
                display_mark = int(mark)
            else:
                display_mark = mark

            print(f"Mark: {display_mark} -> Grade: {grade}")
            break

        except ValueError:
            print("Invalid input. Please enter a number between 0 and 100.")


if __name__ == "__main__":
    main()