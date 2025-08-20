def calculate_sum(numbers):
  """숫자 리스트를 받아 총합을 반환합니다."""
  total = sum(numbers)
  return total

my_numbers = [10, 20, 30, 40, 50]
result = calculate_sum(my_numbers)

print(f"리스트의 총합: {result}")