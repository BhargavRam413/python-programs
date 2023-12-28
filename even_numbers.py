

def find_even_numbers_in_range(numbers_range):
 
    try:
        return [i for i in range(numbers_range) if check_number_is_even_or_not()]

    except Exception as ex:
        logging.error(f" exception occured {str(ex)}")
        return None
    

def check_number_is_even_or_not(number):
    try:
        return number % 2 == 0
    except Exception as ex:
        logging.error(f" exception occured {str(ex)}")
        return None


even_numbers = find_even_numbers_in_range(10)
print(f" even numbers {even_numbers}")
print(check_number_is_even_or_not(8))