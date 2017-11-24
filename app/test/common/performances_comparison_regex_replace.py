from timeit import default_timer as timer

from app.common.string_methods import get_amount, clean_amount

amount_string = "-10,198,127 $"

start = timer()
get_amount(amount_string)
end = timer()

ellapsed_time_regex = end - start
print("regex: {}".format(ellapsed_time_regex))

start = timer()
clean_amount(amount_string)
end = timer()

ellapsed_time_replace = end - start
print("replace: {}".format(ellapsed_time_replace))

print("Ratio: {}".format(ellapsed_time_regex / ellapsed_time_replace))