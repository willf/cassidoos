# Given a list of numbers, return all groups of repeating consecutive numbers.
# for example,
# repeated_groups([1, 2, 2, 4, 5]) -> [[2, 2]]
# repeated_groups([1, 2, 2, 4, 4, 5]) -> [[2, 2], [4, 4]]
# repeated_groups([1, 1, 0, 0, 8, 4, 4, 4, 3, 2, 1, 9, 9]) -> [[1, 1], [0, 0], [4, 4, 4], [9, 9]]

def repeated_groups(numbers)
  repeated_groups_rec(numbers, [], []).filter { |group| group.length > 1 }
end

def repeated_groups_rec(numbers, current_group, repeated_groups)
  return ([current_group] + repeated_groups).reverse if numbers.empty?
  first_number = numbers[0]
  last_number = current_group[0]
  rest_of_numbers = numbers[1..-1]
  if last_number.nil?
    repeated_groups_rec(rest_of_numbers, [first_number], repeated_groups)
  elsif first_number == last_number
    repeated_groups_rec(rest_of_numbers, [first_number] + current_group, repeated_groups)
  else
    repeated_groups_rec(rest_of_numbers, [first_number], [current_group] + repeated_groups)
  end
end
