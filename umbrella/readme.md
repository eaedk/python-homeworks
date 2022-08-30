# Challenge - Umbrella

![](https://images.unsplash.com/photo-1457131760772-7017c6180f05?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1036&q=80)

## **Description**:
Every morning, Simone puts her umbrella in her bag.

Her day is divided in three parts : morning, afternoon and evening.
- She will take her umbrella out of her bag if, at any point of the day, the weather becomes `rainy` or a `thunderstorm`.
- She will keep her umbrella in her bag if the weather is `sunny` or `cloudy`.
- She will always start the day with the umbrella in her bag, no matter the previous day's weather.

Write a function counting how many times will Simone take her umbrella out of her bag regarding the weather conditions.

## **Instructions**:

- Complete with the **logic and document** the function left empty for in the file `solution.py`, .
- **DO NOT CHANGE THE FUNCTION'S NAME NOR PARAMETER.**
- The function takes as input a variable `weather` that is a list of weathers, three information per day.
- The function should return the number of times Simone will take her umbrella out of her bag.
- Follow the guide in `guide.py` if you struggle a bit to start.


## **Examples**:
- `weather = ["rainy", "sunny", "rainy", "sunny", "rainy", "rainy"]` => Simone takes her umbrella out of her bag `3` times.
- `weather = ['sunny', 'cloudy', 'sunny', 'rainy', 'rainy', 'thunderstorm']` => Simone takes her umbrella out of her bag `1` time.
- `weather = ['rainy', 'rainy', 'rainy']` => Simone takes her umbrella out of her bag `1` time.

## **Code**:
```python
result = proposal(weather=["rainy", "sunny", "rainy", "sunny", "rainy", "rainy"])

print(result)

>>> 3
```