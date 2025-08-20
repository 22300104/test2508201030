def celsius_to_fahrenheit(celsius):
  """섭씨 온도를 화씨로 변환합니다."""
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

# 사용자로부터 섭씨 온도 입력받기
c_temp = float(input("섭씨 온도를 입력하세요: "))
f_temp = celsius_to_fahrenheit(c_temp)

print(f"섭씨 {c_temp}°C는 화씨 {f_temp:.2f}°F 입니다.")

password='1234'
input(password)
## 이건 test branch 코드입니다.
## 차이점 추가
## 차이점 추가 11시 48분