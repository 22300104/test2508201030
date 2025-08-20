def fahrenheit_to_celsius(fahrenheit):
  """화씨 온도를 섭씨로 변환합니다."""
  celsius = (fahrenheit - 32) * 5/9
  return celsius

# 사용자로부터 화씨 온도 입력받기
f_temp = float(input("화씨 온도를 입력하세요: "))
c_temp = fahrenheit_to_celsius(f_temp)

print(f"화씨 {f_temp}°F는 섭씨 {c_temp:.2f}°C 입니다.")