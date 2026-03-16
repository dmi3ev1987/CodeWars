class List(object):
    def count_spec_digits(self, integers_list, digits_list):
        result = []
        for digit in digits_list:
            count = 0
            for integer in integers_list:
                count += str(integer).count(str(digit))
            result.append((digit, count))
        return result